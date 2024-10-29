<!-- 
Data Types :
    = bool  => Boolean:
        True, False
    = int   => Integer:
        10, 20, 30 
    = float => Floating Point Number | double :
        10.2 , 50.1
    = string :
        "Ali" , 'Mohamed'
    = array :
        [10,20,30]
        [ 1 => 'Ahmed', 2 => 'Mohamed' ]
    = gettype() => return the datatype
        echo gettype(0);


Type Juggling + Automatic Type Conversion :
    echo 1 + "2"; // 3
    echo gettype(1 + "2");      // Integer

    echo True + True; // 2
    echo gettype(True + True);  // Integer

    echo 5 + '5 Lessons'; // 10 => Warning
    echo gettype(5 + '5 Lessons'); // Integer => Warning

    echo 10 + 15.5; // 25.5
    echo gettype(10 + 15.5); // double => Float


Type Casting :
    echo 5 + (int) "5 Lessons";
    echo 5 + (integer) "5 Lessons";
    echo 5 + ( integer ) "5 Lessons";

    echo gettype(5 + (int) "5 Lessons");

    echo 10 + 15.5;
    echo 10 + (int) 15.5;
    echo gettype(10 + (int) 15.5);

    echo 10.5 + 10.5;
    echo gettype(10.5 + 10.5);
    echo (int) 10.5 + (int) 10.5; // 20
    echo gettype((int) 10.5 + (int) 10.5);
    echo (int) (10.5 + 10.5); // 21


Boolean + Converting To Boolean

    False:
        var_dump((bool) "");
        var_dump((bool) array());
        var_dump((bool) []);
        var_dump((bool) 0);
        var_dump((bool) "0");
    True:
        var_dump((bool) "Elzero");
        var_dump((bool) array(1));
        var_dump((bool) [1]);
        var_dump((bool) 100);
        var_dump((bool) -100);
        var_dump((bool) 10.5);
        var_dump((bool) -10.5);



-->