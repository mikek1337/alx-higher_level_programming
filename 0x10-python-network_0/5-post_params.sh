#!/bin/bash
# Send post request
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1" -X POST
