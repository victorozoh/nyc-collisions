var borough;
var records;

// Displays mapbox map component on webpage
mapboxgl.accessToken = 'pk.eyJ1IjoiYmJtYXBib3giLCJhIjoiY2tmenRyeWcyMmR3eDJ5czNzcjd0MG1sMiJ9.TYbeYuIfPsb178PAPzUj0w';
var map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/dark-v9', // stylesheet location
  center: [-74.5, 40], // starting position [lng, lat]
  zoom: 9 // starting zoom
})

// display locations on a map
$(function(){

  $("#display").click(function(){
    borough = $( "#selected_borough" ).val();
    $.getJSON("/api/boroughs/".concat(borough), function(data){
      console.log(data[0]);
    });
    console.log(borough);
  });

});
