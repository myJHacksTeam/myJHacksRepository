<?php
require("db_header.php");
$sql = "SELECT MAX(id) FROM Trashcan";
$result=$conn->query($sql);
if(!$result) {
	echo $conn->error;
  die("Id not found");
}
$thing = mysqli_fetch_field($result)
echo $thing;
?>
