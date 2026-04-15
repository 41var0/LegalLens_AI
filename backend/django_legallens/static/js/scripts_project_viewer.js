function enableButtonChange() {
//  alert("Acceso denegado.");
    document.getElementById("buttonChange").disabled = false;
}



function saveChanges() {

    // Obtenemos los datos cambiables
    const data = {
        fecha_limite: document.getElementById("fecha_limite").value,
        descripcion: document.getElementById("descripcion").value,
    };

    // Llamamos a "project_updater" con los datos cambiables
    fetch(PROJECT_UPDATE_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken(), // proteccion con CSRF (obligatorio en Django)
        },
        body: JSON.stringify(data),
    })
    .then(response => { // Comprobacion de respuesatas

        if (response.status === 200) { // Ok
            response.text().then( respuesta => {
                alert(respuesta);
            })

        } else if (response.status === 403) { // HttpResponseForbidden
            alert("No tienes permiso para realizar esta acción.");
            return;

        } else if (response.status === 500 ) { // HttpResponseServerError
            alert("Error del servidor. La accion no se ha podido completar.");
            return;

        } else {    // Algun otro error
            alert("Error desconocido. La accion no se ha podidio llevar a cabo.");
            return;
        }

        document.getElementById("buttonChange").disabled = true;
    });
}





function deleteProject() {
    if (!confirm("Pulsa  OK  para confirmar la eliminacion del proyecto ")) return;

    fetch(PROJECT_DELETE_URL, {
        method: "POST",
        headers: {
            "X-CSRFToken": getCSRFToken(), // proteccion con CSRF (obligatorio en Django)
        }
    })
    .then(response => {
        if (response.status === 200) {// Ok
            response.text().then( respuesta => {
                alert(respuesta);
            })

            window.location.href = HOME_URL;

        } else if (response.status === 403) {
            alert("No tienes permiso para borrar este proyecto.");
            return;
        } else {    // Algun otro error
            alert("Error desconocido. La accion no se ha podidio llevar a cabo.");
            return;
        }
    });
}





function stateTaskChange(state, task_url){


    // Llamamos a "task_updater" con los datos cambiables
    const data = {
        nuevo_estado: state
    };


    fetch(task_url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken(), // proteccion con CSRF (obligatorio en Django)
        },
        body: JSON.stringify(data),
    })
    .then(response => {
        if (response.status === 200) {// Ok
            response.text().then( respuesta => {
                alert(respuesta);
            })
            return;
        } else if (response.status === 403) {
            alert("No tienes permiso para editar el estado de esta tarea.");
            return;
        } else {    // Algun otro error
            alert("Error desconocido. La accion no se ha podidio llevar a cabo.");
            return;
        }
    });

}






// CSRF helper
function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}

