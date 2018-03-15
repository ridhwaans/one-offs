#! /usr/bin/env node

var google = require('google')
var prompt = require('prompt');
var Promise = require('bluebird');

Promise.promisifyAll(prompt);

// Ask the user what to google seach for (start is synchronous)
console.log('Google Search')
prompt.start(); 

prompt.getAsync(['input']).then(function(response) {
    console.log('Searching for \'' + response.input + '\'...'); // Attempt google search
    google(response.input, function (err, res){
      if (err) console.error(err)

      if(res.links.length > 0){   
        var link = res.links[0];
        console.log('(Google Search) 1st result:')
        console.log('(Title): ' + link.title + ' (Url): ' + link.href)
      }else{
        console.log('Nothing found')
      }

    })  
});