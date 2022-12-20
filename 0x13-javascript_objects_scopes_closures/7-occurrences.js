#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const listLen = list.length;
  let i = 0;
  let count = 0;
  while (i < listLen) {
    if (list[i] === searchElement) { count++; }
    i++;
  }
  return count;
};
