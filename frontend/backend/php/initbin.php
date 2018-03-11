<?php
require("db_header.php");
$sql = "INSERT INTO Trashcan (id, current_value, location, total_value) VALUES ('".$_POST["id"].",0,NULL,0')";
$result = $conn->query($sql);
if(!$result) {
	echo $conn->error;
  die("Id not found");
}
echo "stuff";
?>
