<?php include("top.html");?>
    <h3>Welcome <?php echo $_POST["name"]; ?></h3><br>
      <p> Thank you for giving us your feedback! Your feedback has been recorded as
        <em>"<?php echo $_POST["comment"];
        
                $myfile = fopen("data.txt", "a");
                $txt = $_POST["name"] . '::' . $_POST["comment"];
                fwrite($myfile, "$txt\n");
                fclose($myfile);
                ?>"
        </em>
      </p>
   </div>

</body>
</html>