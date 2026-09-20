// Scorrimento infinito dell'elenco episodi.
// Le prime 9 schede sono gia' nell'HTML: questo aggiunge le altre, sei per volta, quando il
// fondo della pagina entra nello schermo. Se il JavaScript non parte, la pagina resta valida.
(function () {
  var fondo = document.getElementById('fondo');
  var griglia = document.getElementById('griglia');
  var fine = document.getElementById('fine');
  if (!fondo || !griglia || fondo.hidden) return;
  var coda = null, i = 0, PASSO = 6, inCorso = false;

  function mostra() {
    if (inCorso || !coda) return;
    inCorso = true;
    var pezzo = coda.slice(i, i + PASSO);
    i += pezzo.length;
    pezzo.forEach(function (html) {
      var d = document.createElement('div');
      d.innerHTML = html;
      griglia.appendChild(d.firstChild);
    });
    if (i >= coda.length) { fondo.hidden = true; fine.hidden = false; obs.disconnect(); }
    inCorso = false;
  }

  var obs = new IntersectionObserver(function (voci) {
    if (!voci[0].isIntersecting) return;
    if (coda) return mostra();
    fetch('altri.json').then(function (r) { return r.json(); })
      .then(function (d) { coda = d; mostra(); })
      .catch(function () { fondo.hidden = true; });   // niente errore a schermo: si smette e basta
  }, { rootMargin: '400px' });
  obs.observe(fondo);
})();
