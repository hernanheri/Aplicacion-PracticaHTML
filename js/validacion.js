document.getElementById("registroForm").addEventListener("submit", function(event) {
    // Evitar el envío del formulario hasta validar
    event.preventDefault();

    // Obtener valores de los campos
    const nombreCompleto = document.getElementById("nombreCompleto").value.trim();
    const email = document.getElementById("email").value.trim();
    const fechaNacimiento = document.getElementById("fechaNacimiento").value;
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;

    // Validar que los campos no estén vacíos
    if (nombreCompleto === "" || email === "" || fechaNacimiento === "" || password === "" || confirmPassword === "") {
        alert("Todos los campos son obligatorios.");
        return;
    }

    // Validar el formato del correo electrónico
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert("Por favor, ingresa un correo electrónico válido.");
        return;
    }

    // Validar que el usuario sea mayor de edad (18 años)
    const hoy = new Date();
    const fechaNac = new Date(fechaNacimiento);
    const edad = hoy.getFullYear() - fechaNac.getFullYear();
    const mes = hoy.getMonth() - fechaNac.getMonth();
    if (mes < 0 || (mes === 0 && hoy.getDate() < fechaNac.getDate())) {
        edad--;
    }
    if (edad < 18) {
        alert("Debes tener al menos 18 años para registrarte.");
        return;
    }

    // Validar que la contraseña sea alfanumérica
    const alfanumericoRegex = /^[a-zA-Z0-9]+$/;
    if (!alfanumericoRegex.test(password)) {
        alert("La contraseña debe contener solo caracteres alfanuméricos.");
        return;
    }

    // Validar que las contraseñas coincidan
    if (password !== confirmPassword) {
        alert("Las contraseñas no coinciden.");
        return;
    }

    // Si todo está correcto
    alert("Formulario enviado correctamente.");
    this.submit(); // Enviar el formulario
});
