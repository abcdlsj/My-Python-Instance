# -*- coding: utf-8 -*-
"""
Created on Fri Nov 1 19:25:51 2019

@author: abcdlsj
"""

import requests
from lxml import html

for i in range(10):
    URL = "https://book.douban.com/top250?start={}".format(i*25)
    con = requests.get(URL).content
    sel = html.fromstring(con)
    infos = sel.xpath()
