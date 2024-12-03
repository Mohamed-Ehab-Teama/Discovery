<?php

require_once './connection.php';

if ( $_SERVER['REQUEST_METHOD'] != 'POST' )
{
    echo " Something Went Wrong ";
    die;
}


foreach ( $_POST as $key => $value )
{
    $$key = $value;
}

// $email
// $pass

if ( empty($email) or empty($pass) ){
    echo " Fields cannot be Empty ";
    die;
}

if ( !filter_var( $email , FILTER_VALIDATE_EMAIL) ){
    echo " Email is Not Valid ";
    die;
}

$email = filter_var( $email, FILTER_SANITIZE_EMAIL );

$pass = md5($pass);


$sql = " SELECT * FROM users ";
$res = mysqli_query( $connection, $sql );

if ( $res ){

    while ( $user = mysqli_fetch_assoc( $res ) ){

        // echo "<pre>";
        // var_dump($user);
        // echo "</pre>";

        if ( $email == $user['email'] and  $pass == $user['password'] ){
            header('location:index.php');
            die;
            // echo " Login Success ";
            // die;
        }
        else{
            echo " Login fail ";
            die;
            // header('location:login.php');
            // die;
        }

    }
    

}
