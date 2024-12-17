<?php

require_once './connection.php';

// var_dump( $_GET ); 
$id = $_GET['id'];

$sql = " DELETE FROM users WHERE id = '$id' ";

$res = mysqli_query($connection, $sql);

if ( $res ){
    echo "Deleted Successfully";
    die;
}else{
    echo " Something went wrong ";
    die;
}
