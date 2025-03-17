'''
Created on Nov 24, 2020

@author: DingYang
'''

class Req:
    def __init__(self,rId,reqSeq):
        self.rId=rId
        self.reqSeq=reqSeq
    
    'getting new requirements'
    def getNewReqs(self,fileName):
        reqs=[]
        try:
            with open(fileName,'r') as f:
                data=f.readline()
                elePlace=0
                while data:
                    temp=data.strip().split(',')
                    req=Req('',[])
                    for i in range(len(temp)):
                        req.reqSeq.append(temp[i])
                    req.rId='r'+str(elePlace)
                    reqs.append(req)
                    data=f.readline()
                    elePlace+=1
            return  reqs
        except IOError as ioerr:
            print("File error:" + str(ioerr))
            return(None)

class ReqDesc:
    def __init__(self,rdId,desc):
        self.rdId=rdId
        self.desc=desc
    
    'getting requirement descriptions'    
    def getReqDescs(self,fileName):
        reqDescs=[]
        try:
            with open(fileName,'r') as f:
                data=f.readline()
                while data:
                    temp=data.strip().split(' ',1)
                    reqDesc=ReqDesc('','')
                    reqDesc.desc=temp[1]
                    reqDesc.rdId=temp[0]
                    reqDescs.append(reqDesc)
                    data=f.readline()
            return  reqDescs
        except IOError as ioerr:
            print("File error:" + str(ioerr))
            return(None)