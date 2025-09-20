const API_URL = 'http://localhost:8000';

// Pide todos los carros al backend y los muestra en la lista
async function cargarCarros() {
    const response = await fetch(`${API_URL}/Carros`);
    const carros = await response.json();

    const lista = document.getElementById("lista-carros");
    lista.innerHTML = ""; // limpia la lista antes de volver a pintar

    carros.forEach(carro => {
        const li = document.createElement("li");
        li.textContent = `ID: ${carro.id} - Marca: ${carro.marca}, Modelo: ${carro.modelo}`;
        lista.appendChild(li);
    });
}

// Envía un carro nuevo al backend
async function agregarCarro() {
    const id = document.getElementById("id").value;
    const marca = document.getElementById("marca").value;
    const modelo = document.getElementById("modelo").value;

    const nuevoCarro = { id: Number(id), marca, modelo };

    await fetch(`${API_URL}/Carros`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(nuevoCarro)
    });

    cargarCarros(); // vuelve a cargar la lista después de añadir
}

// Al cargar la página, se muestran los carros existentes
window.onload = cargarCarros;
