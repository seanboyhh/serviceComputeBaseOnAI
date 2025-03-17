# coding=gbk
'''
Created on Apr 13, 2021

@author: Administrator
'''
from tool.FPTree import FPTree
from pattern.patternExcavate import sortAndSave

if __name__=='__main__':
    fp = FPTree('D:\servicePattern\\servHistory.txt',3)
    fp.FPGrowth()
    fp.Output()
    fp.saveToFile('D:\servicePattern/servPatternsOld.txt')
    fileName1=('D:\servicePattern/servPatternsOld.txt')
    fileName2=('D:\servicePattern/servPatternsDescByLen.txt')
    sortAndSave(fileName1,fileName2,'sp')
    