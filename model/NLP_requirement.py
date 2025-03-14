
# coding=gbk
'''
Created on Jun 3, 2021

@author: DingYang
'''

import os
import re
from pyltp import Segmentor, Postagger, Parser, NamedEntityRecognizer, SementicRoleLabeller

class LtpParser:
    def __init__(self):
        LTP_DIR = "F:/temp/ltp_data_v3.4.0"
        self.segmentor = Segmentor()    # 分词
        self.segmentor.load(os.path.join(LTP_DIR, "cws.model"))

        self.postagger = Postagger()    # 词性标注
        self.postagger.load(os.path.join(LTP_DIR, "pos.model"))

        self.parser = Parser()  # 句法依存分析
        self.parser.load(os.path.join(LTP_DIR, "parser.model"))

        self.recognizer = NamedEntityRecognizer()   # 命名实体识别
        self.recognizer.load(os.path.join(LTP_DIR, "ner.model"))

        self.labeller = SementicRoleLabeller()  # 语义角色标注
        self.labeller.load(os.path.join(LTP_DIR, 'pisrl_win.model'))

    # 依存句法分析【为句子中的每个词语维护一个保存句法依存儿子节点的字典】
    def build_parse_child_dict(self, words, postags): # words：分词后的结果；postags：词性标注后的结果；arcs：依存句法分析树
        print("-" * 50, "依存句法分析：开始", "-" * 50)
        child_dict_list = []
        format_parse_list = []
        arcs = self.parser.parse(words, postags)  # 建立依存句法分析树
        print("分词列表：words = {}".format(words))
        print("词性分析：postags = {}".format(postags))
        rely_ids = [arc.head - 1 for arc in arcs]  # 提取该句话的每一个词的依存父节点id【0为ROOT，词语从1开始编号】: [2, 0, 2, 5, 8, 8, 6, 3] - 1 =  [1, -1, 1, 4, 7, 7, 5, 2]【此时 -1 表示ROOT】
        print("各个词语所依赖的父节点：rely_ids = {0}".format(rely_ids))
        heads = ['Root' if rely_id == -1 else words[rely_id] for rely_id in rely_ids]  # 匹配依存父节点词语
        print("各个词语所依赖的父节点词语 = {0}".format(heads))
        relations = [arc.relation for arc in arcs]  # 提取依存关系
        print("各个词语与所依赖的父节点的依赖关系 = {0}".format(relations))

        for word_index in range(len(words)):
            print("\nword_index = {0}----word = {1}".format(word_index, words[word_index]))
            child_dict = dict() # 每个词语与所有其他词语的关系字典
            for arc_index in range(len(arcs)):  # arc_index==0时表示ROOT【还没进入“我想听一首迪哥的歌”语句】，arc_index==1时表示“我”
                # 当“依存句法分析树”遍历，遇到当前词语时，说明当前词语在依存句法分析树中与其他词语有依存关系
                if word_index == rely_ids[arc_index]:  # arcs[arc_index].head 表示arcs[arc_index]所代表的词语依存弧的父结点的索引。 ROOT 节点的索引是 0 ，第一个词开始的索引依次为1，2，3，···【“我”的索引为1】arc. relation 表示依存弧的关系。
                    print("word_index = {0}----arc_index = {1}----rely_ids[arc_index] = {2}----relations[arc_index] = {3}".format(word_index, arc_index, rely_ids[arc_index], relations[arc_index]))
                    if relations[arc_index] in child_dict:  # arcs[arc_index].relation表示arcs[arc_index]所代表的词语与父节点的依存关系(语法关系)
                        child_dict[relations[arc_index]].append(arc_index) # 添加 child_dict = {'ATT': [4]}----> child_dict = {'ATT': [4, 5]}
                    else:
                        child_dict[relations[arc_index]] = [] # 新建
                        child_dict[relations[arc_index]].append(arc_index)  # child_dict = {[]}----> child_dict = {'ATT': [4]}
                    print("child_dict = {0}".format(child_dict))
            child_dict_list.append(child_dict)# 每个词对应的依存关系父节点和其关系
            print("child_dict_list = {0}".format(child_dict_list))
        # 整合每个词语的句法依存关系
        for i in range(len(words)):
            a = [relations[i], words[i], i, postags[i], heads[i], rely_ids[i]-1, postags[rely_ids[i]-1]]
            format_parse_list.append(a)
        print("整合每个词语的句法依存关系---->format_parse_list = ", format_parse_list)
        print("-" * 50, "依存句法分析：结束", "-" * 50)
        return child_dict_list, format_parse_list

    # 语义角色标注
    def format_labelrole(self, words, postags):
        print("-"*50, "语义角色标注：开始", "-"*50)
        print("分词----> words= {0}----len(words) = {1}".format(words, len(words)))
        print("词性标注----> postags= {0}----len(postags) = {1}".format(postags, len(postags)))
        arcs = self.parser.parse(words, postags)  # 建立依存句法分析树
        roles = self.labeller.label(words, postags, arcs)
        print("len(roles) = {0}----roles = {1}".format(len(roles), roles))
        roles_dict = {}
        for role in roles:
            print("谓语所在索引：role.index = {0}".format(role.index))
            roles_dict[role.index] = {arg.name:[arg.name,arg.range.start, arg.range.end] for arg in role.arguments}
        # {6: {'A0': ['A0', 0, 2], 'TMP': ['TMP', 3, 3], 'LOC': ['LOC', 4, 5], 'A1': ['A1', 8, 8]}}
        # 6：表示谓语（发表）所在序号；
        # A0：表示“施事者、主体、触发者”，0,2分别表示A0所在的起始索引、终止索引（此句中有2个A0，分别是“奥巴马”、“克林顿”，索引范围是是0-2）
        # TMP：表示“时间”，3, 3分别表示TMP所在的起始索引、终止索引（“昨晚”）
        # LOC：表示“地点”，4, 5分别表示LOC所在的起始索引、终止索引（“在”,“白宫”）
        # A1：表示“受事者”，8, 8分别表示LOC所在的起始索引、终止索引（“演说”）
        print("语义角色标注---->roles_dict = {0}".format(roles_dict))
        print("-" * 50, "语义角色标注：结束", "-" * 50)
        return roles_dict

    # parser主函数
    def parser_main(self, sentence):
        # 分词
        words = list(self.segmentor.segment(sentence))
        # 词性标注
        postags = list(self.postagger.postag(words))
        # 依存句法分析
        child_dict_list, format_parse_list = self.build_parse_child_dict(words, postags)
        # 语义角色标注
        roles_dict = self.format_labelrole(words, postags)

        return words, postags, child_dict_list, format_parse_list, roles_dict

# 关系抽取类
class TripleExtractor:
    def __init__(self):
        self.parser = LtpParser()

    '''文章分句处理, 切分长句，冒号，分号，感叹号等做切分标识'''
    def split_sents(self, content):
        return [sentence for sentence in re.split(r'[？?！!。；;：:，,\n\r]', content) if sentence]

    '''利用语义角色标注,直接获取主谓宾三元组,基于A0,A1,A2'''
    def ruler1(self, words, postags, roles_dict, role_index):
        v = words[role_index]
        role_info = roles_dict[role_index]
        if 'A0' in role_info.keys() and 'A1' in role_info.keys():
            s = ''.join([words[word_index] for word_index in range(role_info['A0'][1], role_info['A0'][2]+1) if
                         postags[word_index][0] not in ['w', 'u', 'x'] and words[word_index]])
            o = ''.join([words[word_index] for word_index in range(role_info['A1'][1], role_info['A1'][2]+1) if
                         postags[word_index][0] not in ['w', 'u', 'x'] and words[word_index]])
            if s  and o:
                return '1', [s, v, o]
        return '4', []

    '''三元组抽取主函数'''
    def ruler2(self, words, postags, child_dict_list, format_parse_list, roles_dict):
        svos = []
        for index in range(len(postags)):
            tmp = 1
            # 先借助语义角色标注的结果，进行三元组抽取
            if index in roles_dict:
                flag, triple = self.ruler1(words, postags, roles_dict, index)
                if flag == '1':
                    svos.append(triple)
                    tmp = 0
            if tmp == 1:
                # 如果语义角色标记为空，则使用依存句法进行抽取
                # if postags[index] == 'v':
                if postags[index]:
                # 抽取以谓词为中心的事实三元组
                    child_dict = child_dict_list[index]
                    # 主谓宾
                    if 'SBV' in child_dict and 'VOB' in child_dict:
                        r = words[index]
                        e1 = self.complete_e(words, postags, child_dict_list, child_dict['SBV'][0])
                        e2 = self.complete_e(words, postags, child_dict_list, child_dict['VOB'][0])
                        svos.append([e1, r, e2])

                    # 定语后置，动宾关系
                    relation = format_parse_list[index][0]
                    head = format_parse_list[index][2]
                    if relation == 'ATT':
                        if 'VOB' in child_dict:
                            e1 = self.complete_e(words, postags, child_dict_list, head - 1)
                            r = words[index]
                            e2 = self.complete_e(words, postags, child_dict_list, child_dict['VOB'][0])
                            temp_string = r + e2
                            if temp_string == e1[:len(temp_string)]:
                                e1 = e1[len(temp_string):]
                            if temp_string not in e1:
                                svos.append([e1, r, e2])
                    # 含有介宾关系的主谓动补关系
                    if 'SBV' in child_dict and 'CMP' in child_dict:
                        e1 = self.complete_e(words, postags, child_dict_list, child_dict['SBV'][0])
                        cmp_index = child_dict['CMP'][0]
                        r = words[index] + words[cmp_index]
                        if 'POB' in child_dict_list[cmp_index]:
                            e2 = self.complete_e(words, postags, child_dict_list, child_dict_list[cmp_index]['POB'][0])
                            svos.append([e1, r, e2])
        return svos

    '''对找出的主语或者宾语进行扩展：【定中关系  ATT 红苹果 (红 <– 苹果)】'''
    def complete_e(self, words, postags, child_dict_list, word_index):
        child_dict = child_dict_list[word_index]
        prefix = ''
        if 'ATT' in child_dict:
            for i in range(len(child_dict['ATT'])):
                prefix += self.complete_e(words, postags, child_dict_list, child_dict['ATT'][i])
        postfix = ''
        if postags[word_index] == 'v':
            if 'VOB' in child_dict:
                postfix += self.complete_e(words, postags, child_dict_list, child_dict['VOB'][0])
            if 'SBV' in child_dict:
                prefix = self.complete_e(words, postags, child_dict_list, child_dict['SBV'][0]) + prefix

        return prefix + words[word_index] + postfix


    '''程序主控函数'''
    def triples_main(self, text):
        sentences = self.split_sents(text)
        svos = []
        for index, sentence in enumerate(sentences):
            print("="*50, "第{}句：开始".format(index + 1), "="*50)
            # words: 分词; postags: 词性标注; child_dict_list: 依存句法分析; roles_dict: 语义角色标注
            words, postags, child_dict_list, format_parse_list, roles_dict = self.parser.parser_main(sentence)
            svo = self.ruler2(words, postags, child_dict_list, format_parse_list, roles_dict)
            print("svo = {0}".format(svo))
            print("=" * 50, "第{}句：结束".format(index + 1), "=" * 50)
            svos += svo
        return svos

# 关系抽取
def run_extractor(text):
    extractor = TripleExtractor()
    svos = extractor.triples_main(text)
    return svos


