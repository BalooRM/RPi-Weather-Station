<?php
echo "<pre>\n";
$output = passthru('tail -n 24 /home/pi/weather/weatherweb.log');
$output = passthru('python /home/pi/weather/readplot2.py < /home/pi/weather/weatherweb.log');
echo "</pre>\n";
echo "<img src=\"./image/24hours.png\" >";
//phpinfo();
?>