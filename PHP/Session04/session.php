<?php

/*
functions:
built-in functions [Math, array, string]
    array functions :    array_push()    array_pull()    array_unshift()    array_shift()            count()     explode(separator, value)
    string functions :   strlen()    strrev()    trim()  implode(separator, value)
    math functions :
*/
/*
search :
    - String functions
    - Array functions
    - Math functions
*/

/*
User defined functions:
    function function_name(parameters){              [default value : (parameter = value)]
        code
    }

    function_name(arguments);
*/


// function hello() {
//     return "hello";
// }
// hello();

// function add ($x , $y){
//     echo $x + $y;
// }
// add(5,20);


// function add3 ( $x , $y , $z ) {
//     return $x + $y + $z;
// }
// echo add3(15,60,100);

// function speak ($name = 'Unknown') {
//     return "Hello $name";
// }
// echo speak("Ali");

// $arr = [10,20,30,40];

// array_push($arr , 10);
// array_unshift($arr , 10);
// array_shift($arr);
// array_pop($arr);

// $str = implode( "<hr>", $arr);
// echo $str;

// $s = "Mohamed Ehab Teama BFCAI IS";
// $arr2 = explode ( "e", $s );

// echo '<pre>';
// print_r($arr2);
// echo '</pre>';

// $str = " ##Mohamed## ";
// echo strrev($str);
// echo "<hr>";
// echo strlen($str);
// echo "<hr>";
// echo trim ($str, " #");


// $arr = [20,200,50,60,748];
// $x = max($arr);
// echo min($arr);
// echo min($arr);



/*
Superglobals
    $GLOBALS : is an array that contains all global variables.
    $_SERVER : is a PHP super global variable which holds information about headers, paths, and script locations.
    $_REQUEST : is a PHP super global variable which contains submitted form data, and all cookie data.
    $_POST : contains an array of variables received via the HTTP POST method.
    $_GET : contains an array of variables received via the HTTP GET method.
    $_COOKIE
    $_SESSION
*/

// echo "<pre>";
// print_r( $GLOBALS);
// print_r($_SERVER);   $_SERVER['REQUEST_METHOD'] == 'GET POST';
// print_r($_REQUEST);
// print_r($_GET);
// print_r($_POST);
// echo "</pre>";

