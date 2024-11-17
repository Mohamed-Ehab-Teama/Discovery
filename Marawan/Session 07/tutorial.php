<!-- 
Control Structure:
    if
            if ( condition )
            {
                // code
            }
-----------------------------------------------------
    if-else
            if ( condition )
            {
                // code
            }else
            {
                // code
            }
-----------------------------------------------------
    if-elseif-else
            if ( condition )
            {
                // code
            }elseif ( condition )
            {
                // code
            }
            else{
                // code
            }
-----------------------------------------------------

$page = "About";
if ($page == "About") {
    echo "This Is The Page";
}
-----------------------------------------------------

$title = "";
if ($title == "") {
    echo "Unknown Page";
} else {
    echo $title;
}
-----------------------------------------------------

$lang = "Arabic";
if ($lang == "Arabic") {
    echo 'مرحبا';
} elseif ($lang == "English") {
    echo 'Hello';
} elseif ($lang == "Spanish") {
    echo 'Hola';
} else {
    echo 'Unknown Language';
}

-->

<!-- ---------------------------------------------------------------------- -->

<!-- 

if (10 > 10)            No paranthes cause it's a single line of code in each block
    echo "Good";
else
    echo "Bad";

-->

<!-- ---------------------------------------------------------------------- -->

<!-- 
    If, Elseif, Else ( Alternate Syntax  ):

        if (condition) :
            // code
            // code
        endif;
    ---------------------------
        if ( condition ) :
            // code
        else:
            // code
        endif;
    ---------------------------
        if ( condition ) :
            // code
        elseif ( condition ) :
            // code
        else:
            // code
        endif;
    ---------------------------

-->

<!-- ---------------------------------------------------------------------- -->

<!-- 
    Nested-if   =>  means that : if statement inside if statement
       
    EX)

        if ( $password )
        {
            if ( $password_length < 6 )
            {
                if ( $password_length > 20 )
                {
                    echo " password is ready to be stored ";
                }else
                {
                    echo " password length cannot be more than 20 characters ";
                }
            }else
            {
                echo " password length cannot be less than 6 characters ";
            }            
        }else
        {
            echo " password cannot be empty ";
        }

-->

<!-- ---------------------------------------------------------------------- -->

<!-- 

    Ternary Operator     =>     Short If    =>      Condition ? True : False;

    EX)

        echo $a > 8 ? "Good" : "Bad";
        $result = $a > 8 ? "Good" : "Bad";

-->

<!-- ---------------------------------------------------------------------- -->

<!-- 

    Switch

    switch (expression) {
        Case 1:
            // Code Block 1
            break;
            Case 2:
        // Code Block 2
            break;
        Case 3:
            // Code Block 3
            break;
        Default:
            // Default Code Block
    }


    Ex)

        $favcolor = "red";
        switch ($favcolor) {
            case "red":
                echo "Your favorite color is red!";
                break;
            case "blue":
                echo "Your favorite color is blue!";
                break;
            case "green":
                echo "Your favorite color is green!";
                break;
            default:
                echo "Your favorite color is neither red, blue, nor green!";
        }


        switch($day) {
            case "Sat":
                echo "Hello Today Is $day We Are Open From 10:16";
                break;
            case "Sun":
                echo "Hello Today Is $day We Are Open From 12:18";
                break;
            case "Mon":
            case "Thu":
                echo "Hello Today Is $day We Are Open From 08:12";
                break;
            default:
                echo "Unknown Day";
        }
-->