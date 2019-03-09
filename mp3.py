#!/usr/bin/env python
# coding=utf8
import os
import sys
import logging
import re
from replica import tagger

reload(sys)
sys.setdefaultencoding("gb18030")

ENCODING = {0: "latin1", 1: "utf16", 2: "utf16be", 3: "utf8"}

logging.basicConfig(filename="mp3.log", level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s ")


def modify_textual(string):
    return re.sub(u'[\\\/:\*\?"<>\|]', " ", string)


def process_one_song(songName):
    mp3 = tagger.get_tags(u"{songname}".format(songname=songName))
    try:
        artist = mp3.get("TPE1").text[0]
        enco_form = ENCODING.get(mp3.get("TPE1").encoding)
        if enco_form == "latin1":
            artist = artist.encode("latin1")
    except AttributeError as e:
        artist = u"未知艺术家"
    try:
        name = mp3.get("TIT2").text[0]
        enco_form = ENCODING.get(mp3.get("TIT2").encoding)
        if enco_form == "latin1":
            name = name.encode("latin1")
    except AttributeError as e:
        name = u"未知曲名"
    name = modify_textual(name)
    artist = modify_textual(artist)
    logging.info(u"{songname}".format(songname=songName) +
                 u"{filename}.mp3".format(
                         filename=os.path.dirname(songName) + os.sep.decode("utf8") + name + u"-" + artist))
    try:
        os.rename(u"{songname}".format(songname=songName), u"{filename}.mp3".format(
                filename=os.path.dirname(songName) + os.sep.decode("utf8") + name + u"-" + artist))
    except WindowsError as windowserror:
        logging.error(
                "error processing {name} for windows error [{error}]".format(name=songName, error=str(windowserror)))


def main():
    try:
        rootpath = sys.argv[1]
    except IndexError as e:
        rootpath = 'mp3'
    if not os.path.isdir(rootpath):
        print u"输入目录不存在"
        sys.exit(1)
    count = 0
    total = 0
    for root, dir, files in os.walk(rootpath):
        total += len(files)
    for root, dir, files in os.walk(rootpath):
        for file in files:
            filename = os.path.join(root.decode("gb18030"), file.decode("gb18030"))
            if os.path.splitext(file)[1] != '.mp3':
                os.remove(filename)
                continue
            count += 1
            print u"正在处理{percent:.0f}%的歌".format(percent=float(count) / total * 100)
            process_one_song(filename)