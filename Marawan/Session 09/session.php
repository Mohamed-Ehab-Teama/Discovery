<?php

// DRY => Don't Repeat Yourself

// function add_10_20 () {
//     echo 10 + 20 ;
// }
// add_10_20();
// add_10_20();
// add_10_20();


// function add($x , $y) {
//     echo $x + $y;
// }
// add(10,50);
// echo "<br>";
// add( 100, 150 );


// function add( $a = 0 , $b = 0 ){
//     echo $a + $b;
// }
// add();
// add(50);
// add(50, 50);



// function add( $x1, $x2) {
//     echo $x1 + $x2;
// }

// function addR( $x1, $x2) {
//     return $x1 + $x2;
// }

// add(1,2);
// echo "<br>";
// echo addR(9,9);
// echo "<br>";
// $z = addR(9,9);
// echo "HHHHH - " . $z;




// function test( &$number ){
//     return $number += 5;
// }
// // echo test(10);
// $x = 20;
// echo test( $x ); // 25
// echo test( $x ); // 30
// echo test( $x ); // 35
// echo "<br>";
// echo $x;    // 25



// function add_many_numbers(...$x){
//     $sum = 0;
//     for ( $i = 0; $i < count($x); $i++ ){
//         $sum += $x[$i];
//     }
//     return $sum;
// }

// echo add_many_numbers() ;
// echo "<br>";
// echo add_many_numbers(10) ;
// echo "<br>";
// echo add_many_numbers(10,20,30,40,50) ;
// echo "<br>";
// echo add_many_numbers(-10, 50, 700) ;


// function myFamily( $lastName, ...$firstName ){
//     for ( $i = 0; $i < count($firstName); $i++ ){
//         echo $firstName[$i] . " " . $lastName . "<br>";
//     }
// }
// $arr = ['Ahmed', 'Amr', "Mohamed", "Ehab"];

// myFamily("Teama", 'Amr', 'Ahmed', "Mohamed", "Ehab");
// echo "<hr>";
// myFamily( "Teama", ...$arr );




// function add($x , $y) : float {
//     return $x + $y;
// }

// echo add ( 10 ,20 );
// echo "<br>";
// var_dump(add ( 10 ,20 ));



// Variable Function
// function one(){
//     return "Hello From One Function ";
// }
// echo one();

// $var = "one";
// echo "<br>";
// echo $var;
// echo "<br>";
// echo $var();        // one();
// echo "<br>";
// echo "<br>";

// function hello($name) {
//     return " Hello $name ";
// }
// echo hello("Mohamed");      // Hello Mohamed
// echo "<br>";
// $n = "hello";   

// echo $n;                // hello
// echo "<br>";
// echo $n();              // hello()  =>  Error
// echo "<br>";
// echo $n("Marwan");      // Hello Marwan


// function hello(){
//     return "hello";
// }

// if ( function_exists("hello1") ){
//     echo hello();
// }else{
//     echo "Function Not Existed";
// }
// echo "<br>";

// function connect_to_DB(){
//     return mysqli_connect('localhost','root','','kero_blog');
// }

// if ( function_exists('connect_to_DB') ) {
//     $connection = connect_to_DB();
// }else{
//     echo " Connection Error";
//     die;
// }

// var_dump($connection);



// function double_number($number){
//     return $number * 2 ;
// }

// $nums = [1,2,3,4,5,6,7,8,9,10];

// echo "<pre>";
// print_r( array_map( "double_number", $nums ) );
// echo "</pre>";


// $greet = function( ) {
//     return " Hello From Anoynomus Function ";
// };
// echo $greet( );

// $greet = fn() => "Hello From Anoynomus Function";
// echo $greet();


// $greet = function( $firstName, $lastName ){
//     return " Hello $firstName - $lastName  From Anoynomus Function ";
// };
// echo $greet( "Mohamed", "Ehab" );

// $greet = fn($firstName, $lastName) => " Hello $firstName - $lastName  From Anoynomus Function ";
// echo $greet( "Mohamed", "Ehab" );


// $NickName = "Hamo";
// $greet = function( $firstName, $lastName ) use ($NickName){
//     return " Hello $firstName - $lastName [$NickName] From Anoynomus Function ";
// };
// echo $greet( "Mohamed", "Ehab" );

// $NickName = "Hamo";
// $greet = fn($firstName, $lastName) => "Hello $firstName - $lastName [$NickName] From Anoynomus Function";
// echo $greet( "Mohamed", "Ehab" );


// Recursive functions in PHP