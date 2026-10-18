(() => {
  const tabs = [...document.querySelectorAll('[role="tab"]')];
  const reader = document.getElementById('verse-reader');
  const pdf = 'https://hajime.online/download/KATAKAMUNAUTAI80SHU.pdf';
  function activate(id, focus = false) {
    const selected = tabs.find(tab => tab.id === 'tab-' + id) || tabs[0];
    tabs.forEach(tab => {
      const active = tab === selected;
      tab.setAttribute('aria-selected', String(active));
      tab.tabIndex = active ? 0 : -1;
      document.getElementById(tab.getAttribute('aria-controls')).hidden = !active;
    });
    document.querySelector('.highlight-control').hidden = selected.id !== 'tab-kana';
    if (selected.id === 'tab-katakamuna' && !reader.hasAttribute('src')) reader.src = reader.dataset.src;
    if (focus) selected.focus();
  }
  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => { activate(tab.dataset.panel); history.replaceState(null, '', '#' + tab.dataset.panel); });
    tab.addEventListener('keydown', event => {
      let next;
      if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
      if (event.key === 'ArrowLeft') next = (index + tabs.length - 1) % tabs.length;
      if (event.key === 'Home') next = 0;
      if (event.key === 'End') next = tabs.length - 1;
      if (next !== undefined) { event.preventDefault(); tabs[next].click(); tabs[next].focus(); }
    });
  });
  document.querySelectorAll('[data-verse]').forEach(button => button.addEventListener('click', () => {
    const n = Number(button.dataset.verse);
    document.querySelectorAll('[data-verse]').forEach(item => item.setAttribute('aria-pressed', String(item === button)));
    document.getElementById('verse-title').textContent = `Utahi ${String(n).padStart(2, '0')} of 80`;
    const url = `${pdf}#page=${n}`;
    reader.src = url;
    reader.title = `Katakamuna utahi source PDF, verse ${n}`;
    document.getElementById('verse-open').href = url;
  }));
  window.addEventListener('hashchange', () => activate(location.hash.slice(1)));
  activate(location.hash.slice(1));
})();
