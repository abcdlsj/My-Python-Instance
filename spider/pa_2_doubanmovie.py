# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 08:10:51 2019

@author: abcdlsj
"""
import requests as re
from lxml import html
k=1
for i in range(10):
    URL = "https://movie.douban.com/top250?start={}&filter=".format(i*25)
    con = re.get(URL).content
    sel = html.fromstring(con)
    infos = sel.xpath('//div[@class="info"]')
    posters = sel.xpath('//div[@class="pic"]')
    for url in infos:
        title = url.xpath('div[@class="hd"]//span[@class="title"]/text()')
        web = url.xpath('div[@class="hd"]/a/@href')
        # print (web[0]+" : "+title[0])
        info = url.xpath('div[@class="bd"]/p/text()')
        ##poster = url_p.xpath('a/img/@src')
        ## 导演主演
        dire=info[0].replace(" ", "").replace("\n", "") 
        ## 年份地区和类型
        date = info[1].replace(" ","").replace("\n","").split("/")[0]
        country = info[1].replace(" ","").replace("\n","").split("/")[1]
        geners = info[1].replace(" ","").replace("\n","").split("/")[2]
        print("\n"+title[0]+"\n"+web[0]+"\n"+date+country+geners+"\n"+dire+"\n\n"+'*'*60)
        with open('250top.txt','a',encoding="utf-8") as f:
            f.write('*'*60+"\n"+title[0]+"\tTOP: "+str(k)+"\n"+web[0]+"\n"+date+country+geners+"\n"+dire+"\n")
        k=k+1
