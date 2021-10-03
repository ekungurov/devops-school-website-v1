<?php
  include 'config.inc.php';
  
  $db = new PDO($dsn, $user, $pass);
  $id = filter_input(INPUT_GET, 'id', FILTER_SANITIZE_NUMBER_INT);

  include 'models/PlanetModel.php';
  $planetModel = new PlanetModel($db);
  $planetName = $planetModel->getPlanetName($id);

  include 'models/CharacterModel.php';
  $characterModel = new CharacterModel($db);
  $characterList = $characterModel->getCharacters($id);
  
  include 'views/character-list.php';
?>