<head>
  <style>
  table, th, td {
    border: 1px solid #aaa;
  }
  </style>
</head>
<body>

<h1>Planets of a galaxy far, far away...</h1>
<table>
  <thead>
    <tr>
      <th>ID</th>
      <th>Name</th>
      <th>Climate</th>
      <th>Gravity</th>
    </tr>
  </thead>
  <tbody>
    <?php 
    foreach ($planetList as $row):
      $id = $row['id'] 
    ?>
    <tr>
      <td><?= $id ?></td>
      <td><a href=<?= "planet.php?id=".$id ?>>
        <?= $row['name'] ?>
      </a></td>
      <td><?= $row['climate'] ?></td>
      <td><?= $row['gravity'] ?></td>
    </tr>
    <?php endforeach ?>
  </tbody>
</table>

</body>