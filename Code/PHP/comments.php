<?php include("top.html");?>
  <ul class="media-list">
      
      <?php 
          $fn = fopen("data.txt","r");
          while(! feof($fn))  {
                $line = fgets($fn);
                if ($line == "") continue;
                $line_array = explode("::", $line); 
                echo "<li class=\"media\">
                          <div class=\"media-body\">
                            <strong class=\"text-success\">@$line_array[0]</strong>
                            <p>$line_array[1]</p>
                          </div>
                      </li>";
          }
        
          fclose($fn); 
       ?>
  </ul>
 </body>
</html>