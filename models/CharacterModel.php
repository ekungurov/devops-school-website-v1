<?php
class PeopleModel
{
  protected $db;
  
  public function __construct(PDO $db)
  {
    $this->db = $db;
  }
  
  public function getAllPeople() {
    return $this->db->query("SELECT * FROM people");
  }
}
?>