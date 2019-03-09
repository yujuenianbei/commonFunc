const mysql = require('mysql');
const fs = require('fs')
const csv = require('fast-csv')
const poolConfigData={
    host: 'localhost',
    port: '3306',
    user: 'root',
    password: '492275105',
    database: 'antd',
    connectTimeout: 10000,
}
const poolConfig = {
    host: poolConfigData.host,
    port: poolConfigData.port,
    user: poolConfigData.user,
    password: poolConfigData.password,
    database: poolConfigData.database,
    connectTimeout: 10000,
    multipleStatements: true,
};
pool = mysql.createPool(poolConfig);

const query = (sql, param, callback = () => { }, useTransaction) =>
    new Promise((resolve, reject) => {
        if (!pool) {
            callback('mysql pool not exist!', null, null);
            reject('mysql pool not exist!');
        } else {
            pool.getConnection((err, conn) => {
                if (err) {
                    callback(err, null, null);
                    reject(err);
                } else {
                    if (useTransaction) {
                        conn.beginTransaction(err => {
                            if (err) {
                                callback(err, null, null);
                                reject(err);
                            } else {
                                conn.query(sql, param, (qerr, vals, fields) => {
                                    // 释放连接
                                    if (qerr) {
                                        conn.rollback(() => console.log('excute sql error, rollback'));
                                        conn.release();
                                        callback(qerr, vals, fields);
                                        reject(qerr);
                                        return;
                                    }
                                    conn.commit(err => {
                                        if (err) {
                                            console.log('commit sql error');
                                            console.log(err);
                                            reject(err);
                                        }
                                    });
                                    conn.release();
                                    callback(qerr, vals, fields);
                                    resolve(vals);
                                    return;
                                });
                            }
                        });
                    } else {
                        conn.query(sql, param, (qerr, vals, fields) => {
                            conn.release();
                            callback(qerr, vals, fields);
                            if (qerr) {
                                reject(qerr);
                            } else {
                                resolve(vals);
                            }
                        });
                    }
                }
            });
        }
    });

let title = [];
let data = [];
let dataindex = 0;
const datatable1 = 'songlist'
query(`select * from ${datatable1}`, [], (error, results, fields) => {
    results.forEach((currentValue, index, arr) => {
        data.push(currentValue);
        dataindex = index + 1;
    })
    // 创建数据流并生成文件
    var csvStream = csv.createWriteStream({ headers: true }),
        writableStream = fs.createWriteStream(poolConfigData.database+'-'+datatable1+".csv");
    writableStream.on("finish", function () {
        console.log("DONE!");
    });
    csvStream.pipe(writableStream);
    // 将数据写入数据流中
    data.forEach((currentValue, index, arr)=>{
        csvStream.write(currentValue);
    })
    csvStream.end();
});