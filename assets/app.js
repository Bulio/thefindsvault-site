
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
  var activeCat = 'All';
  var activeSort = 'best';
  var query = '';

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
    var newBadge = c.isNew ? '<span class="badge badge-new">New</span>' : '';
    var reviews = c.reviews ? '(' + c.reviews.toLocaleString() + ')' : '';
    var watchBtn = c.youtube
      ? '<a class="watch-btn" href="' + c.youtube + '" target="_blank" rel="noopener" ' +
        'onclick="event.stopPropagation()">&#9654; YouTube</a>'
      : '';
    // niente <a> annidati: il link al prodotto avvolge foto+testo, il
    // bottone YouTube e' un elemento indipendente in fondo alla card.
    return (
      '<div class="card">' +
        '<a class="card-link" href="products/' + c.slug + '/index.html">' +
          '<div class="card-media">' + badge + newBadge +
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

  function shuffle(arr) {
    for (var i = arr.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = arr[i]; arr[i] = arr[j]; arr[j] = t;
    }
    return arr;
  }

  function recompute() {
    grid.innerHTML = '';
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
    } else if (activeSort === 'price-low') {
      filtered.sort(function (a, b) { return (a.priceNum || 1e9) - (b.priceNum || 1e9); });
    } else if (activeSort === 'price-high') {
      filtered.sort(function (a, b) { return (b.priceNum || 0) - (a.priceNum || 0); });
    } else if (activeSort === 'under20') {
      filtered = filtered.filter(function (c) { return c.priceNum && c.priceNum < 20; });
      filtered.sort(function (a, b) { return (b.rating || 0) - (a.rating || 0); });
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
