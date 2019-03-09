# -*- coding: UTF-8 -*-
#!/usr/bin/python3

import requests, sys
import json
url = 'https://mmtp1.com/jjtq/zipai/594/02.jpg'
r = requests.get(url)
json_obj = r.text
j = json.loads(json_obj)

lry = open(sys.argv[2]+'.txt', 'w', newline='')
lry.write(j['lrc']['lyric'])
print(j['lrc']['lyric'])
# 获取网易云歌词 使用时 1 输入歌曲ID 2 输入歌曲名