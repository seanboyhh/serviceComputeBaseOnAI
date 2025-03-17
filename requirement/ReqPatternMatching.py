# coding=gbk
'''
Created on Nov 17, 2020

@author: DingYang
'''
from requirement.requirement import Req
from pattern.pattern import Pattern
from pattern.pattern import Solution

def patternMatching(reqs,patterns,reqNum):
    s = Solution()
    mark=-1#'mark' present matching success or not
    elePlace=0#record place of pattern
    while (mark==-1)&(elePlace<len(patterns)):
        mark=s.kmp(reqs[reqNum].reqSeq,patterns[elePlace].patternSeq)
        if (mark==-1)&(elePlace<len(patterns)):
            elePlace+=1
    print('elePlace:%d'%elePlace+',pattern starting:%d'%mark)   

if __name__ == '__main__':
    req=Req('',[])
    pattern=Pattern('',[],0)
    patterns=pattern.getReqPatterns('E:\data\python\serviceComposition/reqPatternsDescByLen.txt')
    reqs=req.getNewReqs('E:\data\python\serviceComposition/reqNew.txt')
    patternMatching(reqs,patterns,1)

