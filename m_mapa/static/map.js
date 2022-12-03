options = {
     type : ["(place_id)"]
}
var originInput = document.getElementById("destino")
var originAutocomplete = new google.maps.places.Autocomplete(originInput,options )

var lima_coordinates = {lat: -12.046374, lng: -77.042793}
var mapOptions = {
     center : lima_coordinates,
     zoom : 15,
     mapTypeId : google.maps.MapTypeId.ROADMAP 
}


var map = new google.maps.Map(document.getElementById("map"), mapOptions)

var directionService = new google.maps.DirectionsService()

var directionDisplay = new google.maps.DirectionsRenderer()

directionDisplay.setMap(map)

//var origen = document.getElementById("Origen_Tienda").innerHTML
//var destino = document.getElementById("Destino_Ubicacion").innerHTML

function CalcularRuta(){
     var request = {
          origin: document.getElementById("Origen_Tienda").innerHTML,
          destination: document.getElementById("Destino_Ubicacion").innerHTML,
          travelMode: google.maps.TravelMode.DRIVING,
          unitSystem: google.maps.UnitSystem.IMPERIAL
     }

     directionService.route(request, (result, status) => {
          if(status == google.maps.DirectionsStatus.OK) {
               const output = document.querySelector("#output");
               output.innerHTML = "<div> Tiempo aproximado en llegar: " + result.routes[0].legs[0].duration.text + "</div>";

               directionDisplay.setDirections(result);
          }
          else{
               directionDisplay.setDirections({routes:{}});    
               map.setCenter(lima_coordinates);      
               output.innerHTML = "<div> No fue posible calcular la ruta </div>";

          }
     })
}

CalcularRuta()