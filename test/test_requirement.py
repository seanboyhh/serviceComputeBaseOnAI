# coding=gbk
'''
Created on Jun 3, 2021

@author: DingYang
'''

from requirement.requirement import ReqDesc
from requirement.NLP_requirement import run_extractor
# from requirement.similarity import similarity


if __name__ == '__main__':
    reqDesc=ReqDesc('','')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    fileName='E:\data\python\sergviceComposition/RequirementsOfUser.txt'
    reqDescs=reqDesc.getReqDescs(fileName)
    for i in range(len(reqDescs)):
        print(reqDescs[i].rdId+'---'+reqDescs[i].desc)
        svos = run_extractor(reqDescs[i].desc)
        print("��ϵ��ȡ�����svos = {0}".format(svos))
#     similarity()