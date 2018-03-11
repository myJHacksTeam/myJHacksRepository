<?php
require("db_header.php");
$sql = "UPDATE Trashcan SET current_value = " . $_POST["value"] . "WHERE id =". $_POST["id"];
$result=$conn->query($sql);
if(!$result) {
	echo $conn->error;
  die("Id not found");
}
?>
