#!/usr/bin/node
const argv = process.argv;
const number = parseInt(argv[2]);
isNaN(number) ? console.log('Not a number') : console.log(`My number: ${number}`);
