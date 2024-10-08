#!/usr/bin/node
const request = require('request');

if (process.argv.length === 2) {
  console.log('Usage: argument must be greater than two');
  process.exit(1);
}

const url = 'https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);

// for each movie url, find their character name
async function charactersName () {
  const response = await myPromise(url);
  const charactersUrls = JSON.parse(response).characters;
  for (const characterUrl of charactersUrls) {
    try {
      const response = await myPromise(characterUrl);
      const characterName = JSON.parse(response).name;
      console.log(characterName);
    } catch (error) {
      console.error(`Error fetching data from ${characterUrl}`);
    }
  }
}

// return a promise that is to be awaited
function myPromise (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        // resolve(response.body)
        resolve(body);
      }
    });
  });
}

charactersName();
