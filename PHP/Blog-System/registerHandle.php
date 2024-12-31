<?php

require_once 'connection.php';

if ( $_SERVER['REQUEST_METHOD'] == 'POST' )
{

    foreach ( $_POST as $key => $value )
    {
        $$key = $value;
    }

    if( empty($name)  ){
        echo "Name Cannot be Empty";
        die;
    }
    if( empty($email)  ){
        echo "Email Cannot be Empty";
        die;
    }
    if( empty($pass)  ){
        echo "Password Cannot be Empty";
        die;
    }
    if( empty($cpass)  ){
        echo "Confirm-Password Cannot be Empty";
        die;
    }

    if( !filter_var($email, FILTER_VALIDATE_EMAIL) )
    {
        echo "Not Valid Email";
        die;
    }

    $email = filter_var( $email, FILTER_SANITIZE_EMAIL );

    if($pass != $cpass){
        echo " Password and confirm must be the same ";
        die;
    }

    $pass = md5($pass);





    $sql = " INSERT INTO users (name, email, password) VALUES ( '$name', '$email', '$pass' ) ; ";
    $res = mysqli_query( $connection, $sql );

    if ( $res )
    {
        header('location:login.php');
    }
    else{
        header('location:register.php');
    }





}
else
{
    header('location:register.php');
    die;
}