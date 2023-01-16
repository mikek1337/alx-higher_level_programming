#!/bin/bash
# Show status code
curl -w '%{http_code}' -s "$1"
