// One language at a time: ?lang=, then the last choice, then the browser's language.
// Without JavaScript every language is shown, one after another.
(function () {
  var root = document.documentElement;
  var langs = ['en', 'he', 'ru'];
  root.classList.add('js');

  function initial() {
    var q = null;
    try { q = new URLSearchParams(location.search).get('lang'); } catch (e) {}
    if (langs.indexOf(q) >= 0) return q;
    try {
      var saved = localStorage.getItem('lang');
      if (langs.indexOf(saved) >= 0) return saved;
    } catch (e) {}
    var n = ((navigator.languages && navigator.languages[0]) || navigator.language || 'en').toLowerCase();
    if (n.indexOf('he') === 0 || n.indexOf('iw') === 0) return 'he';
    if (n.indexOf('ru') === 0) return 'ru';
    return 'en';
  }

  function show(lang) {
    root.lang = lang;
    root.dir = lang === 'he' ? 'rtl' : 'ltr';
    var sections = document.querySelectorAll('main section[lang]');
    for (var i = 0; i < sections.length; i++) {
      var s = sections[i];
      s.hidden = s.getAttribute('lang') !== lang;
      if (!s.hidden && s.getAttribute('data-title')) document.title = s.getAttribute('data-title');
    }
    var texts = document.querySelectorAll('[data-' + lang + ']');
    for (var j = 0; j < texts.length; j++) texts[j].textContent = texts[j].getAttribute('data-' + lang);
    var buttons = document.querySelectorAll('.langs button');
    for (var k = 0; k < buttons.length; k++) {
      buttons[k].setAttribute('aria-pressed', buttons[k].getAttribute('data-lang') === lang ? 'true' : 'false');
    }
    // the other pages open in the same language
    var links = document.querySelectorAll('a[data-page]');
    for (var m = 0; m < links.length; m++) {
      links[m].setAttribute('href', links[m].getAttribute('data-page') + '?lang=' + lang);
    }
  }

  function choose(lang) {
    try { localStorage.setItem('lang', lang); } catch (e) {}
    try { history.replaceState(null, '', location.pathname + '?lang=' + lang + location.hash); } catch (e) {}
    show(lang);
  }

  function start() {
    show(initial());
    var buttons = document.querySelectorAll('.langs button');
    for (var i = 0; i < buttons.length; i++) {
      buttons[i].addEventListener('click', function () { choose(this.getAttribute('data-lang')); });
    }
  }

  // loaded at the end of <body>, after the footer: everything it touches is already there
  if (document.querySelector('footer')) start();
  else document.addEventListener('DOMContentLoaded', start);
})();
