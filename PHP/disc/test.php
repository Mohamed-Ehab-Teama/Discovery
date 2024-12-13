<?php

require_once 'connection.php';

$sql = " SELECT * FROM users ";
$result = mysqli_query($connection, $sql);

?>


<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>

    <table>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Password</th>
        </tr>

        <?php
        if ($result) {
            while ($row = mysqli_fetch_assoc($result)) {
        ?>
                <tr>
                    <td> <?php echo $row['id']; ?> </td>
                    <td> <?php echo $row['name']; ?> </td>
                    <td> <?php echo $row['email']; ?> </td>
                    <td> <?php echo $row['password']; ?> </td>
                </tr>

        <?php
            }
        }
        ?>


    </table>

</body>

</html>