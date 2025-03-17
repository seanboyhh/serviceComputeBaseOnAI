# coding=gbk
'''
Created on Jun 6, 2021

@author: DingYang
'''

import logging
from gensim import models
from gensim.models import word2vec

def similarity():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = word2vec.LineSentence("E:/data/python/serviceComposition/trainCorpus.txt")
    model = word2vec.Word2Vec(sentences, vector_size=250)
    
    # ����ģ�ͣ����Ժ�ʹ��
    model.save("word2vec.model")
 
    # ģ�Ͷ�ȡ
    # model = word2vec.Word2Vec.load("your_model_name")
 
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    model = models.Word2Vec.load('word2vec.model')
 
    print("�ṩ 3 �ֲ���ģʽ\n")
    print("����һ���ʣ���ȥѰ��ǰһ�ٸ��ôʵ����ƴ�")
    print("���������ʣ���ȥ���������ʵ��������ƶ�")
    print("���������ʣ������������")
    
    while True:
        try:
            query = input('')
            q_list = query.split()
 
            if len(q_list) == 1:
                print("���ƴ�ǰ 100 ����")
                res = model.wv.most_similar(q_list[0], topn=100)
                for item in res:
                    print(item[0] + "," + str(item[1]))
 
            elif len(q_list) == 2:
                print("���� Cosine ���ƶ�")
                res = model.wv.similarity(q_list[0], q_list[1])
                print(res)
            else:
                print("%s֮��%s����%s֮��" % (q_list[0], q_list[2], q_list[1]))
                res = model.wv.most_similar([q_list[0], q_list[1]], [q_list[2]], topn=100)
                for item in res:
                    print(item[0] + "," + str(item[1]))
            print("----------------------------")
        except Exception as e:
            print(repr(e))