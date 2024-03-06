#!/bin/bash

# Fetch public IP address using an external service
public_ip=$(curl -s https://api.ipify.org)

# Print the public IP address
echo $public_ip
