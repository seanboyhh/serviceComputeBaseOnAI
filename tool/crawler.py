# coding=gbk
'''
Created on Nov 10, 2020

@author: DingYang
'''
##import requests
import urllib.request
import urllib.parse
import re
import os
#���header������Referer�Ǳ����,����᷵��403����User-Agent�Ǳ���ģ������ſ���αװ����������з���
header=\
{
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
     "referer":"https://image.baidu.com"
    }
url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word={word}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&cg=girl&pn={pageNum}&rn=30&gsm=1e00000000001e&1490169411926="
keyword = input("�����������ؼ��֣�")
#ת��
keyword = urllib.parse.quote(keyword,'utf-8')
 
n = 0
j = 0
 
while(n<3000):
    error = 0
    n+=30
    #url
    url1 = url.format(word=keyword,pageNum=str(n))
    #��ȡ����
    rep = urllib.request.Request(url1,headers=header)
    #����ҳ
    rep = urllib.request.urlopen(rep)
    #��ȡ��ҳ����
    try:
        html = rep.read().decode('utf-8')
        # print(html)
    except:
        print("�����ˣ�")
        error = 1
        print("����ҳ����"+str(n))
    if error == 1:
        continue
    #����ƥ��
    p = re.compile("thumbURL.*?\.jpg")
    #��ȡ����ƥ�䵽�Ľ��������list
    s = p.findall(html)
    if os.path.isdir(r"F:\data\crawler") != True:
        os.makedirs(r"F:\data\crawler")
    with open("testpic.txt","a") as f:
        #��ȡͼƬ
        for i in s:
            print(i)
            i = i.replace('thumbURL":"','')
            print(i)
            f.write(i)
            f.write("\n")
            #����ͼƬ
            urllib.request.urlretrieve(i,r"F:\data\crawler/pic{num}.jpg".format(num=j))
            j+=1
        f.close()
