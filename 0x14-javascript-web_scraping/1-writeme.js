#!/usr/bin/node
const process = require('process');
const fs = require('fs');
const args = process.argv;

if (args.length > 2) {
  fs.writeFile(args[2], args[3], function (err) {
    if (err) { console.log(err); }
  });
}
