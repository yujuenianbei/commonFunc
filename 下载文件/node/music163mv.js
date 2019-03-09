const request = require('request');
const fs = require('fs');

let url = process.argv[2];
let name = process.argv[3];
const type = process.argv[4];

// 下载文件
downloadFile = (url, filename, callback) => {
    var stream = fs.createWriteStream("./file/"+filename);
    request(url)
        .pipe(stream)
        .on('close', callback);
}

// 判断下载文件类型
MineType = (type) => {
    if (type === 'mp3') {
        return '.mp3';
    } else if (type === 'mp3') {
        return '.mp4';
    } else if(type === 'jpg') {
        return '.jpg';
    } else if(type === 'png') {
        return '.png';
    }
}

const fileUrl = url;
const filename = name + "." + type;

downloadFile(fileUrl, filename, function () {
    console.log(filename + '下载完毕');
});

// 网易云歌曲，图片下载 传三个参数 URL 文件名称 文件类型
