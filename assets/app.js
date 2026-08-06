
(function () {
  var BATCH = 6;
  var grid = document.getElementById('grid');
  var sentinel = document.getElementById('sentinel');
  var endMsg = document.getElementById('end-msg');
  var pills = document.querySelectorAll('.pill');
  var all = [];
  var filtered = [];
  var shown = 0;
  var activeCat = 'All';

  function stars(rating) {
    var full = Math.round(rating);
    return '★'.repeat(full) + '☆'.repeat(5 - full);
  }

  function esc(s) {
    var d = document.createElement('div');
    d.textContent = s || '';
    return d.innerHTML;
  }

  function cardHTML(c) {
    var badge = c.rating >= 4.7 ? '<span class="badge">Top Rated</span>' : '';
    var reviews = c.reviews ? '(' + c.reviews.toLocaleString() + ')' : '';
    var watchBtn = c.youtube
      ? '<a class="watch-btn" href="' + c.youtube + '" target="_blank" rel="noopener" ' +
        'aria-label="Watch on YouTube" onclick="event.stopPropagation()">&#9654;</a>'
      : '';
    // niente <a> annidati: il link al prodotto avvolge foto+testo, il
    // bottone YouTube e' un elemento indipendente sopra l'immagine.
    return (
      '<div class="card">' +
        '<a class="card-link" href="products/' + c.slug + '/index.html">' +
          '<div class="card-media">' + badge +
            '<img src="' + c.image + '" alt="' + esc(c.title) + '" loading="lazy">' +
          '</div>' +
          '<div class="card-body">' +
            '<span class="cat-chip">' + esc(c.category) + '</span>' +
            '<h3>' + esc(c.title) + '</h3>' +
            '<p class="hook">' + esc(c.hook) + '</p>' +
            '<div class="meta">' +
              '<span class="stars">' + stars(c.rating) + '</span>' +
              '<span class="reviews">' + reviews + '</span>' +
              '<span class="price">' + esc(c.price) + '</span>' +
            '</div>' +
          '</div>' +
        '</a>' +
        watchBtn +
      '</div>'
    );
  }

  var sentinelVisible = false;

  function renderNext() {
    var next = filtered.slice(shown, shown + BATCH);
    if (!next.length) {
      sentinel.classList.add('done');
      endMsg.hidden = filtered.length === 0;
      return;
    }
    var frag = document.createDocumentFragment();
    next.forEach(function (c) {
      var div = document.createElement('div');
      div.className = 'card-wrap';
      div.innerHTML = cardHTML(c);
      frag.appendChild(div.firstChild);
    });
    grid.appendChild(frag);
    shown += next.length;
    if (shown >= filtered.length) {
      sentinel.classList.add('done');
      endMsg.hidden = false;
      return;
    }
    endMsg.hidden = true;
    // sentinel likely still inside the viewport on tall/desktop screens after
    // a small batch -- IntersectionObserver only fires on enter/exit, not
    // while continuously visible, so keep pulling batches until it's
    // actually pushed off-screen or we run out of items.
    if (sentinelVisible) {
      requestAnimationFrame(renderNext);
    }
  }

  function applyFilter(cat) {
    activeCat = cat;
    grid.innerHTML = '';
    shown = 0;
    endMsg.hidden = true;
    filtered = cat === 'All' ? all : all.filter(function (c) { return c.category === cat; });
    renderNext();
  }

  pills.forEach(function (btn) {
    btn.addEventListener('click', function () {
      pills.forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active');
      applyFilter(btn.dataset.cat);
    });
  });

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      sentinelVisible = e.isIntersecting;
      if (e.isIntersecting && all.length) renderNext();
    });
  }, { rootMargin: '400px' });
  io.observe(sentinel);

  fetch('assets/products.json')
    .then(function (r) { return r.json(); })
    .then(function (data) {
      all = data;
      sentinel.classList.remove('done');
      applyFilter('All');
    })
    .catch(function () {
      grid.innerHTML = '<p style="color:#b9b0a2">Could not load products right now.</p>';
    });
})();
