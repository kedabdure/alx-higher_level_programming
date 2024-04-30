#!/usr/bin/node
const value = process.argv[2];
const num = Math.floor(Number(value));

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let result = '';
    for (let j = 0; j < num; j++) {
      result += 'X';
    }
    console.log(result);
  }
}
