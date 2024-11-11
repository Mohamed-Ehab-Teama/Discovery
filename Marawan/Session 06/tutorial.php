<!-- 
    The gettype() : returns the type of a variable as a string.
-->


<!-- 
Operators
    - Used To Perform Operations On Values.

    Arithmetic Operators
    - Used To Do Arithmetical Operations &#038; Conversion

    $a [+]  $b => Addition
    $a [-]  $b => Subtraction
    $a [*]  $b => Multiplication
    $a [/]  $b => Division
    $a [%]  $b => Modulus
    $a [**] $b => Exponentiation(power)

-->


<!-- 
Assignment Operators
    - Used To Write Value To Another

    $a [=]  $b => Assign value
    $a [+=]  $b => Addition
    $a [-=]  $b => Subtraction
    $a [*=]  $b => Multiplication
    $a [/=]  $b => Division
    $a [%=]  $b => Modulus
    $a [**=] $b => Exponentiation

-->


<!-- 
Comparison Operators
    - Used To Compare Two Values

    ==    => Equal
    !=    => Not Equal
    <>    => Not Equal
    ===   => Identical
    !==   => Not Identical

    >     => Larger Than
    >=    => Larger Than Or Equal
    <     => Smaller Than
    <=    => Smaller Than Or Equal
    <=>   => Spaceship [Less Than, Equal Or Greater]

-->


<!-- 
Incrementing & Decrementing Operators
    - Increase And Decrease Values
        
        $x++
        $x--
        $++x
        $--x

-->


<!-- 

Logical Operators
    - Compare Conditions

    and => And => Two Are True
    &&  => And => Two Are True
    or  => Or  => One Or Both Is True
    ||  => Or  => One Or Both Is True
    xor => Xor => One Is True But Not Both
    !   => Not => Not True

-->


<!-- 

Operators
    - Used To Perform Operations On Values.

    String Operators
        - Concatenate Strings

    $a = "Mohamed";
    $b = "Ehab";
    $c = "Teama";

    echo "$a $b $c";
    echo "{$a} {$b} {$c}";
    echo $a . " " . $b . " " . $c;
    echo "{$a} {$b} {$c} "  . " " ;

-->


<!-- 

Array Operators
    - Deal With Arrays

    +     => Union
    ==    => Equal => Same Key And Value
    !=    => Not Equal
    <>    => Not Equal
    ===   => Identical => Same Key And Value, Same Order, Same Type
    !==   => Not Identical


    $arr1 = [1 => "A", 2 => "B"];
    $arr2 = [3 => "C", 4 => "D"];
    $arr3 = $arr1 + $arr2;

    $arr4 = [1 => "10", 2 => "20"];
    $arr5 = [2 => 20, 1 => 10];

    var_dump($arr4 == $arr5);
    var_dump($arr4 != $arr5);
    var_dump($arr4 <> $arr5);

    var_dump($arr6 === $arr7);

-->

<!-- 

Error Control Operator
    - Control The Errors

    @

    $b = @$a;
    $b = @$a or die("Variable Not Found");

-->


<!-- 

Operator Precedence
    - "||" Has A Greater Precedence Than "or"
    - "&&" Has A Greater Precedence Than "and"

    $a = 10 || false;       =>      $a = (10 || false) => $a = 1
    $b = 10 or false;       =>      ($b = 10) or false

-->