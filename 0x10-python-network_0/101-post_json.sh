#!/bin/bash
# Send json on post
curl -sL  -d @"$2" -H "Content-Type:application/json" "$1" -X POST
