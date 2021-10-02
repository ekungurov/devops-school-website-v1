<?php
  include 'config.inc.php';
  
  $db = new PDO($dsn, $user, $pass);
  
  include 'models/CharacterModel.php';
  $characterModel = new CharacterModel($db);
  $characterList = $characterModel->getAllCharacters();
  
  include 'views/character-list.php';
?>