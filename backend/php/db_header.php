<?php
$server="localhost";
$username="user";
$dbname="JHacks";
$password="password";

$conn = new mysqli($servername, $username, $password, $dbname);
if($conn->connect_error) {
  die("Failed to connect to the database.");
} ?>
