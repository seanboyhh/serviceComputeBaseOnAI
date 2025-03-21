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
    
    # 保存模型，供以后使用
    model.save("word2vec.model")
 
    # 模型读取
    # model = word2vec.Word2Vec.load("your_model_name")
 
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    model = models.Word2Vec.load('word2vec.model')
 
    print("提供 3 种测试模式\n")
    print("输入一个词，则去寻找前一百个该词的相似词")
    print("输入两个词，则去计算两个词的余弦相似度")
    print("输入三个词，进行类比推理")
    
    while True:
        try:
            query = input('')
            q_list = query.split()
 
            if len(q_list) == 1:
                print("相似词前 100 排序")
                res = model.wv.most_similar(q_list[0], topn=100)
                for item in res:
                    print(item[0] + "," + str(item[1]))
 
            elif len(q_list) == 2:
                print("计算 Cosine 相似度")
                res = model.wv.similarity(q_list[0], q_list[1])
                print(res)
            else:
                print("%s之于%s，如%s之于" % (q_list[0], q_list[2], q_list[1]))
                res = model.wv.most_similar([q_list[0], q_list[1]], [q_list[2]], topn=100)
                for item in res:
                    print(item[0] + "," + str(item[1]))
            print("----------------------------")
        except Exception as e:
            print(repr(e))