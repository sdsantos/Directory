function loadMap(){
    var map = new GMap2(document.getElementById("map"));
    map.addControl(new GLargeMapControl());
    map.addControl(new GMapTypeControl());
    //set map center (vienna)
	
	var lat = parseFloat(document.getElementById("id_map_lat").value);
	var lon = parseFloat(document.getElementById("id_map_lon").value);
	
	if (!lat || !lon) {
		map.setCenter(new GLatLng(40.20614809577503, -8.41552734375), 12);
	} else {
		var point = new GLatLng(lat,lon);
		map.setCenter(point, 13);
		map.addOverlay(new GMarker(point));
	}
	
    GEvent.addListener(map, "click", function(overlay, point){
        map.clearOverlays();
        if (point) {
            map.addOverlay(new GMarker(point));
            map.panTo(point);
            document.getElementById("id_map_lat").value = point.lat(); //models field name 
            document.getElementById("id_map_lon").value = point.lng(); //models field name
        }
    });
}

// arrange for our onload handler to 'listen' for onload events
if (window.attachEvent) {
    window.attachEvent("onload", function(){
        loadMap(); // Internet Explorer
    });
}
else {
    window.addEventListener("load", function(){
        loadMap(); // Firefox and standard browsers
    }, false);
}
