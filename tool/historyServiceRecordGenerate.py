# coding=gbk
'''
Created on Nov 23, 2020

@author: DingYang
'''

import random

def randomGenerate(iterateNum,reqNum,fileName,reqActivities):
    reqActivities=reqActivities
    file=open(fileName,'w')
    for num in range(iterateNum):##��0��iterateNum��������iterateNum
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
reqActivities=["ƻ��","�㽶","����","����","ţ��","���","����","�ɿ���","������","������"]
#service units
servUnits=["ƻ��-"+str(random.sample(range(0,99),1)[0]),"�㽶-"+str(random.sample(range(0,99),1)[0]),"����-"+str(random.sample(range(0,99),1)[0]),"����-"+str(random.sample(range(0,99),1)[0]),"ţ��-"+str(random.sample(range(0,99),1)[0]),"���-"+str(random.sample(range(0,99),1)[0]),"����-"+str(random.sample(range(0,99),1)[0]),"�ɿ���-"+str(random.sample(range(0,99),1)[0]),"������-"+str(random.sample(range(0,99),1)[0]),"������-"+str(random.sample(range(0,99),1)[0])]
fileName='E:\data\python\serviceComposition/servHistory.txt'
randomGenerate(10000, 10,fileName,servUnits)