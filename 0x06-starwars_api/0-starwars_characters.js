#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2] + '/';
const swapiURL = 'https://swapi-api.alx-tools.com/api/films/';

// Makes API request, sets async to allow await promise
request(swapiURL + movieID, async function (error, response, body) {
  if (error) return console.error(error);

  // find URLs of each character in the film as a list obj
  const charURLList = JSON.parse(body).characters;

  // Use URL list to character pages to make new requests
  // await queues requests until they resolve in order
  for (const charURL of charURLList) {
    await new Promise(function (resolve, reject) {
      request(charURL, function (error, response, body) {
        if (error) return console.error(errot);

        // finds each character name and prints in URL order
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
