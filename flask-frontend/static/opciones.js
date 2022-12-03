options = {
     type : ["(place_id)"]
}
var originInput = document.getElementById("destino")
var originAutocomplete = new google.maps.places.Autocomplete(originInput,options)