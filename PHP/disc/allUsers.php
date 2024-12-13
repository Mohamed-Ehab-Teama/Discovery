<?php 

require_once 'connection.php';

$sql = " SELECT * FROM users ";
$result = mysqli_query( $connection, $sql );

?>




<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <title>Hello, world!</title>
</head>

<body>

    <div class="container mt-5">
        <table class="table">
            <thead>
                <tr>
                    <th scope="col"> ID </th>
                    <th scope="col"> Name </th>
                    <th scope="col"> Email </th>
                    <th scope="col"> Pass </th>
                </tr>
            </thead>
            <tbody>

                <?php
                    if ($result){
                        while ( $row = mysqli_fetch_assoc( $result ) ){
                ?>
                    <tr>
                        <th scope="row"> <?php echo $row['id']; ?> </th>
                        <td> <?php echo $row['name']; ?> </td>
                        <td> <?php echo $row['email']; ?> </td>
                        <td> <?php echo $row['password']; ?> </td>
                    </tr>
                <?php          
                        }
                    }
                ?>

            </tbody>
        </table>
    </div>




    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
</body>

</html>