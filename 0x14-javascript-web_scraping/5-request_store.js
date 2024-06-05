#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filepath = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const content = body;

  fs.writeFile(filepath, content, 'utf-8', (error) => {
    if (error) {
      console.error('Error: ', error);
    }
  });
});
