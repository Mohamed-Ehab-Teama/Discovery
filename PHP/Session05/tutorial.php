<?php


/*
time()
Sessions
*/

// echo time();



//      Sessions

// Strat Session
// session_start();
// $_SESSION['name'] = 'value';
// echo $_SESSION['name'];
// print_r( $_SESSION );
// $_SESSION['name'] = 'new Value';

// Destroy a PHP Session
// remove all session variables
// session_unset();

// destroy the session
// session_destroy();


/*
Filters
*/

// filter_list()
/*
The filter_var() function both validate and sanitize data.
The filter_var() function filters a single variable with a specified filter. It takes two pieces of data:
    The variable you want to check
    The type of check to use

filter_var($bool, FILTER_VALIDATE_BOOL, FILTER_NULL_ON_FAILURE)
filter_var($url, FILTER_VALIDATE_URL, ["flags" => FILTER_NULL_ON_FAILURE | FILTER_FLAG_PATH_REQUIRED | FILTER_FLAG_QUERY_REQUIRED])
var_dump(filter_var( $int, FILTER_VALIDATE_INT, ["flags" => FILTER_NULL_ON_FAILURE, "options" => ["min_range" => 50, "max_range" => 100]] ));
*/

// filter_var($int, FILTER_VALIDATE_INT)
// filter_var($email, FILTER_VALIDATE_EMAIL)
// filter_var($email, FILTER_SANITIZE_EMAIL)
// filter_var($url, FILTER_VALIDATE_URL)
// filter_var($url, FILTER_SANITIZE_URL)
// filter_var($ip, FILTER_VALIDATE_IP)