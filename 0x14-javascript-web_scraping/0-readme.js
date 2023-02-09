#!/snap/bin/node
const process = require('process');
const fs = require('fs');
const args = process.argv;

if (args.length > 2) {
  fs.readFile(args[2], function (err, data) {
    if (err == null) { console.log('' + data); } else { console.log(err); }
  });
}
