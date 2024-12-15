<?php

/*
Control Structure   :   Loop
*/

/*
    While:
-------------------------------------------
while ( condition ){
    code
    code
    -- Don't forget the increment or decrement
}

        while ( $x <= 10 ){
            echo $x . "<br>";
            $x++;
        }
-------------------------------------------
Alternate Syntax:

while ( condition ):
    code
    code
    -- Don't forget the increment or decrement
endwhile;
-------------------------------------------
*/


/*
Do While:
-------------------------------------------

do {
    code
    code
    -- Don't forget the increment or decrement
} while ( condition )
    
    do {
        echo $x . "<br>";
        $x++;
        } while ( $x <= 10 )

-------------------------------------------
*/





/*
    For Loop
-------------------------------------------

for (initialization; condition; increment) {
    code to be executed
}

for ($i = 1; $i <= 3; $i++) {
    echo "$i <br>";
    }
-------------------------------------------
Alternate Syntax:
    
    for (initialization; condition; increment) :
        code to be executed
    endfor;
        
*/





/*
    For each
-------------------------------------------

    foreach (iterable_expression as $value){
        statement
    }

    foreach (iterable_expression as $key => $value) {
        statement
    }

-------------------------------------------
Alternate Syntax:

    foreach (iterable_expression as $value):
        statement
    endforeach;

    foreach (iterable_expression as $key => $value) :
        statement
    endforeach;

*/




/*
Break : Ends Execution Of (For, Foreach, While, Do-while or Switch)
Continue : Skip Current Iteration
*/


/*
'Include' & 'Require' : used to include the contents of one PHP file into another PHP file.

The include and require statements are identical, except upon failure:
    require will produce a fatal error (E_COMPILE_ERROR) and stop the script
    include will only produce a warning (E_WARNING) and the script will continue

        include 'filename';
        include_once 'filename';

        require 'filename';
        require_once 'filename';


The require_once() statement is identical to require() except:
    PHP will check if the file has already been included, and if so, not include (require) it again.
*/

// $name = "Ali";