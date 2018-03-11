var map;

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 15,
    center: {
      lat: 38.9869,
      lng: -76.9426
    },
    mapTypeId: 'terrain'
  });


  var script = document.createElement('script');

  script.src = 'https://developers.google.com/maps/documentation/javascript/examples/json/earthquake_GeoJSONP.js';
  document.getElementsByTagName('head')[0].appendChild(script);

}


function eqfeed_callback(results) {
  var heatmapData = [];

  var coords = [38.9828, -76.9483];
  var latLng = new google.maps.LatLng(coords[0], coords[1]);
  

	var magnitude = 0.000001;
  var weightedLoc = {
  	location: latLng,
		weight: Math.pow(2, magnitude)
	};
	heatmapData.push(weightedLoc);


	var heatmap = new google.maps.visualization.HeatmapLayer({
  	data: heatmapData,
  	dissipating: false,
  	map: map,
    radius: 1
	});
  
  var gradient = [
    'rgba(255, 0, 0, 0)',
    'rgba(255, 0, 0, 0.1)',
    'rgba(255, 0, 0, 0.2)',
    'rgba(255, 0, 0, 0.3)',
    'rgba(255, 0, 0, 0.4)',
    'rgba(255, 0, 0, 0.5)',
    'rgba(255, 0, 0, 0.6)',
    'rgba(255, 0, 0, 0.7)',
    'rgba(255, 0, 0, 0.8)',
    'rgba(255, 0, 0, 0.9)',
    'rgba(255, 0, 0, 1)'
  ]
  heatmap.set('gradient', gradient);
  
  
}
