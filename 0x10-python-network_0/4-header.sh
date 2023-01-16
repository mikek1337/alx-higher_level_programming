#!/bin/bash
# Adds header to request
curl -sH X-School-User-Id=98 "$1" -X GET
