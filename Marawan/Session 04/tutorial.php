<?php

// String : Sequence of characters

/*

echo 'Hello PHP';
echo '<br>';
echo "Hello PHP";
echo '<br>';

echo "Hello 'PHP'";
echo '<br>';
echo 'Hello "PHP"';
echo '<br>';

echo 'Hello \'PHP\'';
echo '<br>';
echo "Hello \"PHP\"";
echo '<br>';

echo "Hello PHP\";
echo "Hello PHP\\";
echo '<br>';

echo 'Hello PHP
  On Multiple
  Lines';

echo '<br>';

    nl2br() => Insert line breaks where newlines (\n) occur in the string
echo nl2br('Hello PHP
  On Multiple
  Lines');

*/


/*
    Single quotes vs Double quotes
        $name = "Hamo";
        echo "Hello, $name";
        echo 'Hello, $name';
*/



/*
Heredoc and Nowdoc

    Heredoc:

echo <<<"Here"
Hello PHP
Special Characters $$$ ' ' ' """"" \\\\
Hello My Name Is $name
Here;

echo <<<"ali"
Hello PHP
Special Characters $$$ ' ' ' """"" \\\\
Hello My Name Is $name
ali;

------------

        Nowdoc

echo <<<'Now'
Hello PHP
Special Characters $$$ ' ' ' """"" \\\\\\
Hello My Name Is $name
Now;

echo <<<'lol'
Hello PHP
Special Characters $$$ ' ' ' """"" \\\\\\
Hello My Name Is $name
lol;

------------

echo '<ul>';
    echo "<li>" . $name . "</li>";
    echo "<li>" . $name . "</li>";
    echo "<li>" . $name . "</li>";
    echo "<li>" . $name . "</li>";
echo '</ul>';

echo <<<"navlinks"
  <ul>
    <li>$name</li>
    <li>$name</li>
    <li>$name</li>
    <li>$name</li>
  </ul>
  navlinks;


  echo <<<'navlinks'
  <ul>
    <li>$name</li>
    <li>$name</li>
    <li>$name</li>
    <li>$name</li>
  </ul>
  navlinks;

*/


