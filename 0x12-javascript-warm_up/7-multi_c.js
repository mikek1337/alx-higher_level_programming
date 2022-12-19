#!/usr/bin/node
const n = Math.floor(process.argv[2]);
if (isNaN(n)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < n) {
    console.log('C is fun');
    i++;
  }
}
