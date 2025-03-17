# coding=gbk
'''
Created on Nov 23, 2020

@author: DingYang
'''
from pattern import Solution

def aMapping(patternSeq,servPatterns):
    solution=Solution()
    mark=-1#start position in mapping
    pos=0#which service pattern
    mapRecord=[-1,-1]
    while (mark==-1)&(pos<len(servPatterns)):
        mark=solution.kmp(patternSeq, servPatterns[pos].patternSeq)
        pos=pos+1
    pos=pos-1
    mapRecord[0]=pos
    mapRecord[1]=mark
    return mapRecord

def patternMapping(reqPatterns,servPatterns):
    #a require pattern has a map sequence that record mapping result
    mapSeq=[]*len(reqPatterns)
    for i in range(len(reqPatterns)):
        #mainString record current main string that requirement mapping
        #reqPatterns[i] represent current requirement pattern
        mainString=reqPatterns[i].patternSeq
        originalStart=0# start position in original requirement pattern
        #mapping mark of require pattern
        #'None' means no mapping
        #'-1' means mapping fail
        #'pattern id' means mapping success
        reqPatternMark=[None]*len(reqPatterns[i].patternSeq)
        while mainString!=None:
            mapRecord=aMapping(mainString,servPatterns)
            if mapRecord[1]!=-1:
                length=len(servPatterns[mapRecord[0]].patternSeq)
                for j in range(length):
                    reqPatternMark[mapRecord[1]+j+originalStart]=servPatterns[mapRecord[0]].pId
            else:
                length=len(mainString)
                for k in range(length):
                    reqPatternMark[k+originalStart]=-1
            noneStart=0
            noneEnd=0
            #To scanning 'reqPatternMark' for setting new 'mainString'
            while (reqPatternMark[noneStart]!=None)&(noneStart<(len(reqPatternMark)-1)):
                noneStart+=1
            if noneStart==(len(reqPatternMark)-1):
                noneEnd=noneStart+1
            else:
                noneEnd=noneStart+1  
                while (noneEnd<(len(reqPatternMark)-1))&(reqPatternMark[noneEnd]==None):
                    noneEnd+=1
            if (noneStart==(len(reqPatternMark)-1))&(reqPatternMark[noneStart]!=None):
                mainString=None
            else:
                mainString=reqPatterns[i].patternSeq[noneStart:noneEnd]
            originalStart=noneStart
        mapSeq.append(reqPatternMark)
    return mapSeq