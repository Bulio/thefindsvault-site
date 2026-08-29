
(function () {
  var BATCH = 6;
  var grid = document.getElementById('grid');
  var sentinel = document.getElementById('sentinel');
  var endMsg = document.getElementById('end-msg');
  var catPills = document.querySelectorAll('.pill[data-cat]');
  var sortPills = document.querySelectorAll('.pill[data-sort]');
  var searchBox = document.getElementById('search');
  var resultCount = document.getElementById('result-count');
  var all = [];
  var filtered = [];
  var shown = 0;
  // slug delle card gia' stampate nell'HTML dal generatore: al primo giro non
  // si svuota la griglia, si continua ad appendere da dove sono arrivate.
  var gia = {};
  var quantiGia = 0;
  Array.prototype.forEach.call(grid.querySelectorAll('.card[data-slug]'), function (el) {
    gia[el.getAttribute('data-slug')] = 1; quantiGia++;
  });
  var primoGiro = true;
  var activeCat = 'All';
  var activeSort = 'best';
  var query = '';

  function esc(s) {
    var d = document.createElement('div');
    d.textContent = s || '';
    return d.innerHTML;
  }

  // <picture> con WebP + fallback JPG, width/height sempre quando noti.
  // La primissima card e' l'immagine LCP della home: quella non va in lazy.
  function media(c, prima) {
    var dim = c.imageW ? ' width="' + c.imageW + '" height="' + c.imageH + '"' : '';
    var carica = prima ? ' loading="eager" fetchpriority="high"' : ' loading="lazy"';
    var img = '<img src="' + c.image + '" alt="' + esc(c.title) + '"' + dim + carica + '>';
    if (!c.imageWebp) return img;
    return '<picture><source srcset="' + c.imageWebp + '" type="image/webp">' + img + '</picture>';
  }

  function cardHTML(c, primaDellaPagina) {
    var badge = c.rating >= 4.7 ? '<span class="badge">Top Rated</span>' : '';
    var newBadge = c.isNew ? '<span class="badge badge-new">New</span>' : '';
    var watchBtn = c.youtube
      ? '<a class="watch-btn" href="' + c.youtube + '" target="_blank" rel="noopener" ' +
        'onclick="event.stopPropagation()">&#9654; YouTube</a>'
      : '';
    // niente <a> annidati: il link al prodotto avvolge foto+testo, il
    // bottone YouTube e' un elemento indipendente in fondo alla card.
    return (
      '<div class="card" data-slug="' + esc(c.slug) + '">' +
        '<a class="card-link" href="products/' + c.slug + '/index.html">' +
          '<div class="card-media">' + badge + newBadge + media(c, primaDellaPagina) +
          '</div>' +
          '<div class="card-body">' +
            '<span class="cat-chip">' + esc(c.category) + '</span>' +
            '<h3>' + esc(c.title) + '</h3>' +
            '<p class="hook">' + esc(c.hook) + '</p>' +
            '<div class="meta"><span class="price">See price &rarr;</span></div>' +
          '</div>' +
        '</a>' +
        '<div class="card-actions">' + watchBtn + '</div>' +
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
    next.forEach(function (c, i) {
      var div = document.createElement('div');
      div.className = 'card-wrap';
      div.innerHTML = cardHTML(c, !quantiGia && shown === 0 && i === 0);
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

  function shuffle(arr) {
    for (var i = arr.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = arr[i]; arr[i] = arr[j]; arr[j] = t;
    }
    return arr;
  }

  function recompute() {
    // si tengono le card statiche solo finche' l'utente non tocca niente:
    // al primo filtro/ordinamento/ricerca la griglia riparte da zero.
    var tieni = primoGiro && quantiGia &&
                activeCat === 'All' && activeSort === 'best' && !query;
    if (!tieni) grid.innerHTML = '';
    shown = 0;
    endMsg.hidden = true;
    sentinel.classList.remove('done');

    filtered = activeCat === 'All' ? all.slice() : all.filter(function (c) { return c.category === activeCat; });

    if (query) {
      var q = query.toLowerCase();
      filtered = filtered.filter(function (c) {
        return (c.title + ' ' + c.hook + ' ' + c.category).toLowerCase().indexOf(q) !== -1;
      });
    }

    if (activeSort === 'newest') {
      filtered.sort(function (a, b) { return (b.order || 0) - (a.order || 0); });
    } else if (activeSort === 'random') {
      shuffle(filtered);
    } else {
      filtered.sort(function (a, b) {
        return ((b.rating || 0) - (a.rating || 0)) || ((b.reviews || 0) - (a.reviews || 0));
      });
    }

    if (resultCount) {
      resultCount.textContent = filtered.length + ' finds';
    }
    if (tieni) {
      // le card gia' a video non vanno riappese: si tolgono dalla coda
      filtered = filtered.filter(function (c) { return !gia[c.slug]; });
    }
    primoGiro = false;
    renderNext();
  }

  catPills.forEach(function (btn) {
    btn.addEventListener('click', function () {
      catPills.forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active');
      activeCat = btn.dataset.cat;
      recompute();
    });
  });

  sortPills.forEach(function (btn) {
    btn.addEventListener('click', function () {
      sortPills.forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active');
      activeSort = btn.dataset.sort;
      recompute();
    });
  });

  if (searchBox) {
    searchBox.addEventListener('input', function () {
      query = searchBox.value.trim();
      recompute();
    });
  }

  // tile collezioni: click = filtra quella categoria e scrolla alla griglia
  document.querySelectorAll('.feat-tile').forEach(function (tile) {
    tile.addEventListener('click', function () {
      var cat = tile.dataset.cat;
      catPills.forEach(function (b) {
        b.classList.toggle('active', b.dataset.cat === cat);
      });
      activeCat = cat;
      recompute();
      grid.scrollIntoView({ behavior: 'smooth', block: 'start' });
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
      recompute();
    })
    .catch(function () {
      grid.innerHTML = '<p style="color:#b9b0a2">Could not load products right now.</p>';
    });
})();
