# coding=gbk
'''
Created on Nov 23, 2020

@author: DingYang
'''

import numpy as np
from time import perf_counter
# from pattern.pattern import Pattern 
# from pattern.bilateralPatternMapping import aMapping, patternMapping
from service.atomService import AtomService,PSO,optimizationServs,sortOfservSetsByWeight
# import matplotlib.pyplot as plt

if __name__=='__main__':
#     servPattern=Pattern('',[],0)
#     reqPattern=Pattern('',[],0)
#     fileName='E:\data\python\serviceComposition/servPatternsDescByLen.txt'
#     fileName2='E:\data\python\serviceComposition/reqPatternsDescByLen.txt'
#     servPatterns=servPattern.getServPatterns(fileName)
#     reqPatterns=reqPattern.getReqPatterns(fileName2)
#     mapRcord=aMapping(reqPatterns[0],servPatterns)
#     
#     print("需求模式："+reqPatterns[0].pId+',需求模式匹配的服务模式：'+servPatterns[mapRcord[0]].pId+',匹配开始的位置：%d'%mapRcord[1])
#     mapSeq=patternMapping(reqPatterns,servPatterns)
#     for i in range(len(mapSeq)):
#         print(mapSeq[i])
    fileName='D:\data\python\serviceComposition/QWS2.txt'
    atomservice=AtomService('','',0.0,0.0,0,0,0.0,0)
    atomServices=atomservice.getAtomServices(fileName)
    candidateServSets=[]
    num=0
    for i in range(4):
        candidateServSets.append(atomServices[num:num+100])
        num+=100
    w=[0.3,0.1,0.2,0.1,0.2,0.1]
    pso = PSO(1000, 1000,len(candidateServSets),w,candidateServSets)
    t1=perf_counter()
    pso.evolve()
    t2=perf_counter()
    t=t2-t1
    print('time is '+str(t))
#     optimizationServs(candidateServSets,w)
     
    