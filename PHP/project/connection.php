<?php

$hostName = 'localhost';
$DBName = 'back';
$DBUser = 'root';
$DBPass = '';

$connection = mysqli_connect($hostName, $DBUser, $DBPass, $DBName);

// if ($connection){
//     echo "Done";
// }else{
//     echo "Error";
// }