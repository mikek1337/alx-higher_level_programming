#!/bin/bash
# Show status code
curl -w '%{http_code}' -s "$1" -o /dev/null
