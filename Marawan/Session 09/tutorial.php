<?php 

/*
Functions:
    A function is a block of statements that can be used repeatedly in a program.
    A function will not execute automatically when a page loads.
    A function will be executed by a call to the function.

    Functions:
        1 - Built-in Functions
            - can be called directly
        2 - User Defined Functions
            - create your own functions
*/

/*
---- Create a Function:
        - A function name must start with a letter or an underscore. 
        - Function names are NOT case-sensitive
        - Tip: Give the function a name that reflects what the function does!

    function myMessage() {
        echo "Hello world!";
    }

---- Call a Function:
    myMessage();
*/


/*
PHP Function Arguments:

    function familyName($fname) {
        echo "$fname Refsnes.<br>";
    }
    familyName("Jani");
    familyName("Hege");

    function familyName($fname, $year) {
        echo "$fname Refsnes. Born in $year <br>";
    }
    familyName("Hege", "1975");


PHP Default Argument Value:

    function setHeight($minheight = 50) {
        echo "The height is : $minheight <br>";
    }
    setHeight(350);
    setHeight();        // will use the default value of 50

*/

/*
PHP Functions - Returning values:
    - use the return statement:

    function sum($x, $y) {
        $z = $x + $y;
        return $z;
    }
    echo "5 + 10 = " . sum(5, 10) . "<br>";

    ------------------------------------------
Passing Arguments by Reference:

    function add_five(&$value) {
        $value += 5;
    }
    $num = 2;
    add_five($num);
    echo $num;
*/


/*
Variable Number of Arguments:
    - By using the ... operator in front of the function parameter, 
    - the function accepts an unknown number of arguments. 
    - This is also called a variadic function.

    function sumMyNumbers(...$x) {
        $n = 0;
        $len = count($x);
        for($i = 0; $i < $len; $i++) {
            $n += $x[$i];
        }
        return $n;
    }
    $a = sumMyNumbers(5, 2, 6, 2, 7, 7);
    echo $a;

    -------------------------------------------------

    function myFamily($lastname, ...$firstname) {
        txt = "";
        $len = count($firstname);
        for($i = 0; $i < $len; $i++) {
            $txt = $txt."Hi, $firstname[$i] $lastname.<br>";
        }
        return $txt;
    }
    $a = myFamily("Doe", "Jane", "John", "Joey");
    echo $a;


    - Variable Arguments List
        --- func_num_args()
        --- func_get_arg(index)
        --- func_get_args()


    $group_of_skills = ["HTML", "CSS", "JS", "PHP"];
    function get_data($name, $country = "Private", ...$skills) {
        echo "Hello $name Your Country Is $country <br>";
        foreach ($skills as $skill) :
            echo "-- $skill <br>";
        endforeach;
    }
    get_data("Osama", "Egypt", ...$group_of_skills);
    get_data("Osama", "Egypt", ...["HTML", "CSS", "JS", "PHP"]);


*/


/*
PHP Return Type Declarations:

    function addNumbers(float $a, float $b) : float {
        return $a + $b;
    }
    echo addNumbers(1.2, 5.2);
*/



/*
- Variable Function
    --- PHP Allow To Use Variable Like Function
    --- When You Append Parentheses () To Variable PHP Will Look For Function With That Name

    function one() {
        return "One From Function";
    }
    echo one();
    $func1 = "one";
    echo $func1();

    function say_hello_to($someone) {
        return "Hello $someone";
    }
    $func2 = "say_hello_to";
    echo $func2("Osama");


- Function Exists
    --- function_exists("Func Name")

    if (function_exists("testing")) {
        echo testing();
    } else {
        echo "Function Not Found";
    }

*/

/*
Array Map:

    function myfunction($v)
    {
        return($v*$v);
    }
    $a=array(1,2,3,4,5);
    print_r(array_map("myfunction",$a));

*/



/*
    - Anonymous Function
        --- When We Create A Function We Give It A Name So We Can Call It Later With That Name
        --- Sometimes We Need To Create A Function For Specific Task <= This Is Not Against DRY

    $say_hello = function() {
        return "Hello";
    };
    echo $say_hello();

    $say_hola = function($someone) {
        return "Hola $someone";
    };
    echo $say_hola("Osama");

    $msg = "Hi";
    $say_hi = function($someone) use ($msg) {
        return "$msg $someone";
    };
    echo $say_hi("Osama");
*/


/*
    - Arrow Function
        --- Short Syntax For Anonymous Function
        --- Automatic Use Variables From Parent Scope
    
    - Syntax
        --- Function Replaces With fn
        --- No Need For Curly Braces
        --- Return Is Omitted

    Arrow Function In Variable
        $say_hello = fn() => "Hello";
        echo $say_hello();

    Arrow Function With Parameter In Variable
        $say_hola = fn($someone) => "Hola $someone";
        echo $say_hola("Osama");

    Arrow Inherit Variable From Parent Scope Is Automatic
        $msg = "Hi";
        $say_hi = fn($someone) => "$msg $someone";
        echo $say_hi("Osama");

*/
