<!DOCTYPE html>
<html lang="en-US">
<head>
  <link rel = "stylesheet" href="https://cdn.rawgit.com/openlayers/openlayers.github.io/master/en/v5.3.0/css/ol.css" type= "text/css">
  <script src= "https://cdn.rawgit.com/openlayers/openlayers.github.io/master/en/v5.3.0/build/ol.js"></script>
  <title>Weather Map</title>

  <script src="usingAPI.js" type="text/javascript"></script>
</head>
<body>
  <p>
    <button onclick="panHome()">Pan back to home</button>
  </p>
  <div id="map" class="map"></div>
  <footer>
    <p>This tutorial is based on code from: <a href ="http://openlayers.org/en/latest/examples/animation.html">Open Layers View animation</a></p>
    <p>This map uses the <a href="https://openlayers.org/">Open Layers API</a></p>
  </footer>
</body>
</html>
