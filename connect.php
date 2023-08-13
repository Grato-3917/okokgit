
<?php

// Retrieve form data
$name = $_POST['name'];
$email = $_POST['email'];

// Connect to the database
$host = "localhost";
$username = "root";
$password = "Chinu@2004";
$dbname = "statuscode0";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Insert data into the database
$sql = "INSERT INTO users (name, email) VALUES ('$name', '$email')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
