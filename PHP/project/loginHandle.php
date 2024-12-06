<?php

require_once './connection.php';

if ( $_SERVER['REQUEST_METHOD'] != 'POST' ){
    echo " Something Went Wrong ";
    die;
}



foreach ( $_POST as $key => $value ){
    $$key = $value;
}
// $email
// $pass


if ( empty($email) or empty($pass) ){
    echo "Fields cannot be empty";
    die;
}

if ( !filter_var($email, FILTER_VALIDATE_EMAIL) ){
    echo " InValid Email ";
    die;
}

$email = filter_var( $email, FILTER_SANITIZE_EMAIL);

$pass = md5($pass);


$sql = " SELECT * FROM users ";
$result = mysqli_query($connection, $sql);

if ( $result ){
    while ( $row = mysqli_fetch_assoc($result) ){
        
        if ( $email == $row['email'] and $pass == $row['password'] ){
            echo "Login Success";
            die;
        }else{
            echo "Login Failed";
            // header('location:login.php');
            die;
        }

    }
}