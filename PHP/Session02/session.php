<?php

/*
Constants - Predefined Constants - Magic constants
Operators : ( Arithmetic Assignment Comparison Increment Logical )
if      if esle     if elseif else
switch
*/

/*
Constants - Predefined Constants - Magic constants
    to define constant:
        1- define (name, value, case-sensitive)
        2- const name = value

                define()	                                                const keyword
            Defines constants at runtime	                        Defines class constants at compile time
            Can be defined anywhere in the script	                Can only be defined within classes or interfaces
            Case-insensitive by default	                            Case-sensitive by default
            Global scope	                                        Class scope

    Pre-defined Constants:
        PHP_VERSION     PHP_INT_MAX     PHP_INT_MIN     PHP_FLOAT_MAX       PHP_FLOAT_MIN
    
    Magic Constants:
        __DIR__     __FILE__        __LINE__
*/



// define("USER_NAME", "Mohamed");
// const NAME = "Ali";



// echo USER_NAME;
// echo "<br>";
// echo NAME;
// echo "<br>";
// echo "<br>";
//              Pre-defined Constants
// echo PHP_VERSION;
// echo "<br>";
// echo PHP_FLOAT_MAX;
// echo "<br>";
// echo PHP_FLOAT_MIN;
// echo "<br>";
// echo PHP_INT_MIN;
// echo "<br>";
// echo PHP_INT_MAX;
// echo "<br>";
// echo "<br>";

//              Magic Constants
// echo __LINE__ ;
// echo "<br>";
// echo __DIR__;
// echo "<br>";
// echo __FILE__;
// echo "<br>";




/*
Arithmetic Operators:
    +   -   *   /   %   **

Assignment Operators:
    =   +=  -=  *=  /=  %/

Comparison Operators:
    ==  ===     !=  <>  !==     >   <   >=  <=          <=> (SpaceShip)

Increment / Decrement Operators:
    $x++    $x--    ++$x    --$x

Logical Operators:
    and     &&     or      ||      !

*/

//      Power
// echo 5 ** 3;

// $x = 10;

// $x = $x + 10;

// $x += 10;
// $x -= 10;
// $x *= 10;
// $x /= 10;
// $x %= 10;
// $x **= 10;

//              SpaceShip Operator
// echo 10 <=> 100 ;
// echo 100 <=> 100 ;
// echo 102 <=> 100 ;


// $x = 2;

// echo $x++;
// echo ++$x;

// echo $x--;
// echo --$x;

// echo $x;


echo "<br>";






// Conditional Statements:
/*
    if      if else         if elseif else
        if(condition){
            code
        }

        if(condition){
            code
        }else{
            code
        }

        if(condition){
            code
        }elseif (condition) {
            code
        }else {
            code
        }

    Short hand if:
        if (condition) ? True : False ;
*/





/*
    Switch:

        switch (expression) {
            case label1:
                //code block
                break;
            case label2:
                //code block;
                break;
            case label3:
                //code block
                break;
            default:
                //code block
            }
        
        switch (expression) {
            case label1:
            case label2:
            case label3:
                //code block
                break;
            default:
                //code block
            }

*/


$x = 15;

// if ( $x > 10 ){
//     echo "$x is greater than 10";
// }

// if ($x > 10 ){
//     echo "True";
// }else {
//     echo "False";
// }

// if ( $x == 10){
//     echo "Equal";
// } elseif ( $x >= 10) {
//     echo "Greater";
// }else{
//     echo "Less than";
// }


$x = 50;

switch ($x){
    case 10:
    case 30:
    case 20:
        echo "Equal 20";
        break;
    case 50:
        echo "Equal 50";
        break;
    case 100:
        echo "Equal 100";
        break;
    default:
        echo "Something went wrong";
}