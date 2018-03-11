<?php
require("db_header.php");
$sql = "INSERT INTO Trashcan (id, nickname, current_value, location, total_value) VALUES ('".$_POST["id"].",Hillel,0,NULL,0')";
echo $sql;
$result = $conn->query($sql);
if(!$result) {
	echo $conn->error;
  die("Id not found");
}
echo "stuff";
?>
