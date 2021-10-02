<?php
class CharacterModel
{
  protected $db;
  
  public function __construct(PDO $db)
  {
    $this->db = $db;
  }
  
  public function getAllCharacters() {
    return $this->db->query("SELECT * FROM people");
  }
}
?>