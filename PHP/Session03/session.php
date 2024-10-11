<?php

/*
Arrays
Loops: (While, Do While, for, foreach)
functions
    array functions     array_push()    array_pull()    array_unshift()    array_shift()            count()     explode(separator, value)
    string functions    strlen()    strrev()    trim()  implode(separator, value)
*/


/*
Arrays:
    define array:
        1- $arr = [value, value, value]
        2- $arr = array(value, value, value)

    Indexed arrays:             $arr = [1,2,3,4,5,6]
    Associative arrays:         $arr = ['key' => value, 'key' => value]
    Multi-Dimention array

    Add elements to array : 
        arr[] = value
        array_push( array, values)

    remove elements from array : 
        unset( $array[index] )
        array_pop($array)

    sorting arrays:
        sort - rsort - asort - arsort - ksort - krsort
        sort($array)

*/



// $arr = [];   or      $arr = array();

// $arr = [10,20,30,40, "Mohamed", "Session", True];


// array_unshift($arr , "Hello ");
// array_shift($arr);

// array_push($arr, "last");
// array_pop($arr);


// $arr = [
//     [10,20,30,40] ,
//     ["Ali", "Moba"] ,
//     [2002,2005]
// ];




// echo "<pre>";
// print_r($arr);
// echo "</pre>";




















/*
Loops : 
    while (condition) {
        code & increment
    }

    do {
        code & increment
    } while (condition);

    for (expression1, expression2, expression3) {
        // code block
    }
    
    for ($array as $value) {
        // code block
    }
    
    for ($array as $key => $value) {
        // code block
    }

*/



// $i = 0;
// while ( $i < 10 ){
//     echo $i;
//     echo "<br>";
//     $i++;
// }

// $i = -1;
// do {
//     echo $i;
//     echo "<br>";
//     $i--;
// } while ($i >= 0);


// for ( $i = 0; $i < 15; $i++)
// {
//     echo $i;
//     echo "<br>";
// }


// $arr = [ 10, 20, 30, 40, 50];

// foreach ( $arr as $value ) {
//     echo $value;
//     echo "<hr>";
// }













