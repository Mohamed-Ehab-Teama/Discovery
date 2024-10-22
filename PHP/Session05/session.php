<?php

// echo "<pre>";
// print_r(filter_list());
// echo "</pre>";

$str =  "moha\\\\\\\\\\\\\5____\"\"med  @a.a";
echo filter_var($str, FILTER_VALIDATE_EMAIL);

echo "<hr>";

echo filter_var($str, FILTER_SANITIZE_EMAIL);