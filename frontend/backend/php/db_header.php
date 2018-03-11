<?php
$server="localhost";
$username="user";
$dbname="jhacks";
$password="password";

$conn = new mysqli($server, $username, $password, $dbname);
if($conn->connect_error) {
  die("Failed to connect to the database.");
} ?>
