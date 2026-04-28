var childProcess = require("child_process");
var fs = require("fs");
var path = require("path");
var posixPath = path.posix;

var STYLE_ALIASES = {
  info: "info",
  warning: "warning",
  danger: "danger",
  error: "danger",
  tip: "success",
  success: "success",
  working: "warning"
};

var STYLE_LABELS = {
  info: "Info",
  warning: "Warning",
  danger: "Warning",
  success: "Tip"
};

var STYLE_ICONS = {
  info: "i",
  warning: "!",
  danger: "!",
  success: "+"
};

var lastUpdatedCache = {};
var branchCache;
var languagesCache;
var summaryCache = {};
var outputTitleCache;

function escapeHtml(value) {
  return String(value || "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function escapeJsonForScript(value) {
  return JSON.stringify(value).replace(/</g, "\\u003c");
}

function getYouTubeEmbedUrl(url) {
  try {
    var parsed = new URL(url);
    var host = parsed.hostname.replace(/^www\./, "");
    var id = "";
    var pathParts = parsed.pathname.split("/").filter(Boolean);

    if (host === "youtu.be") {
      id = pathParts[0] || "";
    } else if (host === "youtube.com" || host === "m.youtube.com") {
      if (pathParts[0] === "watch") {
        id = parsed.searchParams.get("v") || "";
      } else if (pathParts[0] === "embed" || pathParts[0] === "shorts") {
        id = pathParts[1] || "";
      }
    }

    if (/^[A-Za-z0-9_-]{6,}$/.test(id)) {
      return "https://www.youtube-nocookie.com/embed/" + encodeURIComponent(id);
    }
  } catch (error) {
    return "";
  }

  return "";
}

function renderEmbed(url) {
  url = String(url || "").trim();
  if (!url) return "";

  var youtubeUrl = getYouTubeEmbedUrl(url);
  if (youtubeUrl) {
    return [
      '<div class="lib-embed">',
      '<iframe src="' + escapeHtml(youtubeUrl) + '" title="Embedded video" loading="lazy" allowfullscreen ',
      'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"></iframe>',
      "</div>"
    ].join("");
  }

  return '<p class="lib-embed-link"><a href="' + escapeHtml(url) + '">' + escapeHtml(url) + "</a></p>";
}

function getConfigValue(config, key, fallback) {
  if (!config) return fallback;
  if (typeof config.get === "function") {
    var value = config.get(key);
    return value == null ? fallback : value;
  }
  return config[key] == null ? fallback : config[key];
}

function getPluginConfig(context) {
  return context.config.get("pluginsConfig.liberation") || {};
}

function git(args) {
  try {
    return childProcess.execFileSync("git", args, {
      encoding: "utf8",
      stdio: ["ignore", "pipe", "ignore"]
    }).trim();
  } catch (error) {
    return "";
  }
}

function getBranch(config) {
  if (process.env.GITHUB_REF_NAME) return process.env.GITHUB_REF_NAME;
  if (branchCache) return branchCache;
  branchCache = git(["rev-parse", "--abbrev-ref", "HEAD"]);
  return branchCache || getConfigValue(config, "branch", "main");
}

function getLastUpdated(path) {
  if (!path) return "";
  if (lastUpdatedCache[path] !== undefined) return lastUpdatedCache[path];
  lastUpdatedCache[path] = git(["log", "--follow", "-1", "--format=%cI", "--", path]);
  return lastUpdatedCache[path];
}

function buildEditUrl(repo, branch, path) {
  if (!repo || !path) return "";
  return repo.replace(/\/$/, "") + "/edit/" + encodeUrlPath(branch) + "/" + encodeUrlPath(path);
}

function encodeUrlPath(value) {
  return String(value || "")
    .split("/")
    .map(encodeURIComponent)
    .join("/");
}

function normalizeDocPath(value) {
  return String(value || "")
    .replace(/\\/g, "/")
    .replace(/^\.\/+/, "")
    .split("#")[0];
}

function getLanguages() {
  if (languagesCache) return languagesCache;

  var langsPath = path.join(process.cwd(), "LANGS.md");
  var languages = [];

  try {
    fs.readFileSync(langsPath, "utf8").split(/\r?\n/).forEach(function(line) {
      var match = line.match(/\[([^\]]+)\]\(([^)]+)\)/);
      if (!match) return;

      var root = normalizeDocPath(match[2]).replace(/\/+$/, "");
      if (root && fs.existsSync(path.join(process.cwd(), root, "SUMMARY.md"))) {
        languages.push({
          id: root,
          title: match[1]
        });
      }
    });
  } catch (error) {
    languages = [];
  }

  if (languages.length === 0 && fs.existsSync(path.join(process.cwd(), "SUMMARY.md"))) {
    languages.push({
      id: "",
      title: "English"
    });
  }

  languagesCache = languages;
  return languagesCache;
}

function getLanguageRoots() {
  return getLanguages().map(function(language) {
    return language.id;
  });
}

function getDefaultLanguageRoot() {
  var languages = getLanguages();
  return languages.length ? languages[0].id : "";
}

function getLanguageRoot(config) {
  var language = getConfigValue(config, "language", "");
  if (language && fs.existsSync(path.join(process.cwd(), language, "SUMMARY.md"))) {
    return language;
  }
  return "";
}

function sourcePathForRepo(languageRoot, sourcePath) {
  sourcePath = normalizeDocPath(sourcePath);
  return languageRoot ? posixPath.join(languageRoot, sourcePath) : sourcePath;
}

function languageOutputPath(languageRoot, sourcePath) {
  return sourcePathForRepo(languageRoot, markdownToOutputPath(sourcePath));
}

function languageHasSourcePath(languageRoot, sourcePath) {
  return fs.existsSync(path.join(process.cwd(), languageRoot || "", normalizeDocPath(sourcePath)));
}

function languageTargets(sourcePath) {
  return getLanguages().map(function(language) {
    var targetPath = languageHasSourcePath(language.id, sourcePath)
      ? languageOutputPath(language.id, sourcePath)
      : (language.id ? language.id + "/index.html" : "index.html");

    return {
      id: language.id,
      title: language.title,
      targetPath: targetPath
    };
  });
}

function getSummary(languageRoot) {
  var cacheKey = languageRoot || ".";
  if (summaryCache[cacheKey]) return summaryCache[cacheKey];

  var summaryPath = path.join(process.cwd(), languageRoot || "", "SUMMARY.md");
  var summary = {
    nodesByPath: {}
  };

  try {
    fs.readFileSync(summaryPath, "utf8").split(/\r?\n/).forEach(function(line) {
      var match = line.match(/^(\s*)\* \[([^\]]+)\]\(([^)]+)\)/);
      if (!match) return;

      var indent = match[1].replace(/\t/g, "  ").length;
      var depth = Math.floor(indent / 2);
      var node = {
        title: match[2],
        path: normalizeDocPath(match[3]),
        children: []
      };

      summary.stack = summary.stack || [];
      summary.stack[depth] = node;
      summary.stack.length = depth + 1;
      summary.nodesByPath[node.path] = node;

      if (depth > 0 && summary.stack[depth - 1]) {
        summary.stack[depth - 1].children.push(node);
      }
    });
  } catch (error) {
    summary.nodesByPath = {};
  }

  delete summary.stack;
  summaryCache[cacheKey] = summary;
  return summaryCache[cacheKey];
}

function markdownToOutputPath(docPath) {
  docPath = normalizeDocPath(docPath);
  if (/\/?README\.md$/i.test(docPath)) {
    var dir = docPath.replace(/(^|\/)README\.md$/i, "");
    return dir ? dir + "/index.html" : "index.html";
  }
  return docPath.replace(/\.md$/i, ".html");
}

function pageOutputDir(docPath) {
  var outputPath = markdownToOutputPath(docPath);
  var dir = posixPath.dirname(outputPath);
  return dir === "." ? "" : dir;
}

function relativeHref(fromDocPath, targetDocPath) {
  var fromDir = pageOutputDir(fromDocPath) || ".";
  var target = markdownToOutputPath(targetDocPath);
  return posixPath.relative(fromDir, target) || "index.html";
}

function splitStatusTitle(title) {
  var match = String(title || "").match(/^([^A-Za-z0-9\s][^\s]*)\s+(.+)$/);
  return {
    icon: match ? match[1] : "",
    title: match ? match[2] : title
  };
}

function cleanTitle(title) {
  return splitStatusTitle(title).title;
}

function cleanHtmlTitle(title) {
  return String(title || "")
    .replace(/\s*[·|]\s*/g, " | ")
    .split(" | ")
    .map(cleanTitle)
    .filter(Boolean)
    .join(" | ");
}

function fallbackTitleFromFilename(title) {
  return cleanTitle(String(title || "")
    .replace(/\.md$/i, "")
    .replace(/[-_]+/g, " ")
    .replace(/\b\w/g, function(char) {
      return char.toUpperCase();
    }));
}

function walkHtmlFiles(dir, files) {
  files = files || [];

  fs.readdirSync(dir).forEach(function(name) {
    var file = path.join(dir, name);
    var stat = fs.statSync(file);

    if (stat.isDirectory()) {
      walkHtmlFiles(file, files);
    } else if (/\.html$/i.test(name)) {
      files.push(file);
    }
  });

  return files;
}

function copyMissingDirectory(sourceDir, targetDir) {
  if (!fs.existsSync(sourceDir)) return;

  fs.mkdirSync(targetDir, { recursive: true });
  fs.readdirSync(sourceDir).forEach(function(name) {
    var source = path.join(sourceDir, name);
    var target = path.join(targetDir, name);
    var stat = fs.statSync(source);

    if (stat.isDirectory()) {
      copyMissingDirectory(source, target);
    } else if (!fs.existsSync(target)) {
      fs.copyFileSync(source, target);
    }
  });
}

function relativeOutputRoot(file, root) {
  var rel = path.relative(path.dirname(file), root).replace(/\\/g, "/");
  return rel || ".";
}

function getOutputTitleMap() {
  if (outputTitleCache) return outputTitleCache;

  var map = {};
  getLanguageRoots().forEach(function(languageRoot) {
    var nodes = getSummary(languageRoot).nodesByPath;

    Object.keys(nodes).forEach(function(sourcePath) {
      var title = cleanTitle(nodes[sourcePath].title);
      var outputPath = sourcePathForRepo(languageRoot, markdownToOutputPath(sourcePath));
      map[outputPath] = title;

      if (/\/index\.html$/i.test(outputPath)) {
        map[outputPath.replace(/index\.html$/i, "")] = title;
        map[outputPath.replace(/\/index\.html$/i, "")] = title;
      } else if (outputPath === "index.html") {
        map[""] = title;
        map["."] = title;
      }
    });
  });

  outputTitleCache = map;
  return outputTitleCache;
}

function splitHref(href) {
  var index = href.search(/[?#]/);
  if (index === -1) {
    return { base: href, suffix: "" };
  }

  return {
    base: href.slice(0, index),
    suffix: href.slice(index)
  };
}

function shouldSkipHref(href) {
  return !href || /^(?:[a-z][a-z0-9+.-]*:|\/\/|#)/i.test(href);
}

function relativeOutputPathForHref(file, root, href) {
  if (shouldSkipHref(href)) return "";

  var parts = splitHref(href);
  var base = parts.base;
  if (!base || base === "." || base === "..") return "";

  var resolved = path.resolve(path.dirname(file), base);
  var ext = path.extname(base);

  if (/\.md$/i.test(base)) {
    var htmlBase = markdownToOutputPath(base);
    resolved = path.resolve(path.dirname(file), htmlBase);
  } else if (!ext || /\/$/i.test(base)) {
    resolved = path.resolve(resolved, "index.html");
  }

  return path.relative(root, resolved).replace(/\\/g, "/");
}

function normalizeHref(file, root, href) {
  if (shouldSkipHref(href)) return href;

  var parts = splitHref(href);
  var base = parts.base;
  if (!base || base === "." || base === "..") return href;

  if (/\.md$/i.test(base)) {
    return markdownToOutputPath(base) + parts.suffix;
  }

  if (path.extname(base) || /\/$/i.test(base)) return href;

  var resolved = path.resolve(path.dirname(file), base);
  if (fs.existsSync(path.join(resolved, "index.html"))) {
    return base + "/" + parts.suffix;
  }

  return href;
}

function titleForHref(file, root, href, fallback) {
  var outputPath = relativeOutputPathForHref(file, root, href);
  var title = outputPath ? getOutputTitleMap()[outputPath] : "";
  return title || fallbackTitleFromFilename(fallback);
}

function cleanGeneratedLinks(html, file, root) {
  var withNormalizedHrefs = html.replace(/\bhref="([^"]+)"/g, function(match, href) {
    var normalized = normalizeHref(file, root, href);
    if (normalized === href) return match;
    return 'href="' + escapeHtml(normalized) + '"';
  });

  return withNormalizedHrefs.replace(/<a\b([^>]*)>([^<]*\.md)<\/a>/g, function(match, attrs, label) {
    var hrefMatch = attrs.match(/\bhref="([^"]+)"/);
    if (!hrefMatch) return match;

    var title = titleForHref(file, root, hrefMatch[1], label);
    return "<a" + attrs + ">" + escapeHtml(title) + "</a>";
  });
}

function renderFaviconLinks(file, root) {
  var href = relativeOutputRoot(file, root).replace(/\/$/, "") +
    "/gitbook/honkit-plugin-liberation/liberation-logo.png";

  return [
    '<link rel="icon" href="' + escapeHtml(href) + '" type="image/png">',
    '<link rel="shortcut icon" href="' + escapeHtml(href) + '" type="image/png">',
    '<link rel="apple-touch-icon" href="' + escapeHtml(href) + '" type="image/png">'
  ].join("\n    ");
}

function cleanGeneratedHtml(context) {
  if (!context.output || context.output.name !== "website") return;

  var root = context.output.root();
  walkHtmlFiles(root).forEach(function(file) {
    var html = fs.readFileSync(file, "utf8");
    var next = html.replace(/<title>([\s\S]*?)<\/title>/, function(match, title) {
      return "<title>" + escapeHtml(cleanHtmlTitle(title)) + "</title>";
    });

    next = next
      .replace(/\s*<link rel="apple-touch-icon-precomposed"[^>]*>\n?/g, "\n")
      .replace(/\s*<link rel="shortcut icon"[^>]*>\n?/g, "\n")
      .replace(/<\/head>/, "    " + renderFaviconLinks(file, root) + "\n</head>");

    next = cleanGeneratedLinks(next, file, root);

    if (next !== html) {
      fs.writeFileSync(file, next);
    }
  });
}

function writeDefaultLanguageIndex(context) {
  if (!context.output || context.output.name !== "website") return;

  var root = context.output.root();
  var defaultLanguageRoot = getDefaultLanguageRoot();
  if (!defaultLanguageRoot) return;

  var href = defaultLanguageRoot.replace(/\/+$/, "") + "/";
  var indexPath = path.join(root, "index.html");
  if (!fs.existsSync(path.join(root, defaultLanguageRoot, "index.html"))) return;

  fs.writeFileSync(indexPath, [
    "<!doctype html>",
    '<html lang="en">',
    "<head>",
    '<meta charset="utf-8">',
    '<meta name="viewport" content="width=device-width, initial-scale=1">',
    '<meta http-equiv="refresh" content="0; url=' + escapeHtml(href) + '">',
    '<title>Liberation User Manual</title>',
    '<script>window.location.replace(' + escapeJsonForScript(href) + ');</script>',
    "</head>",
    "<body>",
    '<p><a href="' + escapeHtml(href) + '">Open the English manual</a></p>',
    "</body>",
    "</html>"
  ].join("\n"));
}

function renderRedirectPage(href, title) {
  var escapedHref = escapeHtml(href);
  var escapedTitle = escapeHtml(title || "Liberation User Manual");

  return [
    "<!doctype html>",
    '<html lang="en">',
    "<head>",
    '<meta charset="utf-8">',
    '<meta name="viewport" content="width=device-width, initial-scale=1">',
    '<meta name="robots" content="noindex">',
    '<meta http-equiv="refresh" content="0; url=' + escapedHref + '">',
    '<link rel="canonical" href="' + escapedHref + '">',
    "<title>" + escapedTitle + "</title>",
    "<script>",
    "var target = " + escapeJsonForScript(href) + " + window.location.search + window.location.hash;",
    "window.location.replace(target);",
    "</script>",
    "</head>",
    "<body>",
    '<p><a href="' + escapedHref + '">' + escapedTitle + "</a></p>",
    "</body>",
    "</html>"
  ].join("\n");
}

function writeLegacyEnglishRedirects(context) {
  if (!context.output || context.output.name !== "website") return;

  var root = context.output.root();
  var defaultLanguageRoot = getDefaultLanguageRoot();
  if (!defaultLanguageRoot) return;

  var languageOutputRoot = path.join(root, defaultLanguageRoot);
  if (!fs.existsSync(languageOutputRoot)) return;

  walkHtmlFiles(languageOutputRoot).forEach(function(file) {
    var rel = path.relative(languageOutputRoot, file).replace(/\\/g, "/");
    if (!rel || rel === "index.html") return;

    var legacyPath = path.join(root, rel);
    var href = path.relative(path.dirname(legacyPath), file).replace(/\\/g, "/") || "index.html";
    var title = getOutputTitleMap()[posixPath.join(defaultLanguageRoot, rel)] || "Liberation User Manual";

    fs.mkdirSync(path.dirname(legacyPath), { recursive: true });
    fs.writeFileSync(legacyPath, renderRedirectPage(href, title));
  });
}

function copyDefaultLanguageAssets(context) {
  if (!context.output || context.output.name !== "website") return;

  var root = context.output.root();
  var defaultLanguageRoot = getDefaultLanguageRoot();
  if (!defaultLanguageRoot) return;

  var defaultGitbookAssets = path.join(root, defaultLanguageRoot, ".gitbook");
  if (!fs.existsSync(defaultGitbookAssets)) return;

  getLanguageRoots().forEach(function(languageRoot) {
    if (!languageRoot || languageRoot === defaultLanguageRoot) return;
    copyMissingDirectory(defaultGitbookAssets, path.join(root, languageRoot, ".gitbook"));
  });
}

function injectPageDescription(content, description) {
  if (!description || /class="lib-page-description"/.test(content)) return content;

  var descriptionHtml = '<p class="lib-page-description">' + escapeHtml(description) + "</p>";
  if (/<h1\b[^>]*>[\s\S]*?<\/h1>/i.test(content)) {
    return content.replace(/(<h1\b[^>]*>[\s\S]*?<\/h1>)/i, "$1" + descriptionHtml);
  }

  return descriptionHtml + content;
}

function renderChildPages(sourcePath, languageRoot) {
  var node = getSummary(languageRoot).nodesByPath[normalizeDocPath(sourcePath)];
  if (!node || !node.children || node.children.length === 0) return "";

  var links = node.children.map(function(child) {
    var label = splitStatusTitle(child.title);
    return [
      '<a class="lib-child-page" href="' + escapeHtml(relativeHref(sourcePath, child.path)) + '">',
      label.icon ? '<span class="lib-child-page-icon" aria-hidden="true">' + escapeHtml(label.icon) + "</span>" : "",
      '<span class="lib-child-page-title">' + escapeHtml(label.title) + "</span>",
      '<span class="lib-child-page-arrow" aria-hidden="true">›</span>',
      "</a>"
    ].join("");
  }).join("");

  return '<nav class="lib-child-pages" aria-label="Pages in this section">' + links + "</nav>";
}

module.exports = {
  book: {
    assets: "./assets",
    css: ["liberation.css"],
    js: ["liberation.js"]
  },

  blocks: {
    hint: {
      process: function(block) {
        var requestedStyle = block.kwargs.style || "info";
        var style = STYLE_ALIASES[requestedStyle] || "info";
        var label = STYLE_LABELS[style] || STYLE_LABELS.info;
        var icon = STYLE_ICONS[style] || STYLE_ICONS.info;

        return this.renderBlock("markdown", block.body).then(function(renderedBody) {
          return [
            '<aside class="callout callout-' + style + '" data-callout="' + style + '">',
            '<div class="callout-icon" aria-hidden="true">' + icon + "</div>",
            '<div class="callout-body">',
            '<span class="callout-label">' + label + "</span>",
            renderedBody,
            "</div>",
            "</aside>"
          ].join("");
        });
      }
    },
    embed: {
      process: function(block) {
        return renderEmbed(block.kwargs.url || block.body);
      }
    }
  },

  hooks: {
    page: function(page) {
      var config = getPluginConfig(this);
      var repo = getConfigValue(config, "repo", "");
      var branch = getBranch(config);
      var languageRoot = getLanguageRoot(this.config);
      var sourcePath = page.path || "";
      var repoPath = sourcePathForRepo(languageRoot, sourcePath);
      var title = cleanTitle(page.title || "");
      var metadata = {
        sourcePath: repoPath,
        editUrl: buildEditUrl(repo, branch, repoPath),
        lastUpdated: getLastUpdated(repoPath) || (languageRoot === "en-GB" ? getLastUpdated(sourcePath) : ""),
        title: title,
        currentLanguage: languageRoot,
        defaultLanguage: getDefaultLanguageRoot(),
        languages: languageTargets(sourcePath)
      };

      page.title = title;

      var pageMeta = '<script type="application/json" id="liberation-page-meta">' +
        escapeJsonForScript(metadata) +
        "</script>";

      page.content = '<div data-pagefind-body class="lib-page-content">' +
        injectPageDescription(page.content, page.description) +
        renderChildPages(sourcePath, languageRoot) +
        "</div>" +
        pageMeta;

      return page;
    },

    finish: function() {
      cleanGeneratedHtml(this);
      copyDefaultLanguageAssets(this);
      writeDefaultLanguageIndex(this);
      writeLegacyEnglishRedirects(this);
    }
  }
};
