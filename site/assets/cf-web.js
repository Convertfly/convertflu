/* Convertfly · comportamento compartilhado do site */
(function () {
  'use strict';

  /* ── Nav: transparente no topo, pílula branca ao rolar ───── */
  var nav = document.querySelector('.nav');
  if (nav) {
    var stuck = false;
    var sync = function () {
      var next = window.scrollY > 32;
      if (next !== stuck) { stuck = next; nav.classList.toggle('is-stuck', stuck); }
    };
    sync();
    window.addEventListener('scroll', sync, { passive: true });

    /* ── Menu mobile ──────────────────────────────────────── */
    var toggle = nav.querySelector('.nav-toggle');
    var links = nav.querySelector('.nav-links');
    if (toggle && links) {
      var setOpen = function (open) {
        nav.classList.toggle('is-open', open);
        toggle.setAttribute('aria-expanded', String(open));
        toggle.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
      };
      toggle.addEventListener('click', function () {
        setOpen(!nav.classList.contains('is-open'));
      });
      links.addEventListener('click', function (e) {
        if (e.target.closest('a')) setOpen(false);
      });
      document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && nav.classList.contains('is-open')) { setOpen(false); toggle.focus(); }
      });
      document.addEventListener('click', function (e) {
        if (nav.classList.contains('is-open') && !nav.contains(e.target)) setOpen(false);
      });
    }
  }

  /* ── Formulário de contato: validação e confirmação ──────── */
  var form = document.querySelector('form[data-contato]');
  if (!form) return;

  var required = ['nome', 'email', 'zap'];
  var emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

  var setErro = function (id, msg) {
    var input = document.getElementById(id);
    if (!input) return;
    var field = input.closest('.field');
    field.classList.toggle('field--erro', !!msg);
    input.setAttribute('aria-invalid', msg ? 'true' : 'false');
    var el = field.querySelector('.field-msg');
    if (msg && !el) {
      el = document.createElement('p');
      el.className = 'field-msg';
      field.appendChild(el);
    }
    if (el) el.textContent = msg || '';
    if (!msg && el) el.remove();
  };

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var ok = true, primeiro = null;

    required.forEach(function (id) {
      var input = document.getElementById(id);
      if (!input) return;
      var v = input.value.trim();
      var msg = '';
      if (!v) msg = 'Preencha este campo para a gente conseguir te responder.';
      else if (id === 'email' && !emailRe.test(v)) msg = 'Confira o e-mail — parece faltar alguma coisa.';
      setErro(id, msg);
      if (msg) { ok = false; if (!primeiro) primeiro = input; }
    });

    if (!ok) { primeiro.focus(); return; }

    var btn = form.querySelector('button[type="submit"]');
    btn.setAttribute('aria-busy', 'true');
    btn.textContent = 'Enviando…';

    window.setTimeout(function () {
      var nome = (document.getElementById('nome').value.trim().split(' ')[0]) || '';
      var ok_ = document.createElement('div');
      ok_.className = 'form-ok';
      ok_.setAttribute('role', 'status');
      ok_.innerHTML = '<h3>Recebemos, ' + nome + '.</h3>' +
        '<p>A gente responde em até um dia útil, pelo WhatsApp que você deixou. ' +
        'Se preferir adiantar, chama no <strong>+55 11 93618-5493</strong>.</p>';
      form.replaceChildren(ok_);
      ok_.scrollIntoView({ block: 'center' });
    }, 600);
  });

  ['nome', 'email', 'zap'].forEach(function (id) {
    var input = document.getElementById(id);
    if (input) input.addEventListener('input', function () { setErro(id, ''); });
  });
})();
