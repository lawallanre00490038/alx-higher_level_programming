#!/bin/bash

# Take the URL as input argument
URL="$1"

# Use curl to send a request to the URL and get the size of the body in bytes
SIZE=$(curl -sI "$URL" | grep -i 'content-length' | awk '{print $2}')

# Display the size of the body in bytes
echo "$SIZE"
