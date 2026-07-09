document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('[data-header]');
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.nav');
  const cursor = document.querySelector('.cursor-dot');

  const updateHeader = () => header?.classList.toggle('is-scrolled', window.scrollY > 20);
  updateHeader();
  window.addEventListener('scroll', updateHeader, { passive: true });

  toggle?.addEventListener('click', () => {
    const open = nav.classList.toggle('is-open');
    toggle.setAttribute('aria-expanded', String(open));
  });

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });
  document.querySelectorAll('.reveal').forEach((el) => observer.observe(el));

  const filterButtons = document.querySelectorAll('[data-filter]');
  const productCards = document.querySelectorAll('[data-category]');
  const applyFilter = (filter) => {
    filterButtons.forEach((button) => {
      button.classList.toggle('is-active', button.dataset.filter === filter);
    });
    productCards.forEach((card) => {
      const visible = filter === 'all' || card.dataset.category === filter;
      card.classList.toggle('is-hidden', !visible);
    });
  };

  filterButtons.forEach((button) => {
    button.addEventListener('click', () => {
      applyFilter(button.dataset.filter);
      history.replaceState(null, '', button.dataset.filter === 'all' ? 'collection.html' : `#${button.dataset.filter}`);
    });
  });

  if (filterButtons.length && window.location.hash) {
    const requested = window.location.hash.replace('#', '');
    if (document.querySelector(`[data-filter="${requested}"]`)) {
      applyFilter(requested);
    }
  }

  document.querySelectorAll('form[data-form-message]').forEach((form) => {
    form.addEventListener('submit', (event) => {
      event.preventDefault();
      const status = form.querySelector('.form-status');
      if (status) status.textContent = form.dataset.formMessage;
      form.classList.add('is-sent');
    });
  });

  if (cursor && window.matchMedia('(pointer:fine)').matches) {
    document.addEventListener('mousemove', (event) => {
      cursor.classList.add('is-active');
      cursor.style.left = `${event.clientX}px`;
      cursor.style.top = `${event.clientY}px`;
    });
    document.querySelectorAll('a,button,.card,.note-pill,input,textarea,select').forEach((el) => {
      el.addEventListener('mouseenter', () => cursor.classList.add('is-hover'));
      el.addEventListener('mouseleave', () => cursor.classList.remove('is-hover'));
    });
  }
});
