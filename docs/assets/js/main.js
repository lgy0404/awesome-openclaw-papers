document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('searchInput');
  const filterBtns = document.querySelectorAll('.filter-btn');
  const categorySections = document.querySelectorAll('.category-section');
  const paperCards = document.querySelectorAll('.paper-card');
  const noResults = document.getElementById('noResults');
  const resultsInfo = document.getElementById('resultsInfo');
  const themeToggle = document.getElementById('themeToggle');

  // --- Theme ---
  const savedTheme = localStorage.getItem('theme') ||
    (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  document.documentElement.setAttribute('data-theme', savedTheme);

  themeToggle.addEventListener('click', () => {
    const current = document.documentElement.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
  });

  // --- Search keyboard shortcut ---
  document.addEventListener('keydown', (e) => {
    if (e.key === '/' && document.activeElement !== searchInput) {
      e.preventDefault();
      searchInput.focus();
    }
    if (e.key === 'Escape') {
      searchInput.blur();
      searchInput.value = '';
      applyFilters();
    }
  });

  // --- Tag click to search ---
  document.querySelectorAll('.tag').forEach(tag => {
    tag.addEventListener('click', () => {
      searchInput.value = tag.dataset.tag;
      setActiveFilter('all');
      applyFilters();
      searchInput.focus();
    });
  });

  // --- Filtering ---
  let activeFilter = 'all';

  function setActiveFilter(filter) {
    activeFilter = filter;
    filterBtns.forEach(btn => {
      btn.classList.toggle('active', btn.dataset.filter === filter);
    });
  }

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      setActiveFilter(btn.dataset.filter);
      applyFilters();
    });
  });

  searchInput.addEventListener('input', () => applyFilters());

  function applyFilters() {
    const query = searchInput.value.toLowerCase().trim();
    let visibleCount = 0;

    categorySections.forEach(section => {
      const categoryId = section.dataset.category;
      const matchesFilter = activeFilter === 'all' || activeFilter === categoryId;
      const cards = section.querySelectorAll('.paper-card');
      let sectionVisible = false;

      cards.forEach(card => {
        const text = card.textContent.toLowerCase();
        const tags = (card.dataset.tags || '').toLowerCase();
        const matchesSearch = !query || text.includes(query) || tags.includes(query);
        const show = matchesFilter && matchesSearch;
        card.classList.toggle('hidden', !show);
        if (show) {
          sectionVisible = true;
          visibleCount++;
        }
      });

      // For project cards (not .paper-card)
      const projectCards = section.querySelectorAll('.project-card');
      projectCards.forEach(card => {
        const text = card.textContent.toLowerCase();
        const matchesSearch = !query || text.includes(query);
        const show = matchesFilter && matchesSearch;
        card.style.display = show ? '' : 'none';
        if (show) {
          sectionVisible = true;
          visibleCount++;
        }
      });

      section.classList.toggle('hidden', !sectionVisible);
    });

    if (noResults) {
      noResults.style.display = visibleCount === 0 ? 'block' : 'none';
    }

    if (resultsInfo) {
      if (query) {
        resultsInfo.style.display = 'block';
        resultsInfo.textContent = `Found ${visibleCount} result${visibleCount !== 1 ? 's' : ''} for "${searchInput.value}"`;
      } else {
        resultsInfo.style.display = 'none';
      }
    }
  }

  // --- Smooth scroll for anchor links ---
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });
});
