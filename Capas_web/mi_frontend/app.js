const API_URL = 'http://localhost:8000';

// Pide todas las mascotas al BE y las muestra
async function cargarMascotas() {
    const response = await fetch(`${API_URL}/mascotas`);
    const mascotas = await response.json();
    // ... lógica para crear los <li> en la lista
}

// Envía los datos del formulario al BE para crear una nueva
async function agregarMascota() {
    // ... lógica para enviar datos con fetch y el método POST
}

// Llama a la función al cargar la página
window.onload = cargarMascotas;