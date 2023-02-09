#!/usr/bin/node

const process = require('process');
const request = require('request');

const args = process.argv;

if (args.length > 2) {
  request.get(args[2], function (error, response, request) {
    if (!error) { console.log('code: ' + response.statusCode); } else { console.log(error); }
  });
}
