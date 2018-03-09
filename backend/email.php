<?php
      if (isset($_POST["submit"])) {
      $to = $_POST['email'];
      $subject = "Password reset authentication";
      $txt = file_get_contents("sha256.txt");
      mail($to, $subject, $txt);
    }
?> 
