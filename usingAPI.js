alert("hi")

var map;
var view;
var ourLoc;

function init(){
  ourLoc = ol.proj.fromLonLat([41.043316, 28.862457]);

  view = newol.View({
    center: ourLoc,
    zoom: 6
  });

map = new ol.Map({
    target: 'map',
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM()
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

function panToLocation(){
  var country = document.getElementById("country-name").value;
  if(country == ""){
    alert("Insert Country Name!");
    return;
  }

  var query = "https://restcountries.eu/rest/v2/name/"+country
  query = query.replace(/ /g,"%20");
  alert(query);

  var country_request = new XMLHttpRequest();
  country_request.open('GET', query, true);
  country_request.onload = processCountryRequest
  country_request.send();

    /*alert("Ready State" + country_request.readyState);
    alert("Status" + country_request.status);
    alert("Response" + country_request.responseText);*/
  }

  function processCountryRequest(){
    if(country_request.readyState != 4){
      return;
    }
  }

  // || means or, you can find these above your enter key and pressing shift
  if(country_request.status != 200 || country_request.responseText ===""){
    window.console.error("Request had an error!");
    return;
  }

  var countryInfo = JSON.parse(country_request.responseText);

  var lon = countryInfo[0].latlng[1];
  var lat = countryInfo[0].latlng[0];

  window.console.log(country +": lon " + lon +"& lat " + lat);

  var location = ol.proj.fromLonLat([lon,lat]);

  view.animate({
    center: location,
    duration: 200
  });

}
