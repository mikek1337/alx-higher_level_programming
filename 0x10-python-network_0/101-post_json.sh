#!/bin/bash
# Send json on post
curl -sd "$2" -H "Content-Type:application/json" "$1" -X POST
 