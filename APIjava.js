alert("hi")

var map;
var view;
var ourLoc;

function init(){
  ourLoc = ol.proj.fromLonLat([41.043316, 28.862457]);

  view = new ol.View({
    center: ourLoc,
    zoom: 6
  });

  map = new ol.Map({
    target: 'map',
    layers: [
      new ol.layer.Tile({
        source: new.ol.source.OSM()
      })
    ],
    loadTilesWhileAnimating: true,
    view: view
  });
}

function panHome(){
  view.animate({
    center: ourLoc,
    duration: 2000
  });
}

window.onload = init;
