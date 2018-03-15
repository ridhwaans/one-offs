#! /usr/bin/env node

var fs = require('fs');

function readFile(file) {
  var text = fs.readFileSync(file, "utf-8");
  var arr = text.replace(/\r\n/g,'\n').split("\n")
  // exclude lines which are blank or whitespace
  arr = arr.filter(function(str) {
      return /\S/.test(str);
  });
  return arr
}

/**
 * @param {array} arr2 (of string patterns)
 * @param {integer} mode (modes 1,2, or 3)
 * Mode 1: output all the lines from input.txt that match exactly any pattern in patterns.txt
 * Mode 2: output all the lines from input.txt that contain a match from patterns.txt somewhere in the line.
 * Mode 3: output all the lines from input.txt that contain a match with edit distance <= 1 patterns.txt
 * @return {array} list of matches found
 */
Array.prototype.diff = function(arr2, mode) {
    var ret = [];
    
    switch(mode) {
      case 1:
          // (required) mode 1 logic
          for(var i in this) {   
            if(arr2.indexOf( this[i] ) > -1){
              ret.push( this[i] );
            }
          }
          break;
      case 2:
          // (optional) mode 2 logic
          for(var i in arr2) {
            let found = this.filter(li => li.indexOf(arr2[i]) > -1);
            ret.push( found );
          }
          break;
      case 3:
          // (optional) mode 3 logic
          break;
      default:
          break;
    }
    return ret;
};

function printElements(arr){
  for (i = 0; i < arr.length; i++)
  {
    console.log(arr[i]);
  }
}

var input = readFile("./input.txt")
var patterns = readFile("./patterns.txt")

console.log( 'input.txt:');
printElements(input);
console.log( '\npatterns.txt:');
printElements(patterns);


console.log( '\nMode 1 results:');
printElements( input.diff(patterns, 1) );

console.log( '\nMode 2 results:');
printElements( input.diff(patterns, 2) );