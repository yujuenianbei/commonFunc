// Import the package main module
const csv = require('fast-csv')
const fs = require('fs')
var csvStream = csv.createWriteStream({headers: true}),
    writableStream = fs.createWriteStream("my.csv");
 
writableStream.on("finish", function(){
  console.log("DONE!");
});
 
csvStream.pipe(writableStream);
csvStream.write({a: "a0", b: "b0"});
csvStream.write({a: "a1", b: "b1"});
csvStream.write({a: "a2", b: "b2"});
csvStream.write({a: "a3", b: "b4"});
csvStream.write({a: "a3", b: "b4"});
csvStream.end();


// var csvStream = csv
//     .createWriteStream({headers: true})
//     .transform(function(row, next){
//         setImmediate(function(){
//             next(null, {A: row.a, B: row.b});
//         });;
//     }),
//     writableStream = fs.createWriteStream("my.csv");
 
// writableStream.on("finish", function(){
//   console.log("DONE!");
// });
 
// csvStream.pipe(writableStream);
// csvStream.write({a: "a0", b: "b0"});
// csvStream.write({a: "a1", b: "b1"});
// csvStream.write({a: "a2", b: "b2"});
// csvStream.write({a: "a3", b: "b4"});
// csvStream.write({a: "a3", b: "b4"});
// csvStream.end();