#!/usr/bin/node

const list = process.argv.map(Number);
const subarray = list.slice(2, list.length);
const sortedList = subarray.sort((a, b) => a - b);
console.log(sortedList[sortedList.length - 2]);
