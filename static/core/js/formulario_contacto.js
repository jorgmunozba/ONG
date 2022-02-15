$(document).ready(function(){

    $("#error").hide();

    $("#formulario").submit(function(){

        var mensaje = "";


        if($("#nombre").val().trim().length==0){
            mensaje += 'El nombre está vacío <br>';
        }

        if($("#correo").val().trim().length==0){
            mensaje += 'El correo está en vacío  <br>';
        }

        if($("#numero").val().trim().length != 9){
            mensaje += 'El numero de teléfono debe tener al menos 9 dígitos  <br>';
        }

        if($("#ciudad").val().trim().length==0){
            mensaje +='El nombre de ciudad está vacío  <br>';
        }
        
        if($("#mensaje").val().trim().length < 50){
            mensaje += 'El mensaje debe tener al menos 50 caracteres  <br>';
        }

        if(mensaje != ""){

            $("#error").html(mensaje);
            $("#error").show();
            event.preventDefault();



        }
    })
})
