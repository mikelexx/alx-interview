#!/usr/bin/node

const process = require('process');
const request = require('request');
const movieId = process.argv[2];

function requestFilmCharacterUrls (filmUrl) {
  return new Promise((resolve, reject) => {
    request.get(filmUrl, { json: true }, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(body.characters);
      }
    });
  });
}

function requestCharacterName (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, { json: true }, (err, _, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(body.name);
      }
    });
  });
}

async function getStarWarsMovieCharacters (filmUrl) {
  const charactersUrls = await requestFilmCharacterUrls(filmUrl);
  const charNames = await Promise.all(charactersUrls.map(characterUrl => requestCharacterName(characterUrl)));
  return charNames;
}

const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

getStarWarsMovieCharacters(filmUrl)
  .then(charNames => {
    charNames.forEach(charName => console.log(charName));
  })
  .catch(err => console.log(err));
