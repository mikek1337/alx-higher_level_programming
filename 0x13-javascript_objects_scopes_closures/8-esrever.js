#!/usr/bin/node

exports.esrever = function (list) {
  const revList = [];
  let len = list.length - 1;
  while (len >= 0) {
    revList.push(list[len]);
    len--;
  }
  return revList;
};
