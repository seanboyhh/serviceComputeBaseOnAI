# coding=gbk
'''
Created on Nov 10, 2020

@author: DingYang
'''
import urllib.request
import re
import os

def getHtml(url):  #ָ����ַ��ȡ����
    page = urllib.request.urlopen(url)
    html = page.read()
    return html.decode('gbk')

def getImg(html):  #�����ȡͼƬ����
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    x = 0
    path = r'F:\data\crawler'  
    # ��ͼƬ���浽F:\File_Python\Crawler�ļ����У����û��Crawler�ļ���,�����Զ��򴴽�
    if not os.path.isdir(path):  
        os.makedirs(path)  
    paths = path+'\\'     

    for imgurl in imglist:  #��in�����б����imgurlͼƬ��ַ��ѭ������ͼƬ�����ڱ���
        urllib.request.urlretrieve(imgurl,'{}{}.jpg'.format(paths,x))   
        x = x + 1  
    return imglist
html = getHtml("http://slide.news.sina.com.cn/y/slide_1_88490_489548.html")#ָ����ȡͼƬ����ַ·��
print (getImg(html)) 