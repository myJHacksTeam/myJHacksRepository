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

var locations = [
  [38.983515, -76.945702], //Caroline Hall, 1106-1130
  [38.983192, -76.945544], //Frederick Hall, 237-245
  [38.982764, -76.948741], //UMD Hillel
  [38.982976, -76.946987], //Van Munching, East Entrance
  [38.983736, -76.947414], //Van Munching, North Entrance
  [38.985248, -76.946095], //Queen Anne, Main Entrance
  [38.986001, -76.942559], //McKeldin Mall, Center
  [38.987305, -76.941936], //ESJ, Room 0224
]



var gradient = [
  'rgba(255, 0, 0, 0)',
  'rgba(255, 0, 0, 1)'
]

function eqfeed_callback(results) {
  var heatmapData = [];

  for (var i = 0; i < locations.length; i++) {
  var coords = locations[i];
  var latLng = new google.maps.LatLng(coords[0], coords[1]);
  heatmapData.push(latLng);
	}

  var heatmap = new google.maps.visualization.HeatmapLayer({
    data: heatmapData,
    dissipating: true,
    map: map,
    radius: 20
  });

  heatmap.set('gradient', gradient);


}
