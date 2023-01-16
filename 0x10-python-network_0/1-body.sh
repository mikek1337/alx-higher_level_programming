#!/bin/bash
# display response body if status 200
curl -w ' %{http_code}' "$1" -s -L | grep 200 | sed 's/200/ /g'
