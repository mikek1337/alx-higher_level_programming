#!/usr/bin/bash
# displays size of a site using curl
curl -w '%{size_download}' -s --output /dev/null --no-progress-meter -N "$1"