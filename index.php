<?php
  include 'config.inc.php';
  
  $db = new PDO($dsn, $user, $pass);
  
  include 'models/PlanetModel.php';
  $planetModel = new PlanetModel($db);
  $planetList = $planetModel->getAllPlanets();
  
  include 'views/planet-list.php';
?>