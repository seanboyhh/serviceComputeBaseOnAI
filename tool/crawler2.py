# coding=gbk
'''
Created on Nov 10, 2020

@author: DingYang
'''
import urllib.request
import re
import os

def getHtml(url):  #指定网址获取函数
    page = urllib.request.urlopen(url)
    html = page.read()
    return html.decode('gbk')

def getImg(html):  #定义获取图片函数
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    x = 0
    path = r'F:\data\crawler'  
    # 将图片保存到F:\File_Python\Crawler文件夹中，如果没有Crawler文件夹,将会自动则创建
    if not os.path.isdir(path):  
        os.makedirs(path)  
    paths = path+'\\'     

    for imgurl in imglist:  #打开in集合中保存的imgurl图片网址，循环下载图片保存在本地
        urllib.request.urlretrieve(imgurl,'{}{}.jpg'.format(paths,x))   
        x = x + 1  
    return imglist
html = getHtml("http://slide.news.sina.com.cn/y/slide_1_88490_489548.html")#指定获取图片的网址路径
print (getImg(html)) 