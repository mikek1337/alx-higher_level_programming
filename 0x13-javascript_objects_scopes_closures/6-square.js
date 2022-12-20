#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let i = 0;

    if (c === undefined) {
      this.print();
    } else {
      while (this.height > i) {
        let j = 0;
        while (this.width > j) {
          process.stdout.write(c);
          j++;
        }
        console.log('');
        i++;
      }
    }
  }
}
module.exports = Square;
