#!/usr/bin/node
let loggedCount = 0;
exports.logMe = function (item) {
  console.log(`${loggedCount}: ${item}`);
  loggedCount++;
};
