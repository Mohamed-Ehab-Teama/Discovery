<?php

if ( $_SERVER['REQUEST_METHOD'] != 'POST' ){
    echo "You are not allowed";
    die;
}

$name = $_POST['name'];
$email = $_POST['email'];
$password = $_POST['password'];

// echo $name . '<br>' . $email . '<br>' . $password;

if ( empty($name) ){
    echo "Name cannot be empty";
    die;
}elseif ( empty($email) ){
    echo "Email cannot be empty";
    die;
}elseif ( empty($password) ){
    echo "Password cannot be empty";
    die;
}

$name = htmlspecialchars( htmlentities($name) );
$email = htmlspecialchars( htmlentities($email) );
$password = htmlspecialchars( htmlentities($password) );

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    echo "Please Enter a valid Email";
    die;
}

$email = filter_var( $email, FILTER_SANITIZE_EMAIL );