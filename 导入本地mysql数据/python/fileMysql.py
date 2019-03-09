#!/usr/bin/python3

# 数据库
import pymysql
import csv
import sys
# 获取MP3信息
from mutagen import File
import os
# copy文件
import shutil

# 时间
import time
import datetime
# 
import math

# 打开数据库连接
db = pymysql.connect("localhost", "root", "492275105", "antd")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 如果数据表已经存在使用 execute() 方法删除表。
cursor.execute("DROP TABLE IF EXISTS SONGLIST")

# 创建数据表SQL语句
initsql = """CREATE TABLE IF NOT EXISTS SONGLIST
        (
            `song_id` bigint(20) NOT NULL AUTO_INCREMENT,
            song_name varchar(128),
            author_name varchar(255),
            album_name varchar(255),
            song_img varchar(1000),
            song_time varchar(255),
            song_url varchar(1000),
            album_data varchar(255),
            create_time datetime not null,
            update_time datetime not null,
            PRIMARY KEY (`song_id`)
        )ENGINE = INNODB CHARACTER SET utf8;"""
# 执行创建表任务
cursor.execute(initsql)

# insert sql
insertsql = "INSERT into songList( song_name, author_name, album_name, song_img, song_time, song_url, album_data, create_time, update_time) \
       VALUES (%s, %s, %s, %s, %s, %s, %s, NOW(), NOW() )"
try:
    for filename in os.listdir(r'G:\\CloudMusic'):
        afile = File('G:\\CloudMusic\\'+filename)
        # 封面图片数据
        artwork = afile.tags['APIC:'].data  
        # 作者
        author = afile.tags["TPE1"].text[0]  
        # 标题
        title = afile.tags["TIT2"].text[0]  
        # 专辑
        album = afile.tags["TALB"].text[0]  

        # 获取歌曲时间（没满10秒的前面加0）
        stime = afile.info.length
        mint = str(int(stime/60))
            # 
        # sec = math.ceil(stime%60)
        # 
        sec = math.floor(stime%60)
        if sec<10:
            sec = '0'+ str(sec)
        else:
            sec = str(sec)
        # 歌曲时间
        songtime = mint+':'+ sec

        # 时间戳
        nowTime = int(round(time.time() * 1000))
        
        # 加时间戳的图片文件
        # imgId = str(title)+'-'+str(nowTime)+'.jpg'
        imgId = str(title)+'.jpg'
        # 专辑创建时间
        albumData = str(datetime.datetime.now().strftime('%Y-%m-%d'))


        # with open('D:/web/react/antd/antd-port/static/img/'+ imgId, 'wb') as img:
        #     img.write(artwork)
        # shutil.copyfile('G:/CloudMusic/' + filename,
        #                 'D:/web/react/antd/antd-port/static/music/'+filename)
        # 执行sql语句
        cursor.execute(insertsql, (title, author, album, imgId, songtime, filename, albumData))
        # 提交到数据库执行
        db.commit()
except:
   # 如果发生错误则回滚
   print("Error: unable to fetch data")

# 关闭数据库连接
db.close()
