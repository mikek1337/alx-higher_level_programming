#!/usr/bin/node

class Rectangle {
    constructor (w, h) {
      if (w > 0 || h > 0) {
        this.width = w;
        this.height = h;
      }
    }
  
    print () {
      let i = 0;
  
      while (this.height > i) {
        let j = 0;
        while (this.width > j) {
          process.stdout.write('X');
          j++;
        }
        i++;
        console.log('');
      }
    }
    rotate () {
        let temp;
        temp = this.height;
        this.height = this.width;
        this.width = temp;
    }
    double () {
        this.width *=2;
        this.height *=2;
    }
  }
  
  module.exports = Rectangle;
  