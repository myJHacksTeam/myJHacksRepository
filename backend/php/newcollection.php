<?php
require("db_header.php");
$sql = "SELECT current_value,total_value FROM Trashcan WHERE id=".$_POST["id"];
$result=$conn->query($sql);
if(!$result) {
  die("Id not found");
}



$row = $result->fetch_assoc();
$total_value = $row["total_value"];
$current_value = $row["current_value"];
$total_value = $total_value + $current_value;
$current_value = 0

$sql = "UPDATE Trashcan SET current_value = " . $current_value . ", total_value =". $total_value ." WHERE id =". $_POST["id"];
$result=$conn->query($sql);
if(!$result) {
  die("Id not found");
}


?>
