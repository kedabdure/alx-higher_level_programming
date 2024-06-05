#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + filmId;

request(url, function (error, response, body) {
  if (error) {
    console.error('Error fetching film data:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch film data. Status code:', response.statusCode);
    return;
  }

  const characters = JSON.parse(body).characters;

  characters.forEach((character) => {
    request(character, function (error, response, body) {
      if (error) {
        console.error('Error fetching character data:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error('Failed to fetch character data. Status code:', response.statusCode);
        return;
      }

      console.log(JSON.parse(body).name);
    });
  });
});
