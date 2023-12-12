#!/usr/bin/node
const number = parseInt(process.argv[2]);
if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < number; index++) {
    console.log('C is fun');
  }
}
