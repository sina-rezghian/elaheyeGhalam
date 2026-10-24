'use strict';

document.documentElement.classList.add('js');
const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#site-nav');
const dropdown = document.querySelector('.nav-dropdown');

function closeMenu() {
  navigation.classList.remove('is-open');
  menuButton.setAttribute('aria-expanded', 'false');
}

if (menuButton && navigation) {
  menuButton.hidden = false;
  menuButton.addEventListener('click', () => {
    const isOpen = navigation.classList.toggle('is-open');
    menuButton.setAttribute('aria-expanded', String(isOpen));
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape') {
      if (dropdown && dropdown.open) {
        dropdown.open = false;
        dropdown.querySelector('summary').focus();
      } else if (navigation.classList.contains('is-open')) {
        closeMenu();
        menuButton.focus();
      }
    }
  });
  document.addEventListener('click', event => {
    if (dropdown && !dropdown.contains(event.target)) dropdown.open = false;
    if (!navigation.contains(event.target) && !menuButton.contains(event.target)) closeMenu();
  });
  window.matchMedia('(min-width: 801px)').addEventListener('change', closeMenu);
}
