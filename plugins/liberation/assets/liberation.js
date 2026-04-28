(function() {
  var pagefindModule = null;
  var pagefindLoading = null;
  var searchTimer = null;
  var searchRun = 0;
  var searchOpenedFromQuery = false;

  function currentScriptBase() {
    var scripts = document.getElementsByTagName("script");
    for (var i = scripts.length - 1; i >= 0; i -= 1) {
      var src = scripts[i].src || "";
      var marker = "/gitbook/honkit-plugin-liberation/liberation.js";
      var index = src.indexOf(marker);
      if (index !== -1) return src.slice(0, index);
    }
    return "";
  }

  function rootPath() {
    return currentScriptBase() || ".";
  }

  function logoPath() {
    return rootPath() + "/gitbook/honkit-plugin-liberation/liberation-logo.png";
  }

  function siteBasePath(meta) {
    var language = meta && meta.currentLanguage;
    var pathname = window.location.pathname || "/";

    if (language) {
      var marker = "/" + language + "/";
      var index = pathname.indexOf(marker);
      if (index !== -1) return pathname.slice(0, index);

      marker = "/" + language;
      if (pathname.slice(-marker.length) === marker) {
        return pathname.slice(0, -marker.length);
      }
    }

    try {
      var scriptBase = new URL(rootPath(), window.location.href);
      return scriptBase.pathname.replace(/\/$/, "");
    } catch (error) {
      return "";
    }
  }

  function siteUrl(path, meta) {
    var base = siteBasePath(meta).replace(/\/$/, "");
    path = String(path || "").replace(/^\/+/, "");
    return path ? (base || "") + "/" + path : (base || "") + "/";
  }

  function iconSearch() {
    return '<span class="lib-search-icon" aria-hidden="true"></span>';
  }

  function escapeHtml(value) {
    return String(value || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function stripStatus(value) {
    return String(value || "").replace(/^[^\p{L}\p{N}\s]+(?:\uFE0F)?\s*/u, "");
  }

  function cleanDocumentTitle() {
    document.title = String(document.title || "")
      .replace(/\s*[·|]\s*/g, " | ")
      .split(" | ")
      .map(stripStatus)
      .filter(Boolean)
      .join(" | ");
  }

  function ensureFavicons() {
    var href = logoPath();
    Array.prototype.forEach.call(document.querySelectorAll('link[rel*="icon"]'), function(link) {
      link.parentNode.removeChild(link);
    });

    [
      { rel: "icon", type: "image/png", sizes: "32x32" },
      { rel: "shortcut icon", type: "image/png" },
      { rel: "apple-touch-icon", type: "image/png" }
    ].forEach(function(attrs) {
      var link = document.createElement("link");
      Object.keys(attrs).forEach(function(key) {
        link.setAttribute(key, attrs[key]);
      });
      link.href = href;
      document.head.appendChild(link);
    });
  }

  function stripStatusFromHtml(value) {
    return String(value || "").replace(/^[^\p{L}\p{N}<\s]+(?:\uFE0F)?\s*/u, "");
  }

  function titleCase(value) {
    return String(value || "")
      .replace(/[-_]+/g, " ")
      .replace(/\b\w/g, function(char) {
        return char.toUpperCase();
      });
  }

  function categoryFromUrl(url, fallbackTitle) {
    var categories = {
      "advanced": "Advanced",
      "appendix-articles": "Appendix - Articles",
      "clip-editor": "The Clip Editor",
      "clips": "Clips & Clip Deck",
      "dmx-control": "DMX / Artnet",
      "faq.html": "FAQ",
      "graphics-and-the-canvas-system": "Graphics and the Canvas System",
      "hardware": "Hardware",
      "installation": "Installation / Licensing",
      "midi-control": "MIDI Control",
      "output-view": "Output View / Zones",
      "reference": "Reference",
      "setting-up": "Setting Up",
      "timeline": "Timeline",
      "troubleshooting": "Troubleshooting"
    };

    try {
      var path = new URL(url, window.location.href).pathname.replace(/^\/+/, "");
      var first = path.split("/")[0] || "";
      if (categories[path]) return categories[path];
      if (categories[first]) return categories[first];
      if (!first || first === "index.html") return "Home";
      return titleCase(first.replace(/\.html$/, "")) || stripStatus(fallbackTitle);
    } catch (error) {
      return stripStatus(fallbackTitle);
    }
  }

  function isMobileNav() {
    return window.matchMedia("(max-width: 900px)").matches;
  }

  function setMobileSidebar(open) {
    var book = document.querySelector(".book");
    var button = document.querySelector(".lib-menu-button");

    if (!book) return;
    book.classList.toggle("lib-mobile-menu-open", !!open);
    document.body.classList.toggle("lib-mobile-menu-open", !!open);
    if (button) button.setAttribute("aria-expanded", open ? "true" : "false");
  }

  function normaliseMobileSidebar() {
    setMobileSidebar(false);
  }

  function updateLanguageSwitcher(header, meta) {
    var switcher = header.querySelector(".lib-language-switcher");
    if (!switcher || !meta || !Array.isArray(meta.languages) || meta.languages.length < 2) {
      if (switcher) switcher.hidden = true;
      return;
    }

    var select = switcher.querySelector(".lib-language-select");
    select.innerHTML = meta.languages.map(function(language) {
      var selected = language.id === meta.currentLanguage ? " selected" : "";
      return '<option value="' + escapeHtml(siteUrl(language.targetPath, meta)) + '"' + selected + ">" +
        escapeHtml(language.title) +
        "</option>";
    }).join("");

    switcher.hidden = false;
  }

  function ensureHeader() {
    var existingHeader = document.querySelector(".lib-site-header");
    var meta = parseMeta();
    if (existingHeader) {
      updateLanguageSwitcher(existingHeader, meta);
      return;
    }

    var header = document.createElement("header");
    header.className = "lib-site-header";
    header.innerHTML = [
      '<button class="lib-menu-button" type="button" aria-label="Toggle navigation" aria-expanded="false">',
      '<span class="lib-menu-icon" aria-hidden="true"></span>',
      "</button>",
      '<a class="lib-brand" href="' + rootPath() + '/">',
      '<img class="lib-brand-logo" src="' + logoPath() + '" alt="" width="32" height="32">',
      '<span>Liberation User Manual</span>',
      "</a>",
      '<div class="lib-header-spacer"></div>',
      '<label class="lib-language-switcher" hidden>',
      '<span class="lib-language-label">Language</span>',
      '<select class="lib-language-select" aria-label="Language"></select>',
      "</label>",
      '<button class="lib-search-button" type="button">',
      iconSearch(),
      '<span class="lib-search-label">Search...</span>',
      '<span class="lib-search-kbd">Ctrl K</span>',
      "</button>"
    ].join("");

    document.body.insertBefore(header, document.body.firstChild);

    header.querySelector(".lib-menu-button").addEventListener("click", function() {
      if (isMobileNav()) {
        var currentBook = document.querySelector(".book");
        setMobileSidebar(!(currentBook && currentBook.classList.contains("lib-mobile-menu-open")));
        return;
      }

      if (window.gitbook && window.gitbook.sidebar) {
        window.gitbook.sidebar.toggle();
        return;
      }
      var book = document.querySelector(".book");
      if (book) book.classList.toggle("with-summary");
    });

    header.querySelector(".lib-search-button").addEventListener("click", openSearch);
    header.querySelector(".lib-language-select").addEventListener("change", function(event) {
      if (event.target.value) window.location.href = event.target.value;
    });
    updateLanguageSwitcher(header, meta);

    var summary = document.querySelector(".book-summary");
    if (summary) {
      summary.addEventListener("click", function(event) {
        if (event.target.closest("a") && isMobileNav()) setMobileSidebar(false);
      });
    }
  }

  function ensureSearchOverlay() {
    var overlay = document.querySelector(".lib-search-overlay");
    if (overlay) return overlay;

    overlay = document.createElement("div");
    overlay.className = "lib-search-overlay";
    overlay.innerHTML = [
      '<div class="lib-search-dialog" role="dialog" aria-modal="false" aria-label="Search documentation">',
      '<form class="lib-search-form" role="search" action="javascript:void(0);">',
      '<span class="lib-search-panel-icon" aria-hidden="true"></span>',
      '<input class="lib-search-input" type="search" placeholder="Search..." autocomplete="off" autocapitalize="none" spellcheck="false">',
      '<button class="lib-search-close" type="button" aria-label="Close search">ESC</button>',
      "</form>",
      '<div id="liberation-search-results" class="lib-search-results"><div class="lib-search-status">Loading search index...</div></div>',
      "</div>"
    ].join("");

    document.body.appendChild(overlay);

    overlay.addEventListener("click", function(event) {
      if (event.target === overlay) closeSearch();
    });
    overlay.querySelector(".lib-search-close").addEventListener("click", closeSearch);
    overlay.querySelector(".lib-search-form").addEventListener("submit", function(event) {
      event.preventDefault();
    });
    overlay.querySelector(".lib-search-input").addEventListener("input", function(event) {
      scheduleSearch(event.target.value);
    });

    return overlay;
  }

  function loadPagefind() {
    if (pagefindModule) return Promise.resolve(pagefindModule);
    if (pagefindLoading) return pagefindLoading;

    pagefindLoading = import(rootPath() + "/pagefind/pagefind.js")
      .then(function(module) {
        pagefindModule = module;
        return module.options({
          basePath: rootPath() + "/pagefind/",
          excerptLength: 18
        }).then(function() {
          return module;
        });
      })
      .catch(function(error) {
        var target = document.getElementById("liberation-search-results");
        if (target) {
          target.innerHTML = '<div class="lib-search-status">Search index not found. Run <code>npm run build:site</code> before previewing the static site.</div>';
        }
        throw error;
      });

    return pagefindLoading;
  }

  function openSearch() {
    var overlay = ensureSearchOverlay();
    var input = overlay.querySelector(".lib-search-input");
    var params = new URLSearchParams(window.location.search);
    var initialQuery = params.get("q");

    overlay.classList.add("open");
    document.body.classList.add("lib-search-open");
    if (initialQuery && !input.value) {
      input.value = initialQuery;
    }
    loadPagefind().then(function() {
      if (input.value) performSearch(input.value);
      else renderSearchIntro();
    });
    focusSearch();
  }

  function closeSearch() {
    var overlay = document.querySelector(".lib-search-overlay");
    if (overlay) overlay.classList.remove("open");
    document.body.classList.remove("lib-search-open");
  }

  function focusSearch() {
    window.setTimeout(function() {
      var input = document.querySelector(".lib-search-input");
      if (input) input.focus();
    }, 80);
  }

  function scheduleSearch(term) {
    clearTimeout(searchTimer);
    searchTimer = window.setTimeout(function() {
      performSearch(term);
    }, 140);
  }

  function renderSearchIntro() {
    var target = document.getElementById("liberation-search-results");
    if (target) {
      target.innerHTML = '<div class="lib-search-status">Start typing to search the manual.</div>';
    }
  }

  function updateSearchUrl(query) {
    if (!window.history || !window.history.replaceState) return;
    var url = new URL(window.location.href);
    if (query) {
      url.searchParams.set("q", query);
    } else {
      url.searchParams.delete("q");
    }
    window.history.replaceState(null, "", url.pathname + url.search + url.hash);
  }

  function renderSearchResult(data, index) {
    var title = stripStatus((data.meta && data.meta.title) || data.url);
    var category = categoryFromUrl(data.url, title);
    var subResults = (data.sub_results || []).slice(0, 2);
    var resultHref = data.url || "#";
    var html = [
      '<article class="lib-search-result' + (index === 0 ? " is-active" : "") + '">',
      '<a class="lib-search-result-main" href="' + escapeHtml(resultHref) + '">',
      '<span class="lib-search-result-icon" aria-hidden="true"></span>',
      '<span class="lib-search-result-copy">',
      '<span class="lib-search-result-section">' + escapeHtml(category) + "</span>",
      '<span class="lib-search-result-title">' + escapeHtml(title) + "</span>",
      "</span>",
      '<span class="lib-search-result-arrow" aria-hidden="true">›</span>',
      "</a>"
    ];

    if (subResults.length) {
      html.push('<div class="lib-search-subresults">');
      subResults.forEach(function(subResult) {
        html.push(
          '<a class="lib-search-subresult" href="' + escapeHtml(subResult.url || resultHref) + '">',
          '<span class="lib-search-subresult-copy">',
          '<span class="lib-search-subresult-title">' + escapeHtml(stripStatus(subResult.title)) + "</span>",
          '<span class="lib-search-subresult-excerpt">' + stripStatusFromHtml(subResult.excerpt || "") + "</span>",
          "</span>",
          '<span class="lib-search-result-arrow" aria-hidden="true">›</span>',
          "</a>"
        );
      });
      html.push("</div>");
    } else if (data.excerpt) {
      html.push(
        '<a class="lib-search-subresult" href="' + escapeHtml(resultHref) + '">',
        '<span class="lib-search-subresult-copy">',
        '<span class="lib-search-subresult-excerpt">' + stripStatusFromHtml(data.excerpt) + "</span>",
        "</span>",
        '<span class="lib-search-result-arrow" aria-hidden="true">›</span>',
        "</a>"
      );
    }

    html.push("</article>");
    return html.join("");
  }

  function renderSearchResults(term, results) {
    var target = document.getElementById("liberation-search-results");
    if (!target) return;

    if (!term) {
      renderSearchIntro();
      return;
    }

    if (!results.length) {
      target.innerHTML = '<div class="lib-search-status">No results for <strong>' + escapeHtml(term) + "</strong>.</div>";
      return;
    }

    target.innerHTML = [
      '<div class="lib-search-count">' + results.length + " result" + (results.length === 1 ? "" : "s") + ' for <strong>' + escapeHtml(term) + "</strong></div>",
      '<div class="lib-search-result-list">',
      results.map(renderSearchResult).join(""),
      "</div>"
    ].join("");
  }

  function performSearch(term) {
    var query = String(term || "").trim();
    var target = document.getElementById("liberation-search-results");
    var run = ++searchRun;

    updateSearchUrl(query);

    if (!query) {
      renderSearchIntro();
      return;
    }

    if (target) target.innerHTML = '<div class="lib-search-status">Searching for <strong>' + escapeHtml(query) + "</strong>...</div>";

    loadPagefind()
      .then(function(module) {
        return module.search(query);
      })
      .then(function(search) {
        return Promise.all(search.results.slice(0, 7).map(function(result) {
          return result.data();
        }));
      })
      .then(function(results) {
        if (run === searchRun) renderSearchResults(query, results);
      })
      .catch(function() {
        if (target) {
          target.innerHTML = '<div class="lib-search-status">Search failed. Rebuild with <code>npm run build:site</code> and try again.</div>';
        }
      });
  }

  function parseMeta() {
    var node = document.getElementById("liberation-page-meta");
    if (!node) return {};
    try {
      return JSON.parse(node.textContent || "{}");
    } catch (error) {
      return {};
    }
  }

  function formatDate(value) {
    if (!value) return "";
    var date = new Date(value);
    if (Number.isNaN(date.getTime())) return "";
    return date.toLocaleDateString(undefined, {
      year: "numeric",
      month: "short",
      day: "numeric"
    });
  }

  function ensureId(heading, index) {
    if (heading.id) return heading.id;
    var base = heading.textContent
      .trim()
      .toLowerCase()
      .replace(/[^\w]+/g, "-")
      .replace(/^-+|-+$/g, "");
    heading.id = base || "section-" + index;
    return heading.id;
  }

  function enhancePageTools(meta) {
    var section = document.querySelector(".markdown-section");
    if (!section || section.querySelector(".lib-page-tools")) return;

    var tools = document.createElement("div");
    tools.className = "lib-page-tools";

    if (meta.editUrl) {
      var edit = document.createElement("a");
      edit.className = "lib-edit-link";
      edit.href = meta.editUrl;
      edit.target = "_blank";
      edit.rel = "noopener";
      edit.textContent = "Edit on GitHub";
      tools.appendChild(edit);
    }

    if (tools.children.length > 0) {
      section.insertBefore(tools, section.firstChild);
    }
  }

  function enhanceFooter(meta) {
    var section = document.querySelector(".markdown-section");
    if (!section || section.querySelector(".lib-page-footer")) return;

    var footer = document.createElement("div");
    footer.className = "lib-page-footer";

    var updated = document.createElement("div");
    updated.className = "lib-updated";
    var formattedDate = formatDate(meta.lastUpdated);
    updated.textContent = formattedDate ? "Last updated " + formattedDate : "Last updated from Git history";
    footer.appendChild(updated);

    section.appendChild(footer);
  }

  function enhanceToc() {
    var oldToc = document.querySelector(".lib-page-toc");
    if (oldToc) oldToc.remove();

    var section = document.querySelector(".markdown-section");
    if (!section) return;

    var headings = Array.prototype.slice.call(section.querySelectorAll("h2, h3"))
      .filter(function(heading) {
        return heading.textContent.trim().length > 0;
      });

    if (headings.length === 0) return;

    var toc = document.createElement("aside");
    toc.className = "lib-page-toc";
    toc.innerHTML = '<div class="lib-page-toc-title">On this page</div><nav class="lib-page-toc-list"></nav>';
    var list = toc.querySelector("nav");

    headings.forEach(function(heading, index) {
      var id = ensureId(heading, index);
      var link = document.createElement("a");
      link.href = "#" + id;
      link.textContent = heading.textContent.trim();
      link.dataset.depth = heading.tagName === "H3" ? "3" : "2";
      list.appendChild(link);
    });

    document.body.appendChild(toc);
  }

  function updateActiveTocLink() {
    var links = Array.prototype.slice.call(document.querySelectorAll(".lib-page-toc a"));
    if (links.length === 0) return;

    var active = links[0];
    links.forEach(function(link) {
      var target = document.getElementById(link.getAttribute("href").slice(1));
      if (target && target.getBoundingClientRect().top < 160) {
        active = link;
      }
      link.classList.remove("active");
    });
    active.classList.add("active");
  }

  function enhancePage() {
    cleanDocumentTitle();
    ensureFavicons();
    ensureHeader();
    normaliseMobileSidebar();
    if (!searchOpenedFromQuery && new URLSearchParams(window.location.search).get("q")) {
      searchOpenedFromQuery = true;
      openSearch();
    }
    var meta = parseMeta();
    enhancePageTools(meta);
    enhanceFooter(meta);
    enhanceToc();
    updateActiveTocLink();
  }

  document.addEventListener("keydown", function(event) {
    if (event.key === "Escape") {
      closeSearch();
      return;
    }

    var key = String(event.key || "").toLowerCase();
    if ((event.ctrlKey || event.metaKey) && key === "k") {
      event.preventDefault();
      openSearch();
    }
  });

  document.addEventListener("scroll", updateActiveTocLink, true);
  window.addEventListener("resize", function() {
    normaliseMobileSidebar();
    updateActiveTocLink();
  });

  if (window.gitbook && window.gitbook.events) {
    window.gitbook.events.on("page.change", function() {
      window.setTimeout(enhancePage, 0);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", enhancePage);
  } else {
    enhancePage();
  }
})();
