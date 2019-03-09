var child_process = require('child_process');
var arg1 = 'songlist'
child_process.exec('python ./writecsv.py '+ arg1 ,function(error,stdout,stderr){
    if(stdout.length >1){
        console.log('you offer args:',stdout);
    } else {
        console.log('you don\'t offer args');
    }
    if(error) {
        console.info('stderr : '+stderr);
    }
});