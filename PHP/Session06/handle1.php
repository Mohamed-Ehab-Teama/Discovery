<?php

// echo "<pre>";
// var_dump( $_POST );
// echo "<hr>";
// var_dump( $_GET );
// echo "</pre>";

// $arr = [
//     "one" => 2002,
//     "Two" => 2005,
//     "thr" => "Alii"
// ];


// echo "Name : " . $_POST['user_name'];
// echo "<br>";
// echo "Email : " . $_POST['user_email'];
// echo "<br>";
// echo "password : " . $_POST['password'];

// $name = $_POST['user_name'];
// $email = $_POST['user_email'];
// $pass = $_POST['password'];

foreach ( $_POST as $key => $value ) {
    $$key = $value;
}

// $user_name
// $user_email
// $password

// if ( empty($user_name) or empty($user_email) or empty($password) ){
//     echo "Some Fields are Empty";
// } 

// Check Empty Fields
if ( empty($user_name)   ){
    echo "Name Cannot be Empty";
}
elseif ( empty($user_email) ){
    echo "Email Cannot be Empty";
}
elseif ( empty($password) ){
    echo "password Cannot be Empty";
}

// Check Valid Email    
if ( !filter_var( $user_email , FILTER_VALIDATE_EMAIL ) ) {
    echo "Please Insert Valid Email";
}


$user_name = htmlentities( htmlspecialchars( $user_name ) );
$user_email = htmlentities( htmlspecialchars( $user_email ) );
$password = htmlentities( htmlspecialchars( $password ) );




