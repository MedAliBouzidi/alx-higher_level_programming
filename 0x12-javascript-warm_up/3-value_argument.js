#!/usr/bin/node
const argv = process.argv;
(argv[2] === undefined) ? console.log('No argument') : console.log(argv[2]);
