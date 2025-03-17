# coding=gbk
'''
Created on Nov 23, 2020

@author: DingYang
'''

import random

def randomGenerate(iterateNum,reqNum,fileName,reqActivities):
    reqActivities=reqActivities
    file=open(fileName,'w')
    for num in range(iterateNum):##从0到iterateNum，不包含iterateNum
        randomData=random.sample(reqActivities,reqNum)
        eleNum=0
        print(randomData)
        for ele in randomData:
            eleNum=eleNum+1
            if eleNum<reqNum:
                file.write(ele+',')
            else:
                file.write(ele)
        file.write('\n')
        num
    file.close()

#requirement activities
reqActivities=["苹果","香蕉","榴莲","葡萄","牛奶","面包","鸡蛋","巧克力","三明治","汉堡包"]
#service units
servUnits=["苹果-"+str(random.sample(range(0,99),1)[0]),"香蕉-"+str(random.sample(range(0,99),1)[0]),"榴莲-"+str(random.sample(range(0,99),1)[0]),"葡萄-"+str(random.sample(range(0,99),1)[0]),"牛奶-"+str(random.sample(range(0,99),1)[0]),"面包-"+str(random.sample(range(0,99),1)[0]),"鸡蛋-"+str(random.sample(range(0,99),1)[0]),"巧克力-"+str(random.sample(range(0,99),1)[0]),"三明治-"+str(random.sample(range(0,99),1)[0]),"汉堡包-"+str(random.sample(range(0,99),1)[0])]
fileName='E:\data\python\serviceComposition/servHistory.txt'
randomGenerate(10000, 10,fileName,servUnits)