<?php

/*
Date
include - require - include_once - require_once
files:
    readfile()
    fopen()


SuperGlobals:
    $GLOBALS    $_SERVER    $_REQUEST   $_POST   $_GET    $_FILES    $_ENV    $_COOKIE    $_SESSION

    $GLOBALS is an array that contains all global variables
    $_SERVER is a PHP super global variable which holds information about headers, paths, and script locations
    $_REQUEST is a PHP super global variable which contains submitted form data, and all cookie data
    $_POST contains an array of variables received via the HTTP POST method
    $_GET contains an array of variables received via the HTTP GET method.
*/


/*
date(format, timestamp)
    format :
        Y m d l(day of week)  H h i s a(am or pm)
date_default_timezone_set("America/New_York")
date_default_timezone_get()
*/