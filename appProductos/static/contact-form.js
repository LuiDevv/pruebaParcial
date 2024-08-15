
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('contactForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Evita el envío real del formulario
        alert('Enviado exitosamente'); // Muestra la alerta
    });
});


document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');

    loginForm.onsubmit = function(event) {
        const username = loginForm.username.value.trim();
        const password = loginForm.password.value.trim();

        if (username === "" || password === "") {
            event.preventDefault(); // Previene el envío del formulario
            alert("Por favor, completa todos los campos.");
        } else if (username !== "nombre_usuario_valido" || password !== "contraseña_valida") {
            event.preventDefault(); // Previene el envío del formulario
            alert("Usuario incorrecto o no existe.");
        }
    };
});
