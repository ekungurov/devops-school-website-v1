<?php
  include 'config.inc.php';
  
  $db = new PDO($dsn, $user, $pass);
  
  include 'models/PeopleModel.php';
  $peopleModel = new PeopleModel($db);
  $peopleList = $peopleModel->getAllPeople();
  
  include 'views/people-list.php';
?>