<?php

require_once './connection.php';


if ( $_SERVER['REQUEST_METHOD'] == 'POST' ){

    // var_dump($_POST);
    // die;

    foreach ( $_POST as $key => $value ){
        $$key = $value;
    }

    // echo $name;
    // echo $email;
    // echo $pass;

    if ( empty($name) or empty($email) or empty($pass) ){
        echo "Fields cannot be Empty";
        die;
    }

    if ( !filter_var( $email, FILTER_VALIDATE_EMAIL) ){
        echo "please Enter a valid Email";
        die;
    }

    $email = filter_var( $email, FILTER_SANITIZE_EMAIL );

    if ( strlen($pass) < 6 or strlen($pass) > 20  ){
        echo " Password must be between 6 and 20 characters ";
        die;
    }

    $pass = md5($pass);


    // Store in Database

    $sql = " INSERT INTO users (name, email, password) VALUES ('$name', '$email', '$pass') ";

    $result = mysqli_query( $connection , $sql );

    if ( $result ){
        echo "Registered Successfully";
    }else{
        echo "Registered Went Wrong";
    }


}
else{
    echo "Something went Wrong";
    die;
}