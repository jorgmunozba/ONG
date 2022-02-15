function getLocation() {
    if(navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        jQuery('#geo').html('No se pudo obtener la ubicacion.');
    }
}
    
function showPosition(position) {
    var latitud = position.coords.latitude;
    var longitud = position.coords.longitude;
    var linkAPI = 'http://api.weatherapi.com/v1/current.json?key=c0f80ee9e94a4fdb8eb205632211605&q=';
    var linkFinal = linkAPI + latitud + ',' + longitud;
    jQuery.getJSON(linkFinal, 
    function(data) {

        jQuery('#geo').html('--' + data.location.name+ ', '+data.location.country+': '+data.current.temp_c + ' °C  --')
    });

}


jQuery(document).ready(function() {

    jQuery('#btnClima').click(function() {
        getLocation();
    });
});