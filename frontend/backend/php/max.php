<?php
require("db_header.php");
$sql = "SELECT MAX(id) FROM Trashcan";
$result=$conn->query($sql);
if(!$result) {
	echo $conn->error;
  die("Id not found");
}
$row = $result->fetch_assoc();
echo $row;//['id'];
?>
