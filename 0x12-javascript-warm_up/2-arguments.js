#!/usr/bin/node
const argc = process.argv.length;
(argc === 2) ? console.log('No Argument') : (argc === 3) ? console.log('Argument found') : console.log('Arguments found');
