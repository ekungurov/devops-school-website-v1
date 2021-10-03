<head>
  <style>
  table, th, td {
    border: 1px solid #aaa;
  }
  </style>
</head>
<body>

<h1><?= $planetName ?></h1>
<table>
  <thead>
    <tr>
      <th>ID</th>
      <th>Name</th>
      <th>Gender</th>
      <th>Eye Color</th>
    </tr>
  </thead>
  <tbody>
    <?php foreach ($characterList as $row): ?>
    <tr>
      <td><?= $row['id'] ?></td>
      <td><?= $row['name'] ?></td>
      <td><?= $row['gender'] ?></td>
      <td><?= $row['eye_color'] ?></td>
    </tr>
    <?php endforeach?>
  </tbody>
</table>
<p><a href="index.php">Back to planets</a></p>

</body>