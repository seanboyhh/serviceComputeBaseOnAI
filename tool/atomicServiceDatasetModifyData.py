# coding=gbk
'''
Created on Dec 11, 2020

@author: DingYang
'''

import random

#randomly generate 4 figures
def random4Figures():
    num1=random.randint(1,100)
    num2=random.randint(0,9)
    num3=random.randint(0,9)
    num=str(num1)+'.'+str(num2)+str(num3)
    num=float(num)
    if num>100:
        num=100
    return num

def modifyData(fileName1,fileName2):
    f_w=open(fileName2,'w')
    with open(fileName1,'r') as f:
        lines=f.readlines()
        lineNum=0
        for line in lines:
            reputation=str(random.randint(0,10))
            price=random4Figures()
            servId='as'+str(lineNum+1)
            if (lineNum>=0)&(lineNum<=99):
                servName='苹果-'+str(lineNum)
                line_new=line.replace('\n','')
                line_new=line_new+','+str(price)+','+reputation+','+servName+','+servId+'\n'
            if (lineNum>=100)&(lineNum<=199):
                servName='香蕉-'+str(lineNum-100)
                line_new=line.replace('\n','')
                line_new=line_new+','+str(price)+','+reputation+','+servName+','+servId+'\n'
            if (lineNum>=200)&(lineNum<=299):
                servName='榴莲-'+str(lineNum-200)
                line_new=line.replace('\n','')
                line_new=line_new+','+str(price)+','+reputation+','+servName+','+servId+'\n'
            if (lineNum>=300)&(lineNum<=399):
                servName='葡萄-'+str(lineNum-300)
                line_new=line.replace('\n','')
                line_new=line_new+','+str(price)+','+reputation+','+servName+','+servId+'\n'
            if (lineNum>=400)&(lineNum<=499):
                servName='牛奶-'+str(lineNum-400)
                line_new=line.replace('\n','')
                line_new=line_new+','+str(price)+','+reputation+','+servName+','+servId+'\n'
            if (lineNum>=500)&(lineNum<=599):
                servName='面包-'+str(lineNum-500)
                line_new=line.replace('\n','')
                line_new=line_new+','+str(price)+','+reputation+','+servName+','+servId+'\n'
            if (lineNum>=600)&(lineNum<=699):
                servName='鸡蛋-'+str(lineNum-600)
                line_new=line.replace('\n','')
                line_new=line_new+','+str(price)+','+reputation+','+servName+','+servId+'\n'
            if (lineNum>=700)&(lineNum<=799):
                servName='巧克力-'+str(lineNum-700)
                line_new=line.replace('\n','')
                line_new=line_new+','+str(price)+','+reputation+','+servName+','+servId+'\n'
            if (lineNum>=800)&(lineNum<=899):
                servName='三明治-'+str(lineNum-800)
                line_new=line.replace('\n','')
                line_new=line_new+','+str(price)+','+reputation+','+servName+','+servId+'\n'
            if (lineNum>=900)&(lineNum<=999):
                servName='汉堡包-'+str(lineNum-900)
                line_new=line.replace('\n','')
                line_new=line_new+','+str(price)+','+reputation+','+servName+','+servId+'\n'
            if (lineNum>=1000)&(lineNum<=1099):
                servName='橘子-'+str(lineNum-1000)
                line_new=line.replace('\n','')
                line_new=line_new+','+str(price)+','+reputation+','+servName+','+servId+'\n'
            if (lineNum>=1100)&(lineNum<=1199):
                servName='甘蔗-'+str(lineNum-1100)
                line_new=line.replace('\n','')
                line_new=line_new+','+str(price)+','+reputation+','+servName+','+servId+'\n'
            if (lineNum>=1200)&(lineNum<=1299):
                servName='菠萝-'+str(lineNum-1200)
                line_new=line.replace('\n','')
                line_new=line_new+','+str(price)+','+reputation+','+servName+','+servId+'\n'
            if (lineNum>=1300)&(lineNum<=1399):
                servName='青菜-'+str(lineNum-1300)
                line_new=line.replace('\n','')
                line_new=line_new+','+str(price)+','+reputation+','+servName+','+servId+'\n'
            if (lineNum>=1400)&(lineNum<=1499):
                servName='生菜-'+str(lineNum-1400)
                line_new=line.replace('\n','')
                line_new=line_new+','+str(price)+','+reputation+','+servName+','+servId+'\n'
            if (lineNum>=1500)&(lineNum<=1599):
                servName='牛肉-'+str(lineNum-1500)
                line_new=line.replace('\n','')
                line_new=line_new+','+str(price)+','+reputation+','+servName+','+servId+'\n'
            if (lineNum>=1600)&(lineNum<=1699):
                servName='羊肉-'+str(lineNum-1600)
                line_new=line.replace('\n','')
                line_new=line_new+','+str(price)+','+reputation+','+servName+','+servId+'\n'
            if (lineNum>=1700)&(lineNum<=1799):
                servName='鸡肉-'+str(lineNum-1700)
                line_new=line.replace('\n','')
                line_new=line_new+','+str(price)+','+reputation+','+servName+','+servId+'\n'
            if (lineNum>=1800)&(lineNum<=1899):
                servName='鱼肉-'+str(lineNum-1800)
                line_new=line.replace('\n','')
                line_new=line_new+','+str(price)+','+reputation+','+servName+','+servId+'\n'
            if (lineNum>=1900)&(lineNum<=1999):
                servName='鸭肉-'+str(lineNum-1900)
                line_new=line.replace('\n','')
                line_new=line_new+','+str(price)+','+reputation+','+servName+','+servId+'\n'
            if (lineNum>=2000)&(lineNum<=2099):
                servName='坚果-'+str(lineNum-2000)
                line_new=line.replace('\n','')
                line_new=line_new+','+str(price)+','+reputation+','+servName+','+servId+'\n'
            if (lineNum>=2100)&(lineNum<=2199):
                servName='橙子-'+str(lineNum-2100)
                line_new=line.replace('\n','')
                line_new=line_new+','+str(price)+','+reputation+','+servName+','+servId+'\n'
            if (lineNum>=2200)&(lineNum<=2299):
                servName='豆腐-'+str(lineNum-2200)
                line_new=line.replace('\n','')
                line_new=line_new+','+str(price)+','+reputation+','+servName+','+servId+'\n'
            if (lineNum>=2300)&(lineNum<=2399):
                servName='豆皮-'+str(lineNum-2300)
                line_new=line.replace('\n','')
                line_new=line_new+','+str(price)+','+reputation+','+servName+','+servId+'\n'
            if (lineNum>=2400)&(lineNum<=2499):
                servName='豆浆-'+str(lineNum-2400)
                line_new=line.replace('\n','')
                line_new=line_new+','+str(price)+','+reputation+','+servName+','+servId+'\n'
            if lineNum>2499:
                line_new=line
            lineNum+=1
            f_w.write(line_new)
            

if __name__=='__main__':
    fileName1='E:\data\python\serviceComposition/QWS.txt'
    fileName2='E:\data\python\serviceComposition/QWS2.txt'
    modifyData(fileName1,fileName2)