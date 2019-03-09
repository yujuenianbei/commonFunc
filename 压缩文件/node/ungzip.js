var fs = require("fs");
var zlib = require('zlib');
const file = process.argv[2];
// 解压 input.txt.gz 文件为 input.txt
fs.createReadStream(file)
  .pipe(zlib.createGunzip())
  .pipe(fs.createWriteStream('1.txt'));
  
console.log("文件解压完成。");