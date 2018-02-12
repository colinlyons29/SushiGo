<!DOCTYPE html>
<html lang="en">
<head>
  <title>Sushi Go LeaderBoard</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
   <link href="main.css" rel="stylesheet">
  <style>

table {
    width: 100%;
    border-collapse: collapse;
}

table, td, th {
    border: 1px solid black;
    padding: 5px;
}

th {text-align: left;}
</style>

</head>
<body>

<nav class="navbar navbar-inverse">
  <div class="container-fluid">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>                        
      </button>
      <a class="navbar-brand" href="#"></a>
    </div>
    <div class="collapse navbar-collapse" id="myNavbar">
      <ul class="nav navbar-nav">
        <li class="active"><a href="#">Home</a></li>
        <li><a href="#">About</a></li>
      </ul>
      <ul class="nav navbar-nav navbar-right">
        <li><a href="#"><span class="glyphicon glyphicon-log-in"></span> Login</a></li>
      </ul>
    </div>
  </div>
</nav>
  
<div class="container-fluid text-center">    
  <div class="row content">
    <div class="col-sm-2 sidenav">
    </div>
    <div class="col-sm-8 text-left"> 
      <h1>LeaderBoard</h1>
<?php

$con = mysqli_connect('cs1.ucc.ie','apc1','aezihiep','2018_apc1');
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
    </div>
    <div class="col-sm-2 sidenav">

    </div>
  </div>
</div>

<footer class="container-fluid text-center">
  <p>Sushi Go</p>
</footer>

</body>
</html>