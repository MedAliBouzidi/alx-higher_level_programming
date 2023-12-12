#!/usr/bin/node
const size = parseInt(process.argv[2]);
const square = [];

if (isNaN(size)) {
  console.log('Missing size');
}
for (let i = 0; i < size; i++) {
  for (let j = 0; j < size; j++) {
    square.push('X');
  }
  if (i != size - 1) {
    square.push('\n');
  }
}
console.log(square.join(''));
