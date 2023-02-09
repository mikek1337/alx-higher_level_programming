#!/usr/bin/node

const process = require('process');
const request = require('request');

const args = process.argv;

if (args.length > 2) {
  request.get('https://swapi-api.alx-tools.com/api/films/' + args[2], function (error, response, body) {
    if (!error) {
      const res = JSON.parse(body);
      console.log(res.title);
    } else {
      console.log(error);
    }
  });
}
