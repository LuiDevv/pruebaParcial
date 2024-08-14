// static/js/contact-form.js
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('contactForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Evita el envío real del formulario
        alert('Enviado exitosamente'); // Muestra la alerta
    });
});
