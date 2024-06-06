#!/usr/bin/node

const request = require('request');

const darkvadorID = process.argv[2];

const url = `https://swapi-api.hbtn.io/api/films/${darkvadorID}`;

request(url, async (err, res, body) => {
  err && console.log(err);

  const charArray = (JSON.parse(res.body).characters);
  for (const character of charArray) {
    await new Promise((resolve, reject) => {
      request(character, (err, res, body) => {
        err && console.log(err);

        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});