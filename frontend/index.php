<html>
<head>
    <title>Leaderboard | ReUniversity</title>
    <link rel="stylesheet" type="text/css" href="stylesheet.css"  />
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700" rel="stylesheet">
    <link rel="icon" href="icon.png">
    <meta http-equiv="refresh" content="5"/>
</head>

<body>
    <header class="header">
        <h1 class="header--title"><span class="title--weak">
            Reduce.</span> <span class="title--re">Re</span>University. <span class="title--weak">Recycle.</span>
        </h1>
        <div class="header--separator"></div>
        <p class="header--tagline">
            Working together for a cleaner world.
        </p>
    </header>
    <div class="leaderboard-wrapper">
        <h1 class="leaderboard-title">Leaderboard</h1>
        <div class="leaderboard-location-wrapper">
            <h2 class="leaderboard-location">
                Showing results for: <span class="leaderboard-location--specific">UMD Campus</span>
            </h2>
        </div>
        <table class="leaderboard">
            <tr class="leaderboard__header">
                <td>Position</td>
                <td>Recycling Bin</td>
                <td>Items Recycled</td>
                <!--<td>Map</td>-->
            </tr>
            <?php
            include("backend/php/db_header.php");
            $conn = new mysqli($server, $username, $password, $dbname);
            if($conn->connect_error) {
              echo "<tr class=\"leaderboard__item\"><td colspan=\"4\">Failed to connect to database</td></tr>";
            }
            else {
              $sql = "SELECT * FROM Trashcan ORDER BY current_value DESC";
              $result = $conn->query($sql);
              if(!$result) {
                echo "<tr class=\"leaderboard__item\"><td colspan=\"4\">The table is empty</td></tr>";
              }
              else {
                for ($i = 1; ;$i++) {
                  if(!$row = $result->fetch_assoc()) {
                    break;
                  }
                  echo "<tr class=\"leaderboard__item\"><td>#" . $i . "</td>";
                  echo "<td>" . $row["nickname"] . "</td>";
                  echo "<td>" . $row["current_value"] . "</td></tr>";
                  //echo "<td><a class=\"map-link-row\" href=\"#\">Map</a></td></tr>";
                }
              }
            }
            ?>
            <!--
            <tr class="leaderboard__item">
                <td>1</td>
                <td>Caroline Hall 1101-1110</td>
                <td>5,302</td>
                <td><a href="#">Map</a></td>
            </tr>
            LOLWUT -->
        </table>
    </div>
    <div id="map"></div>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDB9WLFiXheQKCmVR6wPyu9Jx5TuAeAPP0&libraries=visualization&callback=initMap" async defer></script>
</body>
</html>
