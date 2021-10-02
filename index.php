<?php
  include 'config.inc.php';
  
  $db = new PDO($dsn, $user, $pass);
  
  include 'models/CharacterModel.php';
  $peopleModel = new PeopleModel($db);
  $peopleList = $peopleModel->getAllPeople();
  
  include 'views/character-list.php';
?>