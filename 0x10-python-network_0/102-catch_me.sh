#!/bin/bash
#display response from server
curl -sL 0.0.0.0:5000/catch_me -X PUT -d 'user_id=98' -H "origin: HolbertonSchool"
