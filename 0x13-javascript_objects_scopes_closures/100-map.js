#!/usr/bin/node
const oldList = Array.from(require('./100-data.js').list);
const newList = oldList.map((element, index) => element * index);

console.log(oldList);
console.log(newList);
