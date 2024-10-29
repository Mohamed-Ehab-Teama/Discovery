<?php /* Dealing with forms */ ?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> Session 06 - Login </title>
    <style>
        .cen{
            margin-top: 50px;
        }
        form{
            border: silver 1px double;
            width: 50%;
            padding: 10px;
        }
        *{
            margin: 5px;
        }
    </style>
</head>
<body>
    

    <center class="cen">

    <h1> Login Form </h1>

        <form action="handle1.php" method="post" >

            <label for="">Name</label>
            <br>
            <input type="text" name="user_name" >
            <br>

            <label for="">Email</label>
            <br>
            <input type="email" name="user_email">
            <br>

            <label for="">Password</label>
            <br>
            <input type="password" name="password">
            <br>

            <input type="submit">
            <input type="reset">

        </form>

    </center>

</body>
</html>