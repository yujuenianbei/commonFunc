const request = require('request');
const fs = require('fs');

let url = process.argv[2];
let name = process.argv[3];
const urlSplit = url.split('.')
const type = urlSplit[urlSplit.length - 1]

// 下载文件
downloadFile = (uri, filename, callback) => {
    var stream = fs.createWriteStream(filename);
    request(uri)
        .pipe(stream)
        .on('close', callback);
}

// 判断下载文件类型
MineType = (type) => {
    if (type === 'mp3') {
        return '.mp3';
    } else if (type === 'mp4') {
        return '.mp4';
    } else if(type === 'jpg') {
        return '.jpg';
    } else if(type === 'png') {
        return '.png';
    }
}

const fileUrl = url;
const filename = name + MineType(type);

downloadFile(fileUrl, filename, function () {
    console.log(filename + '下载完毕');
});

// console.log(url, name, type, filename)