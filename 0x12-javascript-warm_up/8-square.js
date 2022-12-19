#!/usr/bin/node
const n = Math.floor(process.argv[2]);
if (isNaN(n)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < n) {
    let j = 0;
    while (j < n) {
      process.stdout.write('X');
      j++;
    }
    console.log('');
    i++;
  }
}
