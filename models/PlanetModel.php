<?php
class PlanetModel
{
  protected $db;
  
  public function __construct(PDO $db)
  {
    $this->db = $db;
  }
  
  public function getAllPlanets() {
    return $this->db->query("SELECT * FROM planet");
  }

  public function getPlanetName($id) {
    $stmt = $this->db->prepare("SELECT * FROM planet WHERE id = :id");
    $stmt->bindParam(':id', $id, PDO::PARAM_INT);
    $stmt->execute();
    $row = $stmt->fetch();
    return $row['name'];
  }
}
?>