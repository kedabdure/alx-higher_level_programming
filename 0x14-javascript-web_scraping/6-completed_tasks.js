#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const tasks = JSON.parse(body);
    const completedTasksByUser = {};

    for (const i in tasks) {
      const task = tasks[i];
      if (task.completed) {
        if (completedTasksByUser[task.userId] === undefined) {
          completedTasksByUser[task.userId] = 1;
        } else {
          completedTasksByUser[task.userId]++;
        }
      }
    }
    console.log(completedTasksByUser);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
