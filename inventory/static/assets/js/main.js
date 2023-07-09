function classToggle() {
    const navs = document.querySelectorAll('.navbar-toggler')
    
    navs.forEach(nav => nav.classList.toggle('navbar-togglerShow'));
  }
  
  document.querySelector('.navbar-toggler')
    .addEventListener('click', classToggle);