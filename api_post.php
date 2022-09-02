<?php
$servername = "localhost";
$dbname = "meteraninfo";
$username = "root";
$password = "";

$reading_value =  $created_at =  $prediction_score =  $status =  $img = "";

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $reading_value      = test_input($_POST["reading_value"]);
    $created_at         = test_input($_POST["created_at"]);
    $prediction_score   = test_input($_POST["prediction_score"]);
    $status             = test_input($_POST["status"]);
    $img                = test_input($_POST["img"]);

    $conn = new mysqli($servername, $username, $password, $dbname, 3306);
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    $sql = "INSERT INTO meteraninfo (
        reading_value, 
        created_at,
        prediction_score,
        stat,
        img) VALUES (
            '" . $reading_value . "',
            '" . $created_at . "',
            '" . $prediction_score . "',
            '" . $img . "')";

    if ($conn->query($sql) === TRUE) {
        echo "New record created successfully";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
    
}

function test_input($data)
{
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}
?>