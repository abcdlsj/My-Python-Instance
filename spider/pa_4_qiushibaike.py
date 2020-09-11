# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 17:10:49 2019

@author: lison
"""

# -*- coding: utf-8 -*-

from lxml import html
import requests

URL = "https://www.qiushibaike.com/"

con = requests.get(URL).content
sel = html.fromstring(con)
file="C:\\Users\\lison\\Desktop\\ABC\\Python_Learning\\pach\\qiushibake.txt"

for i in sel.xpath('//div[@class="article block untagged mb15 typs_hot"]'):
    text = i.xpath('a/div[@class="content"]/span/text()')
    for t in text:
        t.replace("\n","")
        print(t)
        with open(file,'a',encoding='UTF-8') as f:
            f.write(t)
    print('\n')