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


// --- Para ver el archivo seleccionado (PDF) ---
const input = document.getElementById("doc");
const fileName = document.querySelector(".file-name");
const labelText = document.querySelector(".label-text");
const container = document.querySelector(".contedor-doc");

if (input) {
  input.addEventListener("change", function () {
    if (this.files.length > 0) {
      fileName.textContent = this.files[0].name;
      labelText.textContent = "Documento cargado";
      container.classList.add("has-file");
    } else {
      fileName.textContent = "";
      labelText.textContent = "Sube un documento";
      container.classList.remove("has-file");
    }
  });
}