'''
Created on Nov 24, 2020

@author: DingYang
'''

import re

class Pattern:
    def __init__(self,pId,patternSeq,patternFrequency=0):
        self.pId=pId
        self.patternSeq=patternSeq
        self.patternFrequency=patternFrequency
        
    def getPatterns(self,fileName):
        reqPatterns=[]
        try:
                with open(fileName,'r') as f:
                    data=f.readline()
                    elePlace=0
                    while data:
                        temp=re.split(',|:',data)
                        reqPattern=Pattern('',[],0)
                        for i in range(len(temp)-2):
                            reqPattern.patternSeq.append(temp[i])
                        reqPattern.pId=temp[len(temp)-1]
                        reqPattern.patternFrequency=temp[len(temp)-2]
                        reqPatterns.append(reqPattern)
                        data=f.readline()
                        elePlace=elePlace+1
                return  reqPatterns
        except IOError as ioerr:
                print("File error:" + str(ioerr))
                return(None)
            
    def getReqPatterns(self,fileName):
        return self.getPatterns(fileName)
    
    def getServPatterns(self,fileName):
        oldServPatterns=self.getPatterns(fileName)#no processing service pattern for preparing other using
        newServPatterns=oldServPatterns
        for i in range(len(newServPatterns)):
            patternSeq=[]
            for j in range(len(newServPatterns[i].patternSeq)):
                temp=newServPatterns[i].patternSeq[j].strip().split('-')
                patternSeq.append(temp[0])
            newServPatterns[i].patternSeq=patternSeq
        return newServPatterns
    
#kmp pattern matching algorithm
class Solution:
    # get next array
    def get_next(self, T):
        i = 0
        j = -1
        next_val = [-1] * len(T)
        while i < len(T)-1:
            if j == -1 or T[i] == T[j]:
                i += 1
                j += 1
                # next_val[i] = j
                if i < len(T) and T[i] != T[j]:
                    next_val[i] = j
                else:
                    next_val[i] = next_val[j]
            else:
                j = next_val[j]
        return next_val
        
    # KMP algorithm
    def kmp(self, S, T):
        i = 0
        j = 0
        next1 = self.get_next(T)
        while i < len(S) and j < len(T):
            if j == -1 or S[i] == T[j]:
                i += 1
                j += 1
            else:
                j = next1[j]
        if j == len(T):
            return i - j
        else:
            return -1#-1 represent not success matching