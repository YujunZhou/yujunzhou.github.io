/* Keep the existing visitor counter, but never count local development visits. */
(() => {
  if (window.location.hostname !== 'yujunzhou.github.io') return;
  const mount = document.querySelector('[data-visitor-map]');
  if (!mount || document.getElementById('mapmyvisitors')) return;
  const script = document.createElement('script');
  script.id = 'mapmyvisitors';
  script.async = true;
  script.src = 'https://mapmyvisitors.com/map.js?d=23pIdJVhMjN_8WNUnKTi-FQTV-hOMyUeuluWO9V4xPc&cl=ffffff&w=180';
  mount.hidden = false;
  script.addEventListener('error', () => { mount.hidden = true; });
  mount.append(script);
})();
