/* Count production visits without displaying a map; the footer links to statistics. */
(() => {
  if (window.location.hostname !== 'yujunzhou.github.io') return;
  const mount = document.querySelector('[data-visitor-map]');
  if (!mount || document.getElementById('mapmyvisitors')) return;
  const script = document.createElement('script');
  script.id = 'mapmyvisitors';
  script.async = true;
  script.src = 'https://mapmyvisitors.com/map.js?d=23pIdJVhMjN_8WNUnKTi-FQTV-hOMyUeuluWO9V4xPc&cl=ffffff&w=180';
  // Keep the widget hidden while its script records visits.
  mount.append(script);
})();
