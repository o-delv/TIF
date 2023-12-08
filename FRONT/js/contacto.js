
        function validarFormulario() {
            var nombre = document.getElementById("nombre").value;
            var apellido = document.getElementById("apellido").value;
            var correo = document.getElementById("correo").value;
            var comentario = document.getElementById("comentario").value;

            if (nombre.trim() === "") {
                alert("Por favor, ingrese su nombre.");
                return false;
            }

            if (apellido.trim() === "") {
                alert("Por favor, ingrese su apellido.");
                return false;
            }

            if (correo.trim() === "" || !correo.includes("@")) {
                alert("Por favor, ingrese una dirección de correo válida.");
                return false;
            }

            if (comentario.trim() === "") {
                alert("Por favor, escriba su consulta.");
                return false;
            }

            return true;
        }

        var formulario = document.querySelector("form");
        formulario.addEventListener("submit", function (event) {
            if (!validarFormulario()) {
                event.preventDefault();
            }
        });