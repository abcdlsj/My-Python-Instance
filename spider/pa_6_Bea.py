# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 14:59:05 2019

@author: lison
"""

import requests
from bs4 import BeautifulSoup
import urllib.request

headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
        }

play_url = 'https://music.163.com/playlist?id=762862931'
d_url = 'http://music.163.com/song/media/outer/url?id='
s = requests.session()

reponse = s.get(play_url,headers=headers).content

s = BeautifulSoup(reponse,'lxml')

main = s.find('ul',{'class':'f-hide'})
print(main)

lists = []
for music in main.find_all('a'):
    music_url = d_url+music['href'][9:]+'.mp3'
    music_name = music.text
    list = []
    list.append(music_url)
    list.append(music_name)
    lists.append(list)

print(lists)


for list in lists[:3]:
    name = list[1]
    music = list[0]
    try:
        print('正在下载',name)
        urllib.request.urlretrieve(music,'D://music//%s.mp3'%name)
        print('下载完成')
    except:
        print('下载失败',name)


