#!/bin/bash
# Send post request
curl -sd "email:test@gmail.com,subject:i will always be here for PLD" "$1" -X post
