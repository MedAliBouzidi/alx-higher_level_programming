#!/usr/bin/node
let argv = process.argv;
if (argv[2] === undefined) {
  console.log('No argument');
} else {
  argv = argv.slice(2);
  argv.forEach(arg => {
    console.log(arg);
  });
}
