/* Nav: transparente no topo, pílula branca ao rolar. */
(function () {
  var nav = document.querySelector('.nav');
  if (!nav) return;
  var stuck = false;
  function sync() {
    var next = window.scrollY > 32;
    if (next !== stuck) { stuck = next; nav.classList.toggle('is-stuck', stuck); }
  }
  sync();
  window.addEventListener('scroll', sync, { passive: true });
})();
