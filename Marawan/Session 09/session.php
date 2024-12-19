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





echo "<br>";
echo "<br>";
echo "<br>";
echo "<br>";
echo "<br>";