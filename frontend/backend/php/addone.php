<?php
require("db_header.php");
$sql = "SELECT FIRST(current_value) FROM Trashcan WHERE id = " . $_POST["id"];
echo $sql;
$result=$conn->query($sql);
if(!$result) {
	echo $conn->error;
	die("Id Not Found");
}
$curr_val = $result->fetch_[0]();
$new_val = $curr_val[0] + 1;
$sql = "UPDATE Trashcan SET current_value = " . $new_val . " WHERE id = ". $_POST["id"];
echo $sql;

$result=$conn->query($sql);
if(!$result) {
	echo $conn->error;
  die("Id not found");
}
?>
