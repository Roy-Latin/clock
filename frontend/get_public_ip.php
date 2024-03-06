<?php

// Execute the Bash script to fetch the public IP address
$public_ip = shell_exec('./get_public_ip.sh');

// Output the public IP address
echo $public_ip;

?>
