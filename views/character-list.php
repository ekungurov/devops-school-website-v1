<head>
  <style>
  table, th, td {
    border: 1px solid #aaa;
  }
  </style>
</head>
<body>

<table>
  <thead>
    <tr>
      <th>ID</th>
      <th>Name</th>
    </tr>
  </thead>
  <tbody>
    <?php foreach ($peopleList as $row): ?>
    <tr>
      <td><?= $row['id'] ?></td>
      <td><?= $row['name'] ?></td>
    </tr>
    <?php endforeach?>
  </tbody>
</table>

</body>