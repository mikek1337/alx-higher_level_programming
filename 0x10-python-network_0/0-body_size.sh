#!/bin/bash
# displays size of a site using curl
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
