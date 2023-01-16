#!/bin/bash
# Display all methods the server accepts
curl -sI "$1" | grep -i Allow | sed 's/Allow: //g'
