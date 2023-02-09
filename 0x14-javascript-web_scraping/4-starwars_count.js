#!/usr/bin/node

const process = require('process');
const request = require('request');

const args = process.argv;

if (args.length > 2) {
  request.get(args[2], function (error, response, body) {
    if (!error) {
      const films = JSON.parse(body).results;
      let count = 0;
      for (const filmIndex in films) {
        const filmChars = films[filmIndex].characters;
        for (const charIndex in filmChars) {
          if (filmChars[charIndex].includes('18')) {
            count++;
          }
        }
      }
      console.log(count);
    } else {
      console.log(error);
    }
  });
}
