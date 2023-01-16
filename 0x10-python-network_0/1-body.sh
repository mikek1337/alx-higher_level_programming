#!/bin/bash
# display response body if status 200
curl -w ' %{http_code}'  0.0.0.0:5000/route_1 -s -L | grep 200 | sed 's/200/ /g'
  