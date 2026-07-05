/*
  CONVERTFLY · DECK STAGE
  Engine genérica para decks HTML no design system Convertfly.
  Navegação por teclado, trilha de miniaturas, print-to-PDF.

  Uso: div#cf-deck com os slides dentro, mais este arquivo carregado via tag de script.
*/
(function () {
  function initDeck(root) {
    var slides = Array.prototype.slice.call(root.querySelectorAll('.cf-slide'));
    var current = 0;

    function render() {
      slides.forEach(function (s, i) {
        s.classList.toggle('cf-slide--active', i === current);
      });
      var counter = document.getElementById('cf-deck-counter');
      if (counter) counter.textContent = (current + 1) + ' / ' + slides.length;
      var rail = document.getElementById('cf-deck-rail');
      if (rail) {
        Array.prototype.forEach.call(rail.children, function (t, i) {
          t.classList.toggle('cf-rail-thumb--active', i === current);
        });
      }
    }

    function go(i) {
      current = Math.max(0, Math.min(slides.length - 1, i));
      render();
    }

    function buildRail() {
      var rail = document.getElementById('cf-deck-rail');
      if (!rail) return;
      slides.forEach(function (s, i) {
        var thumb = document.createElement('button');
        thumb.className = 'cf-rail-thumb';
        thumb.type = 'button';
        thumb.textContent = i + 1;
        thumb.addEventListener('click', function () { go(i); });
        rail.appendChild(thumb);
      });
    }

    document.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') { e.preventDefault(); go(current + 1); }
      if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); go(current - 1); }
      if (e.key === 'Home') { e.preventDefault(); go(0); }
      if (e.key === 'End') { e.preventDefault(); go(slides.length - 1); }
    });

    var prevBtn = document.getElementById('cf-deck-prev');
    var nextBtn = document.getElementById('cf-deck-next');
    if (prevBtn) prevBtn.addEventListener('click', function () { go(current - 1); });
    if (nextBtn) nextBtn.addEventListener('click', function () { go(current + 1); });

    var printBtn = document.getElementById('cf-deck-print');
    if (printBtn) printBtn.addEventListener('click', function () { window.print(); });

    buildRail();
    render();
  }

  document.addEventListener('DOMContentLoaded', function () {
    var deck = document.getElementById('cf-deck');
    if (deck) initDeck(deck);
  });
})();
