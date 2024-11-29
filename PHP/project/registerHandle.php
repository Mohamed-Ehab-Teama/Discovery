<?php

require_once 'connection.php';

// echo "<pre>";
// print_r($_POST);
// echo "</pre>";

foreach ( $_POST as $key => $value )
{
    $$key = $value;
}

// echo $name;
// echo "<br>";
// echo $email;
// echo "<br>";
// echo $pass;

if ( empty($name) or empty($email) or empty($pass) ){
    echo "Fields cannot be Empty";
    die;
}

if ( !filter_var ( $email, FILTER_VALIDATE_EMAIL ))
{
    echo "Not Valid Email";
    die;
}

$email = filter_var ( $email, FILTER_SANITIZE_EMAIL );


$sql = " INSERT INTO users (id,name,email,password) VALUES ('1','$name','$email', '$pass') ";
$result = mysqli_query( $connection, $sql );

if ( $result ){
    echo "Done Successfully";
}