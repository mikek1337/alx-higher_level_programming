#!/usr/bin/node
const a = Math.floor(process.argv[2]);
const b = Math.floor(process.argv[3]);
add(a, b);
function add (a, b) {
  console.log(a + b);
}
