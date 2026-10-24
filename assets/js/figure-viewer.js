/* Progressive enhancement: original figure links work without JavaScript. */
(() => {
  const dialog = document.querySelector('.figure-dialog');
  if (!dialog || typeof dialog.showModal !== 'function') return;
  const image = dialog.querySelector('img');
  const stage = dialog.querySelector('.figure-stage');
  const zoom = dialog.querySelector('.figure-zoom');
  let trigger;

  function setZoom(enabled) {
    stage.classList.toggle('is-zoomed', enabled);
    zoom.setAttribute('aria-pressed', String(enabled));
    zoom.textContent = enabled ? 'Fit to screen' : 'Zoom to 100%';
    stage.scrollTo(0, 0);
  }

  document.querySelectorAll('.research-figure a').forEach(link => {
    link.setAttribute('aria-haspopup', 'dialog');
    link.addEventListener('click', event => {
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey || event.button !== 0) return;
      event.preventDefault();
      trigger = link;
      const source = link.closest('figure').querySelector('img');
      image.src = source.src;
      image.alt = source.alt;
      dialog.querySelector('h2').textContent = link.closest('article').querySelector('.project-name').textContent;
      setZoom(false);
      dialog.showModal();
      document.body.classList.add('figure-open');
    });
  });
  zoom.addEventListener('click', () => setZoom(zoom.getAttribute('aria-pressed') !== 'true'));
  dialog.querySelector('.figure-close').addEventListener('click', () => dialog.close());
  dialog.addEventListener('close', () => {
    document.body.classList.remove('figure-open');
    setZoom(false);
    trigger?.focus({ preventScroll: true });
  });
})();
