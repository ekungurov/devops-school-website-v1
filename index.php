<?php
  include 'config.inc.php';
  
  function getAllPeople($db) {
    $stmt = $db->prepare("SELECT * FROM people");
    $stmt->execute();
    return $stmt->fetchAll();
  }
   
  $db = new PDO($dsn, $user, $pass);
  $results = getAllPeople($db);
  
  echo "<table>";
  echo "<thead><tr><th>ID</th><th>Name</th></tr></thead>";
  echo "<tbody>";
  foreach ($results as $row) {
    echo "<tr>";
    echo "<td>".$row['id']."</td>";
    echo "<td>".$row['name']."</td>";
    echo "</tr>";   
  }
  echo "</tbody></table>";
?>