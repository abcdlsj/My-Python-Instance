 # -*- coding: utf-8 -*-
import requests
import webbrowser
import os
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
from lxml import html

'''
param = {"wd": "abcdlsj"}  # 搜索的信息
r1 = requests.get('http://www.baidu.com/s', params=param)
print(r1.url)
webbrowser.open(r1.url)
'''

'''
data={'firstname':'a','lastname':'b'}
r2 = requests.post("http://pythonscraping.com/pages/files/processing.php",data=data)
print(r2.text)
'''

'''
file={'uploadFile':open('/Users/abcdlsj/Pictures/wallhaven-140569.jpg','rb')}
r3 = requests.post("http://pythonscraping.com/pages/files/processing2.php",files=file)
print(r3.text)
'''

'''
data = {'username':'111','password':'password'}
r4 = requests.post("http://pythonscraping.com/pages/cookies/welcome.php",data=data)
print(r4.cookies.get_dict())

r5 = requests.get("http://pythonscraping.com/pages/cookies/welcome.php",cookies=r4.cookies)
print(r5.text)
'''

'''
data = {'username':'111','password':'password'}
session = requests.Session()
r6 = session.post("http://pythonscraping.com/pages/cookies/welcome.php",data=data)
print(r6.cookies.get_dict())
r7 = session.get("http://pythonscraping.com/pages/cookies/welcome.php")
print(r7.text)
'''

'''
os.makedirs('./img/',exist_ok=True)

IMAGE_URL = "https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png"


urlretrieve(IMAGE_URL,'./img/image1.png')

r8 = requests.get(IMAGE_URL)


with open('./img/image2.png','wb') as f:
    f.write(r8.content)

with open('./img/image3.png','wb') as f:
    for chunk in r8.iter_content(chunk_size=32):
        f.write(chunk)
'''

'''
练习下载图片
'''

URL="http://www.ngchina.com.cn/photography/"

html = requests.get(URL).text

soup = BeautifulSoup(html,'lxml')
img_ul = soup.find_all('ul',{'class':"cf"})


for ul in img_ul:
    imgs = ul.find_all('img')
    for img in imgs:
        url = img['src']
        image = requests.get(url,stream=True)
        ima_name = url.split('/')[-1]
        with open('./img/%s' % ima_name,'wb') as f:
            for chunk in image.iter_content(chunk_size=32):
                f.write(chunk)
