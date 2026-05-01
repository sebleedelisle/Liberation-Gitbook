(function() {
  var pagefindModule = null;
  var pagefindLoading = null;
  var searchTimer = null;
  var searchRun = 0;
  var searchOpenedFromQuery = false;
  var languageStorageKey = "liberation.manual.language";
  var uiLabels = {
    suggestEdit: {
      "en-GB": "Suggest edit",
      "zh-CN": "建议修改",
      "de-DE": "Änderung vorschlagen",
      "nl-NL": "Wijziging voorstellen",
      "fr-FR": "Suggérer une modification",
      "es-ES": "Sugerir una edición",
      "da-DK": "Foreslå ændring",
      "nb-NO": "Foreslå endring",
      "sv-SE": "Föreslå ändring",
      "ja-JP": "編集を提案",
      "is-IS": "Leggja til breytingu",
      "fi-FI": "Ehdota muokkausta",
      "hu-HU": "Javasolj módosítást",
      "it-IT": "Suggerisci modifica",
      "pl-PL": "Zaproponuj zmianę",
      "pt-BR": "Sugerir edição",
      "ko-KR": "수정 제안",
      "zh-HK": "建議修改",
      "vi-VN": "Đề xuất chỉnh sửa",
      "tr-TR": "Düzenleme öner",
      "cs-CZ": "Navrhnout úpravu",
      "hr-HR": "Predloži izmjenu",
      "ru-RU": "Предложить правку",
      "ar": "اقتراح تعديل",
      "zh-TW": "建議修改"
    },
    selectTextFirst: {
      "en-GB": "Select text to suggest an edit.",
      "zh-CN": "请选择要建议修改的文字。",
      "de-DE": "Wähle Text für den Änderungsvorschlag aus.",
      "nl-NL": "Selecteer tekst om een wijziging voor te stellen.",
      "fr-FR": "Sélectionnez le texte à corriger.",
      "es-ES": "Selecciona el texto que quieres editar.",
      "da-DK": "Vælg tekst for at foreslå en ændring.",
      "nb-NO": "Velg tekst for å foreslå en endring.",
      "sv-SE": "Markera text för att föreslå en ändring.",
      "ja-JP": "修正を提案するテキストを選択してください。",
      "is-IS": "Veldu texta til að leggja til breytingu.",
      "fi-FI": "Valitse teksti, johon ehdotat muutosta.",
      "hu-HU": "Jelöld ki a módosítandó szöveget.",
      "it-IT": "Seleziona il testo da modificare.",
      "pl-PL": "Zaznacz tekst, którego dotyczy zmiana.",
      "pt-BR": "Selecione o texto que deseja corrigir.",
      "ko-KR": "수정을 제안할 텍스트를 선택하세요.",
      "zh-HK": "請選取要建議修改的文字。",
      "vi-VN": "Chọn văn bản bạn muốn đề xuất sửa.",
      "tr-TR": "Düzenleme önermek için metin seçin.",
      "cs-CZ": "Vyberte text, který chcete upravit.",
      "hr-HR": "Odaberite tekst za predloženu izmjenu.",
      "ru-RU": "Выделите текст для правки.",
      "ar": "حدّد النص الذي تريد اقتراح تعديله.",
      "zh-TW": "請選取要建議修改的文字。"
    },
    issueTitlePrefix: {
      "en-GB": "Suggested edit",
      "zh-CN": "修改建议",
      "de-DE": "Änderungsvorschlag",
      "nl-NL": "Voorgestelde wijziging",
      "fr-FR": "Modification suggérée",
      "es-ES": "Edición sugerida",
      "da-DK": "Foreslået ændring",
      "nb-NO": "Foreslått endring",
      "sv-SE": "Föreslagen ändring",
      "ja-JP": "修正提案",
      "is-IS": "Tillaga að breytingu",
      "fi-FI": "Ehdotettu muutos",
      "hu-HU": "Javasolt módosítás",
      "it-IT": "Modifica suggerita",
      "pl-PL": "Proponowana zmiana",
      "pt-BR": "Edição sugerida",
      "ko-KR": "수정 제안",
      "zh-HK": "修改建議",
      "vi-VN": "Đề xuất chỉnh sửa",
      "tr-TR": "Önerilen düzenleme",
      "cs-CZ": "Navržená úprava",
      "hr-HR": "Predložena izmjena",
      "ru-RU": "Предложенная правка",
      "ar": "اقتراح تعديل",
      "zh-TW": "修改建議"
    },
    issuePage: {
      "en-GB": "Page",
      "zh-CN": "页面",
      "de-DE": "Seite",
      "nl-NL": "Pagina",
      "fr-FR": "Page",
      "es-ES": "Página",
      "da-DK": "Side",
      "nb-NO": "Side",
      "sv-SE": "Sida",
      "ja-JP": "ページ",
      "is-IS": "Síða",
      "fi-FI": "Sivu",
      "hu-HU": "Oldal",
      "it-IT": "Pagina",
      "pl-PL": "Strona",
      "pt-BR": "Página",
      "ko-KR": "페이지",
      "zh-HK": "頁面",
      "vi-VN": "Trang",
      "tr-TR": "Sayfa",
      "cs-CZ": "Stránka",
      "hr-HR": "Stranica",
      "ru-RU": "Страница",
      "ar": "الصفحة",
      "zh-TW": "頁面"
    },
    issueTitle: {
      "en-GB": "Title",
      "zh-CN": "标题",
      "de-DE": "Titel",
      "nl-NL": "Titel",
      "fr-FR": "Titre",
      "es-ES": "Título",
      "da-DK": "Titel",
      "nb-NO": "Tittel",
      "sv-SE": "Titel",
      "ja-JP": "タイトル",
      "is-IS": "Titill",
      "fi-FI": "Otsikko",
      "hu-HU": "Cím",
      "it-IT": "Titolo",
      "pl-PL": "Tytuł",
      "pt-BR": "Título",
      "ko-KR": "제목",
      "zh-HK": "標題",
      "vi-VN": "Tiêu đề",
      "tr-TR": "Başlık",
      "cs-CZ": "Název",
      "hr-HR": "Naslov",
      "ru-RU": "Заголовок",
      "ar": "العنوان",
      "zh-TW": "標題"
    },
    issueManualUrl: {
      "en-GB": "Manual URL",
      "zh-CN": "手册链接",
      "de-DE": "Handbuch-URL",
      "nl-NL": "Handleiding-URL",
      "fr-FR": "URL du manuel",
      "es-ES": "URL del manual",
      "da-DK": "Manual-URL",
      "nb-NO": "Manual-URL",
      "sv-SE": "Manual-URL",
      "ja-JP": "マニュアルURL",
      "is-IS": "Slóð handbókar",
      "fi-FI": "Käyttöoppaan URL",
      "hu-HU": "Kézikönyv URL-je",
      "it-IT": "URL del manuale",
      "pl-PL": "Adres URL podręcznika",
      "pt-BR": "URL do manual",
      "ko-KR": "매뉴얼 URL",
      "zh-HK": "手冊連結",
      "vi-VN": "URL sổ tay",
      "tr-TR": "Kılavuz URL'si",
      "cs-CZ": "URL příručky",
      "hr-HR": "URL priručnika",
      "ru-RU": "URL руководства",
      "ar": "رابط الدليل",
      "zh-TW": "手冊連結"
    },
    issueSelectedText: {
      "en-GB": "Selected text",
      "zh-CN": "已选文字",
      "de-DE": "Ausgewählter Text",
      "nl-NL": "Geselecteerde tekst",
      "fr-FR": "Texte sélectionné",
      "es-ES": "Texto seleccionado",
      "da-DK": "Valgt tekst",
      "nb-NO": "Valgt tekst",
      "sv-SE": "Markerad text",
      "ja-JP": "選択したテキスト",
      "is-IS": "Valinn texti",
      "fi-FI": "Valittu teksti",
      "hu-HU": "Kijelölt szöveg",
      "it-IT": "Testo selezionato",
      "pl-PL": "Zaznaczony tekst",
      "pt-BR": "Texto selecionado",
      "ko-KR": "선택한 텍스트",
      "zh-HK": "已選文字",
      "vi-VN": "Văn bản đã chọn",
      "tr-TR": "Seçilen metin",
      "cs-CZ": "Vybraný text",
      "hr-HR": "Odabrani tekst",
      "ru-RU": "Выделенный текст",
      "ar": "النص المحدد",
      "zh-TW": "已選文字"
    },
    issueSuggestedChange: {
      "en-GB": "Suggested change",
      "zh-CN": "建议修改",
      "de-DE": "Vorgeschlagene Änderung",
      "nl-NL": "Voorgestelde wijziging",
      "fr-FR": "Modification suggérée",
      "es-ES": "Cambio sugerido",
      "da-DK": "Foreslået ændring",
      "nb-NO": "Foreslått endring",
      "sv-SE": "Föreslagen ändring",
      "ja-JP": "修正案",
      "is-IS": "Tillaga að breytingu",
      "fi-FI": "Ehdotettu muutos",
      "hu-HU": "Javasolt módosítás",
      "it-IT": "Modifica suggerita",
      "pl-PL": "Proponowana zmiana",
      "pt-BR": "Alteração sugerida",
      "ko-KR": "제안하는 수정",
      "zh-HK": "建議修改",
      "vi-VN": "Thay đổi đề xuất",
      "tr-TR": "Önerilen değişiklik",
      "cs-CZ": "Navržená změna",
      "hr-HR": "Predložena izmjena",
      "ru-RU": "Предлагаемое изменение",
      "ar": "التعديل المقترح",
      "zh-TW": "建議修改"
    },
    issuePlaceholder: {
      "en-GB": "Please describe the correction, or paste the replacement text.",
      "zh-CN": "请描述更正内容，或粘贴替换文字。",
      "de-DE": "Beschreibe die Korrektur oder füge den Ersatztext ein.",
      "nl-NL": "Beschrijf de correctie of plak de vervangende tekst.",
      "fr-FR": "Décrivez la correction ou collez le texte de remplacement.",
      "es-ES": "Describe la corrección o pega el texto de reemplazo.",
      "da-DK": "Beskriv rettelsen, eller indsæt erstatningsteksten.",
      "nb-NO": "Beskriv rettelsen, eller lim inn erstatningsteksten.",
      "sv-SE": "Beskriv rättningen eller klistra in ersättningstexten.",
      "ja-JP": "修正内容を説明するか、置き換えるテキストを貼り付けてください。",
      "is-IS": "Lýstu leiðréttingunni eða límdu inn nýjan texta.",
      "fi-FI": "Kuvaile korjaus tai liitä korvaava teksti.",
      "hu-HU": "Írd le a javítást, vagy illeszd be a helyettesítő szöveget.",
      "it-IT": "Descrivi la correzione oppure incolla il testo sostitutivo.",
      "pl-PL": "Opisz poprawkę albo wklej tekst zastępczy.",
      "pt-BR": "Descreva a correção ou cole o texto substituto.",
      "ko-KR": "수정 내용을 설명하거나 대체할 텍스트를 붙여 넣어 주세요.",
      "zh-HK": "請描述修正內容，或貼上替換文字。",
      "vi-VN": "Mô tả phần cần sửa hoặc dán văn bản thay thế.",
      "tr-TR": "Düzeltmeyi açıklayın veya yerine geçecek metni yapıştırın.",
      "cs-CZ": "Popište opravu nebo vložte náhradní text.",
      "hr-HR": "Opišite ispravak ili zalijepite zamjenski tekst.",
      "ru-RU": "Опишите исправление или вставьте текст для замены.",
      "ar": "صِف التصحيح أو الصق النص البديل.",
      "zh-TW": "請描述修正內容，或貼上替換文字。"
    }
  };

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

  function languageHomeUrl(meta) {
    var language = meta && (meta.currentLanguage || meta.defaultLanguage);
    if (!language) return siteUrl("", meta);
    return siteUrl(String(language).replace(/^\/+|\/+$/g, "") + "/", meta);
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

  function rememberLanguage(language) {
    if (!language) return;
    try {
      window.localStorage.setItem(languageStorageKey, language);
    } catch (error) {
      // Ignore storage failures in private browsing or locked-down environments.
    }
  }

  function uiText(key, meta) {
    var labels = uiLabels[key] || {};
    var language = meta && meta.currentLanguage;
    var base = String(language || "").split("-")[0];
    return labels[language] || labels[base] || labels["en-GB"] || "";
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
      return '<option value="' + escapeHtml(siteUrl(language.targetPath, meta)) + '"' +
        ' data-language-id="' + escapeHtml(language.id) + '"' + selected + ">" +
        escapeHtml(language.title) +
        "</option>";
    }).join("");

    switcher.hidden = false;
  }

  function updateBrandLink(header, meta) {
    var brand = header.querySelector(".lib-brand");
    if (brand) brand.href = languageHomeUrl(meta);
  }

  function ensureHeader() {
    var existingHeader = document.querySelector(".lib-site-header");
    var meta = parseMeta();
    if (existingHeader) {
      updateBrandLink(existingHeader, meta);
      updateLanguageSwitcher(existingHeader, meta);
      return;
    }

    var header = document.createElement("header");
    header.className = "lib-site-header";
    header.innerHTML = [
      '<button class="lib-menu-button" type="button" aria-label="Toggle navigation" aria-expanded="false">',
      '<span class="lib-menu-icon" aria-hidden="true"></span>',
      "</button>",
      '<a class="lib-brand" href="' + escapeHtml(languageHomeUrl(meta)) + '">',
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
    updateBrandLink(header, meta);

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
      var option = event.target.options[event.target.selectedIndex];
      if (option) rememberLanguage(option.getAttribute("data-language-id"));
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

    if (meta.suggestIssueBaseUrl || meta.suggestIssueUrl || meta.editUrl) {
      var edit = document.createElement("a");
      var hint = document.createElement("div");
      var editLabel = uiText("suggestEdit", meta);
      var suggestUrl = meta.suggestIssueBaseUrl || meta.suggestIssueUrl || meta.editUrl;
      edit.className = "lib-edit-link";
      edit.href = resolveSuggestUrl(suggestUrl, meta);
      edit.target = "_blank";
      edit.rel = "noopener";
      edit.textContent = editLabel;
      hint.className = "lib-edit-hint";
      hint.setAttribute("role", "status");
      hint.textContent = uiText("selectTextFirst", meta);
      prepareSuggestLinkOnOpen(edit, suggestUrl, hint, meta);
      tools.appendChild(edit);
      tools.appendChild(hint);
    }

    if (tools.children.length > 0) {
      section.insertBefore(tools, section.firstChild);
    }
  }

  function resolveSuggestUrl(url, meta) {
    if (meta && meta.suggestIssueBaseUrl) {
      return buildSuggestIssueUrl(meta.suggestIssueBaseUrl, meta);
    }

    return String(url || "")
      .replace(/&amp;/g, "&")
      .replace("%7B%7BPAGE_URL%7D%7D", encodeURIComponent(window.location.href))
      .replace("%7B%7BSELECTED_TEXT%7D%7D", encodeURIComponent(formatSelectedText(meta)));
  }

  function buildSuggestIssueUrl(baseUrl, meta) {
    var sourcePath = meta.sourcePath || "";
    var body = [
      uiText("issuePage", meta) + ": `" + sourcePath + "`",
      meta.title ? uiText("issueTitle", meta) + ": " + meta.title : "",
      uiText("issueManualUrl", meta) + ": " + window.location.href,
      "",
      formatSelectedText(meta),
      uiText("issueSuggestedChange", meta) + ":",
      "",
      "<!-- " + uiText("issuePlaceholder", meta) + " -->"
    ].filter(Boolean).join("\n");

    return String(baseUrl || "").replace(/&amp;/g, "&") +
      "?title=" + encodeURIComponent(uiText("issueTitlePrefix", meta) + ": " + sourcePath) +
      "&body=" + encodeURIComponent(body);
  }

  function prepareSuggestLinkOnOpen(link, url, hint, meta) {
    var preparedAt = 0;
    var hintTimer = 0;

    function prepare() {
      link.href = resolveSuggestUrl(url, meta);
      preparedAt = Date.now();
    }

    function showHint() {
      if (!hint) return;
      hint.classList.add("is-visible");
      window.clearTimeout(hintTimer);
      hintTimer = window.setTimeout(function() {
        hint.classList.remove("is-visible");
      }, 4200);
    }

    function hasSelection() {
      return selectedText().length > 0;
    }

    link.addEventListener("pointerdown", function(event) {
      if (!hasSelection()) return;
      prepare(event);
    });
    link.addEventListener("keydown", function(event) {
      if ((event.key === "Enter" || event.key === " ") && hasSelection()) prepare();
    });
    link.addEventListener("click", function(event) {
      if (!hasSelection()) {
        event.preventDefault();
        showHint();
        return;
      }
      if (Date.now() - preparedAt > 500) prepare();
    });
  }

  function selectedText() {
    var selection = window.getSelection ? String(window.getSelection()) : "";
    return selection.replace(/\s+\n/g, "\n").replace(/\n\s+/g, "\n").trim();
  }

  function formatSelectedText(meta) {
    var selection = selectedText();
    if (!selection) return "";

    return [
      uiText("issueSelectedText", meta) + ":",
      "",
      selection.split(/\r?\n/).map(function(line) {
        return "> " + line;
      }).join("\n"),
      ""
    ].join("\n");
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
