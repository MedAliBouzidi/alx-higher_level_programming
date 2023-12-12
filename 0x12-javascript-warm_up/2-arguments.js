#!/usr/bin/node
const argc = process.argv.length;
(argc === 2) ? console.log('No argument') : (argc === 3) ? console.log('Argument found') : console.log('Arguments found');
