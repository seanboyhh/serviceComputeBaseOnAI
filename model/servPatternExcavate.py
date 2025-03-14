# coding=gbk
'''
Created on Nov 23, 2020

@author: DingYang
'''

from tool.FPTree import FPTree
from pattern.patternExcavate import sortAndSave

                    
if __name__=='__main__':
#generating pattern
#     fp = FPTree('E:\data\python\serviceComposition\\servHistory.txt',3)
#     fp.FPGrowth()
#     fp.Output()
#     fp.saveToFile('E:\data\python\serviceComposition/servPatternsOld.txt')

#sorting toward pattern and to save
    fileName1='E:\data\python\serviceComposition/servPatternsOld.txt'
    fileName2='E:\data\python\serviceComposition/servPatternsDescByLen.txt'
    sortAndSave(fileName1,fileName2,'sp')