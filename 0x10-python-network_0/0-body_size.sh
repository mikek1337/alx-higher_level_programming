#!/usr/bin/bash
# displays size of a site using curl

curl -w '%{size_download}' --silent --output /dev/null --no-progress-meter -N "$1"