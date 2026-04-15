const tabs = document.querySelectorAll('.tab-btn');
const contents = document.querySelectorAll('.tab-content');

tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    // Cambiar estilo activo de tabs
    tabs.forEach(t => t.classList.remove('active'));
    tab.classList.add('active');

    // Mostrar u ocultar containers
    const target = tab.dataset.target;
    contents.forEach(c => {
      if(c.id === target){
        c.classList.add('show');
      } else {
        c.classList.remove('show');
      }
    });
  });
});
