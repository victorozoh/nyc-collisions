var borough;
var geojson;

// Displays mapbox map component on webpage
mapboxgl.accessToken = 'pk.eyJ1IjoiYmJtYXBib3giLCJhIjoiY2tmenRyeWcyMmR3eDJ5czNzcjd0MG1sMiJ9.TYbeYuIfPsb178PAPzUj0w';
var map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/dark-v9', // stylesheet location
  center: [-73.9, 40.7], // starting position [lng, lat]
  zoom: 9 // starting zoom
})

// display locations on a map
$(function(){

  $("#display").click(function(){
    borough = $( "#selected_borough" ).val();
    $.getJSON("/api/boroughs/".concat(borough), function(data){
      console.log(data[0]);

      // Add an image to use as a custom marker
      map.loadImage('https://docs.mapbox.com/mapbox-gl-js/assets/custom_marker.png', function (error, image) {
          if (error) throw error;
          map.addImage('my-marker', image);
          // Add a GeoJSON source
          var array_data = data;
          console.log(array_data.length);
          geojson = {
              "type": "FeatureCollection",
              "features": array_data
               }
          map.addSource('points', {type: 'geojson', data: geojson});

          // Add a symbol layer
          map.addLayer({
            "id": "points",
            "type": "symbol",
            "source": "points",
            "layout": {
                "icon-image": "my-marker",
                "icon-size": 0.1
            }
          });

      });// end of loadImage

    });// end of getJSON
  }); // end of onclick

});
