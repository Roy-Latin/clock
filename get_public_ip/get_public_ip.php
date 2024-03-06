<?php

// Execute the Bash script to fetch the public IP address
$public_ip = shell_exec('/home/roy/app1/get_public_ip/get_public_ip.sh');

// Output the public IP address
echo $public_ip;

?>
