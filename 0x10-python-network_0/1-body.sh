#!/bin/bash
# display response body if status 200
curl -sfL "$1" -X GET
