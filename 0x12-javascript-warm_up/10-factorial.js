#!/usr/bin/node
const n = Math.floor(process.argv[2]);
console.log(factorial(n));
function factorial (n) {
  if (n === 1) {
    return 1;
  }
  if (n === 0){
      return 0;
  }  
  return n * factorial(n - 1);
}
