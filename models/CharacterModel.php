<?php
class CharacterModel
{
  protected $db;
  
  public function __construct(PDO $db)
  {
    $this->db = $db;
  }

  public function getCharacters($planetId) {
    $stmt = $this->db->prepare("SELECT people.* FROM people JOIN planet ON people.planet_id = planet.id WHERE planet.id = :id");
    $stmt->bindParam(':id', $planetId, PDO::PARAM_INT);
    $stmt->execute();
    return $stmt->fetchAll();
  }
}
?>