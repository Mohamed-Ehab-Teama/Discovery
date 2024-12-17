<?php
require_once 'connection.php';
foreach($_POST as $key => $value){
    $$key = $value;
}
if (empty($email) or empty ($pass)){
    echo "fields cannot be empty";
    die;
}
if (!filter_var($email, FILTER_VALIDATE_EMAIL)){
    echo"email is not valid";
    die;
}
$sql = "SELECT * FROM users";
$res = mysqli_query($connection,$sql);
if ($res){
    while($row = mysqli_fetch_assoc($res)){
        if ($email == $row['email'] and $pass == $row ['password']){
            echo "loginsucess";
            die;
        }else{
            echo "login failed";
            die;
        }
    }
}