<?php
require("db_header.php");
$sql = "INSERT INTO Trashcan (nickname, current_value, location, total_value) VALUES (" . $_POST["nickname"]."',0,'".$_POST["location"]."',0)";
echo $sql;
$result = $conn->query($sql);
if(!$result) {
	echo $conn->error;
  die("Id not found");
}
echo "stuff";
?>
