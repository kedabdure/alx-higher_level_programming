#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  console.log(response.statusCode);
});
