<?php
require("db_header.php");
$sql = "UPDATE Trashcan SET current_value = 0, total_value = 0 WHERE id =". $_POST["id"];
$result=$conn->query($sql);
if(!$result) {
  die("Id not found");
}
?>
