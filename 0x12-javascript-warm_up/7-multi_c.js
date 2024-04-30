#!/usr/bin/node
const value = process.argv[2];
const num = Math.floor(Number(value));

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
