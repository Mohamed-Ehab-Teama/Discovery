<?php

// Arrays

// PHP Indexed Arrays:
    // In indexed arrays each item has an index number.
    // By default, the first item has index 0, the second item has item 1


// PHP Associative Arrays
    // Associative arrays are arrays that use named keys that you assign to them


// Create Array:
    // $cars = array("Volvo", "BMW", "Toyota");
    // $cars = ["Volvo", "BMW", "Toyota"];
    // $cars = [
    //     0 => "Volvo",
    //     1 => "BMW",
    //     2 =>"Toyota"
    //   ];
    // $myCar = [
    //     "brand" => "Ford",
    //     "model" => "Mustang",
    //     "year" => 1964
    //   ];

// Array Without Keys
    // $arr0 = [ 10, 20, 30, 40, 50 ];
    // $arr1 = [ "one" , "Two" , "Three" ];
    // $arr2 = [ true , false , true ];
    // $arr3 = [ 50, 120.6 , "Two" , "Three" , true ];


// Array With Keys
    // $arr1 = [ 
    //     "one" => "Mohamed" ,
    //     "Two" => "Ahmed" , 
    //     "Three" => "Ali"
    // ];


// Print Array:
    // print_r()
    // print_r( $arr )

    // echo $arr[0];
    // echo $arr["one"];




            // Variables
// Variables are "containers" for storing information
    // [1] Start With Dollar Sign $
    // [2] Start With A Letter [a-z] Or [A-Z] Or Underscore
    // [3] You Can Use Numbers Inside The Name
    // [4] No Special Characters Allowed
    // [5] Case Sensitive

    // $userName = "Mohamed";
    // $track = 'Backend';

    // echo $username;
    // echo $Username;
    // echo 'Hello $username';
    // echo "Hello $username";



// PHP is a Loosely Typed Language:
    // It does not require the specification of the data types in variables



// To get the data type of a variable: 
    // use the var_dump() function

    // var_dump( $userName )


    // $x = "John";
    // $x = $y = $z = "Fruit";


// Variable Variable
    // Takes The Value Of A Variable And Treats That As The Name Of A Variable

    // $x = "PHP";
    // $$x = "Backend";
    // $$$x = "Developer";

    // echo $x;
    // echo $$x;
    // echo $$$x;
    // echo $PHP;
    // echo $Backend;
    // echo "Hello ${$x}";
    // echo "<br>";
    // echo "Hello ${$$x}";


// Assign Variable By Reference
    // - By Default, Variables Are Always Assigned By Value
    // - Assigned By Reference Make Variable Alias Or Point To Another

    // Assign by values[Default]
        // $a = "Ali";
        // $b = $a;
        // echo $a;
        // echo $b;
    
    // Assign by Reference
        // $a = "Ali";
        // $b = &$a;
        // $b = "Mohamed";
        // $a = "GG";
        // echo $a;
        // echo $b;


// Pre-Defined Variables:
    // Superglobals — Built-in variables that are always available in all scopes
    // $GLOBALS — References all variables available in global scope
    // $_SERVER — Server and execution environment information
    // $_GET — HTTP GET variables
    // $_POST — HTTP POST variables
    // $_FILES — HTTP File Upload variables
    // $_REQUEST — HTTP Request variables
    // $_SESSION — Session variables
    // $_ENV — Environment variables
    // $_COOKIE — HTTP Cookies



// Constants
    // - That Value Cannot Change During The Execution
    // - Constants Always Uppercase

    // define("USER_NAME", "Mohamed Ehab Teama");
    // define("PASSWORS_LENGTH", 16);
  
    // echo USER_NAME;
    // echo PASSWORS_LENGTH;

// Pre-Defined Constants [Case Sensitive]
    // PHP_VERSION
    // PHP_OS_FAMILY
    // PHP_INT_MAX
    // DEFAULT_INCLUDE_PATH

// Magic Constants [Case Insensitive]
    // __LINE__
    // __FILE__
    // __DIR__
