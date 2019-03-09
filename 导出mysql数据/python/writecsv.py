#!/usr/bin/python3

import pymysql
import csv
import sys


# 打开数据库连接
db = pymysql.connect("localhost", "root", "492275105", "antd")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM " + sys.argv[1]+";"
sqlTitle = "select column_name from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='" +sys.argv[1]+"';"
try:
    # 创建csv文件
    with open(sys.argv[1]+'.csv', 'w', newline='') as csvfile:
        fieldnames = []
        # 获取列名
        cursor.execute(sqlTitle)
        titleResults = cursor.fetchall()
        for title in titleResults:
            fieldnames.append(title[0])
        # fieldnames = ['song_id', 'song_name', 'author_name', 'song_img','album_name','song_time', 'song_url', 'album_data', 'create_time', 'update_time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        if sys.argv[1] == 'songlist':
            for row in results:
                songId = str(row[0])
                songName = str(row[1])
                authorName = str(row[2])
                albumName = str(row[3])
                songImg = str(row[4])
                songTime = str(row[5])
                songUrl = str(row[6])
                albumData = str(row[7])
                createTime = str(row[8])
                updateTime = str(row[9])
                # 将结果写入csv文件中
                writer.writerow({'song_id': songId, 'song_name': songName, 'author_name': authorName, 'album_name': albumName,
                                'song_img': songImg, 'song_time': songTime, 'song_url': songUrl, 'album_data': albumData, 'create_time': createTime, 'update_time': updateTime})
                # 打印结果
                print(row)
        elif sys.argv[1] == 'userlist':
            for row in results:
                Id = row[0]
                userName = row[1]
                userPass = row[2]
                userRealName = row[3]
                userBirth = row[4]
                userId = row[5]
                createTime = row[6]
                updateTime = row[7]
                # 将结果写入csv文件中
                writer.writerow({'id': Id, 'user_name': userName, 'user_password': userPass,
                                'user_realname': userRealName, 'user_birthday': userBirth, 'user_id': userId, 'create_time': createTime, 'update_time': updateTime})
                # 打印结果
                print(row)

except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()
