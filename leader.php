<!DOCTYPE html>
<html lang="en">
    <head>
        
        <title>Sushi Go LeaderBoard</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="main.css" >

    </head>
    <body>

        <ul>
            <li><a class="active" href="welcome.html">Home</a></li>
            <li><a href="contact.html">Contact</a></li>
            <li><a href="rules.html">How To Play</a></li>
        </ul>

        <div class="logo">
                <img src="Images/sushi_go_logo.png">
        </div>
        
        <div class="header"> 
            <h1>LeaderBoard</h1>
        </div>

<?php
    $con = mysqli_connect('cs1.ucc.ie','jp11','rahquahv','2019_jp11');
    if (!$con) {
        die('Could not connect: ' . mysqli_error($con));
    }
    mysqli_select_db($con,"GameStats");
    $sql="SELECT * FROM GameStats
    ORDER By TopScore DESC
    Limit 10";
    $result = mysqli_query($con,$sql);
    echo "<table>
    <tr>
    <th>PlayerID</th>
    <th>PlayerName</th>
    <th>GamesWon</th>
    <th>TopScore</th>
    </tr>";
    while($row = mysqli_fetch_array($result)) {
        echo "<tr>";
        echo "<td>" . $row['PlayerID'] . "</td>";
        echo "<td>" . $row['PlayerName'] . "</td>";
        echo "<td>" . $row['GamesWon'] . "</td>";
        echo "<td>" . $row['TopScore'] . "</td>";
        echo "</tr>";
    }
    echo "</table>";
    mysqli_close($con);
?>

    </body>
</html>
