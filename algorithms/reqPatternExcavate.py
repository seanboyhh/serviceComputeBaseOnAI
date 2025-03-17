# coding=gbk
'''
Created on Nov 23, 2020

@author: DingYang
'''

from tool.FPTree import FPTree
from pattern.patternExcavate import sortAndSave

                    
if __name__=='__main__':
#generating pattern
#     fp = FPTree('E:\data\python\serviceComposition\\reqHistory.txt',3)
#     fp.FPGrowth()
#     fp.Output()
#     fp.saveToFile('E:\data\python\serviceComposition/reqPatternsOld.txt')

#sorting and saving toward pattern
    fileName1='E:\data\python\serviceComposition/reqPatternsOld.txt'
    fileName2='E:\data\python\serviceComposition/reqPatternsDescByLen.txt'
    sortAndSave(fileName1,fileName2,'rp')     