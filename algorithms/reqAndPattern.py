# coding=gbk
'''
Created on Nov 17, 2020

@author: DingYang
'''
# import re

class ReqPattern:
    def __init__(self,pId,pattern,patternFrequency):
        self.pId=pId
        self.pattern=pattern
        self.patternFrequency=patternFrequency

class Req:
    def __init__(self,rId,reqSeq):
        self.rId=rId
        self.reqSeq=reqSeq
                