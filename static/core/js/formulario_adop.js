$(document).ready(function(){


    $('#form2').validate({
        rules: {
        
            nombre2: {
                required: true,
                minlength: 5,
            },
            nombremascota: {
                required: true,
                minlength: 5,
                
            },
            idmascota: {
                required: true,
                number:true,
            },
            email2:{
                required: true,
                email:true,
            },
            telefono2: {
                required: true,
                number:true,
            }
        },

        messages: {
            nombre2:{
                minlength: "El nombre debe tener al menos 5 caracteres"
            },
            nombremascota: {
                required: "Debe ingresar el nombre de mascota.",
                minlength: "El nombre de mascota debe tener al menos 5 carácteres"
            },
            idmascota: {
                required: "Debe ingresar ID de mascota",
                number:"El ID debe contener sólo números"
            },
            email2: {
                required: "Debe ingresar correo electronico",
                email: "Fomato de correo incorrecto"
            },
            telefono2: {
                required: "Debe ingresar numero de telefono",
                number: "El número de telefono solo debe incluir números",
            }
        }



    });

})
