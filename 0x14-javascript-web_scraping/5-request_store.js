#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileUrl = process.argv[3];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(fileUrl, body, function (err) {
      if (err) { console.log(err); }
    });
  }
});
