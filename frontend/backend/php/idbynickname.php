<?php
require("db_header.php");
$sql = "SELECT id FROM Trashcan WHERE nickname = '".$_POST["nickname"]."'";
$result=$conn->query($sql);
if(!$result) {
	echo $conn->error;
  die("Id not found");
}
$row = $result->fetch_row();
echo $row[0];
?>
