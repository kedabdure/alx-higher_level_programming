#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const films = JSON.parse(body).results;
  let count = 0;

  for (const i in films) {
    const chars = films[i].characters;
    for (const j in chars) {
      const char = chars[j];
      if (char.includes(/18/)) {
        count++;
        break;
      }
    }
  }
  console.log(count);
});
