#!/usr/bin/node

const request = require('request');
const urlMovie = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(urlMovie, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }

  const film = JSON.parse(body);
  const characterPromises = film.characters.map(url => fetchCharacter(url));

  Promise.all(characterPromises)
    .then(characters => {
      characters.forEach(character => {
        console.log(character.name);
      });
    })
    .catch(error => {
      console.error('Error fetching character data:', error);
    });
});

function fetchCharacter(url) {
  return new Promise((resolve, reject) => {
    request(url, function (error, response, body) {
      if (error) {
        reject(error);
        return;
      }
      resolve(JSON.parse(body));
    });
  });
}
