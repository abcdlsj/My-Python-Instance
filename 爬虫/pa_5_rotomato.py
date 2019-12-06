# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 21:52:44 2019

@author: lison
"""

import re

import requests
from bs4 import BeautifulSoup
from lxml import html

getid = re.compile(r'\d+')
ids = []
url_main = "http://www.rotomato.com/sort/newmovie/page/"
url_page = "http://www.rotomato.com/archives/"
def get_ids(url):
    for i in range(1,10):
        url_newmovie = url + str(i)
        con = requests.get(url_newmovie).content
        sel = html.fromstring(con)
        infos = sel.xpath('//article')
        for movie in infos:
            id = movie.xpath('@id')
            #titles = movie.xpath('a/@title')
            ids.append(str(id)[7:11])

def get_movies(_ids):
    k=1
    for _id in _ids:
        url_movie = url_page+_id
        con = requests.get(url_movie).content
        sel = html.fromstring(con)
        title = sel.xpath('//meta[@property="og:description"]/@content')
        code = sel.xpath('//code/a/@href')
        with open("rotomato.txt",'a',encoding="utf-8") as f:
            f.write(str(k)+" : "+'*'*60+"\n"+title[0]+"\n"+"下载链接:"+code[0]+"\n")
        k=k+1

if __name__=="__main__":
    get_ids(url_main)
    get_movies(ids)
