const request = require('request');
const fs = require('fs');

// let url = process.argv[2];
let name = process.argv[2];
// const type = process.argv[4];

// 下载文件
downloadFile = (url, filename, callback) => {
    var stream = fs.createWriteStream("./img/"+filename);
    request(url)
        .pipe(stream)
        .on('close', callback);
}

for(var i = 500; i < 610; i++){
    for(var m = 1; m < 10; m++){
        downloadFile("https://mmtp1.com/jjtq/zipai/"+i+"/0"+m+".jpg", i+'-'+m+".jpg", function () {
            console.log( i+'-'+m+'下载完毕');
        });
    }

}



// 网易云歌曲，图片下载 传三个参数 URL 文件名称 文件类型
