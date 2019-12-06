"""
import pyperclip

pyperclip.copy("这是我复制的内容")
text = pyperclip.paste()
print("获取剪切板内容：" + text)

import  os
print os.getcwd() #获取当前工作目录路径
print os.path.abspath('.') #获取当前工作目录路径
print os.path.abspath('test.txt') #获取当前目录文件下的工作目录路径
print os.path.abspath('..') #获取当前工作的父目录 ！注意是父目录路径
print os.path.abspath(os.curdir) #获取当前工作目录路径
"""

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import pyperclip

def clip(file):
    filepath = os.path.abspath(file)
    with open(filepath) as f:
        str = f.read()
        pyperclip.copy(str)
        print(pyperclip.paste())

if __name__ == '__main__':
    str = input("请输入文件名:")
    clip(str)
