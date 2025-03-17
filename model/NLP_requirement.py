
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
        self.segmentor = Segmentor()    # �ִ�
        self.segmentor.load(os.path.join(LTP_DIR, "cws.model"))

        self.postagger = Postagger()    # ���Ա�ע
        self.postagger.load(os.path.join(LTP_DIR, "pos.model"))

        self.parser = Parser()  # �䷨�������
        self.parser.load(os.path.join(LTP_DIR, "parser.model"))

        self.recognizer = NamedEntityRecognizer()   # ����ʵ��ʶ��
        self.recognizer.load(os.path.join(LTP_DIR, "ner.model"))

        self.labeller = SementicRoleLabeller()  # �����ɫ��ע
        self.labeller.load(os.path.join(LTP_DIR, 'pisrl_win.model'))

    # ����䷨������Ϊ�����е�ÿ������ά��һ������䷨������ӽڵ���ֵ䡿
    def build_parse_child_dict(self, words, postags): # words���ִʺ�Ľ����postags�����Ա�ע��Ľ����arcs������䷨������
        print("-" * 50, "����䷨��������ʼ", "-" * 50)
        child_dict_list = []
        format_parse_list = []
        arcs = self.parser.parse(words, postags)  # ��������䷨������
        print("�ִ��б�words = {}".format(words))
        print("���Է�����postags = {}".format(postags))
        rely_ids = [arc.head - 1 for arc in arcs]  # ��ȡ�þ仰��ÿһ���ʵ����游�ڵ�id��0ΪROOT�������1��ʼ��š�: [2, 0, 2, 5, 8, 8, 6, 3] - 1 =  [1, -1, 1, 4, 7, 7, 5, 2]����ʱ -1 ��ʾROOT��
        print("���������������ĸ��ڵ㣺rely_ids = {0}".format(rely_ids))
        heads = ['Root' if rely_id == -1 else words[rely_id] for rely_id in rely_ids]  # ƥ�����游�ڵ����
        print("���������������ĸ��ڵ���� = {0}".format(heads))
        relations = [arc.relation for arc in arcs]  # ��ȡ�����ϵ
        print("�����������������ĸ��ڵ��������ϵ = {0}".format(relations))

        for word_index in range(len(words)):
            print("\nword_index = {0}----word = {1}".format(word_index, words[word_index]))
            child_dict = dict() # ÿ��������������������Ĺ�ϵ�ֵ�
            for arc_index in range(len(arcs)):  # arc_index==0ʱ��ʾROOT����û���롰������һ�׵ϸ�ĸ衱��䡿��arc_index==1ʱ��ʾ���ҡ�
                # ��������䷨��������������������ǰ����ʱ��˵����ǰ����������䷨�������������������������ϵ
                if word_index == rely_ids[arc_index]:  # arcs[arc_index].head ��ʾarcs[arc_index]������Ĵ������满�ĸ����������� ROOT �ڵ�������� 0 ����һ���ʿ�ʼ����������Ϊ1��2��3�������������ҡ�������Ϊ1��arc. relation ��ʾ���满�Ĺ�ϵ��
                    print("word_index = {0}----arc_index = {1}----rely_ids[arc_index] = {2}----relations[arc_index] = {3}".format(word_index, arc_index, rely_ids[arc_index], relations[arc_index]))
                    if relations[arc_index] in child_dict:  # arcs[arc_index].relation��ʾarcs[arc_index]������Ĵ����븸�ڵ�������ϵ(�﷨��ϵ)
                        child_dict[relations[arc_index]].append(arc_index) # ��� child_dict = {'ATT': [4]}----> child_dict = {'ATT': [4, 5]}
                    else:
                        child_dict[relations[arc_index]] = [] # �½�
                        child_dict[relations[arc_index]].append(arc_index)  # child_dict = {[]}----> child_dict = {'ATT': [4]}
                    print("child_dict = {0}".format(child_dict))
            child_dict_list.append(child_dict)# ÿ���ʶ�Ӧ�������ϵ���ڵ�����ϵ
            print("child_dict_list = {0}".format(child_dict_list))
        # ����ÿ������ľ䷨�����ϵ
        for i in range(len(words)):
            a = [relations[i], words[i], i, postags[i], heads[i], rely_ids[i]-1, postags[rely_ids[i]-1]]
            format_parse_list.append(a)
        print("����ÿ������ľ䷨�����ϵ---->format_parse_list = ", format_parse_list)
        print("-" * 50, "����䷨����������", "-" * 50)
        return child_dict_list, format_parse_list

    # �����ɫ��ע
    def format_labelrole(self, words, postags):
        print("-"*50, "�����ɫ��ע����ʼ", "-"*50)
        print("�ִ�----> words= {0}----len(words) = {1}".format(words, len(words)))
        print("���Ա�ע----> postags= {0}----len(postags) = {1}".format(postags, len(postags)))
        arcs = self.parser.parse(words, postags)  # ��������䷨������
        roles = self.labeller.label(words, postags, arcs)
        print("len(roles) = {0}----roles = {1}".format(len(roles), roles))
        roles_dict = {}
        for role in roles:
            print("ν������������role.index = {0}".format(role.index))
            roles_dict[role.index] = {arg.name:[arg.name,arg.range.start, arg.range.end] for arg in role.arguments}
        # {6: {'A0': ['A0', 0, 2], 'TMP': ['TMP', 3, 3], 'LOC': ['LOC', 4, 5], 'A1': ['A1', 8, 8]}}
        # 6����ʾν�����������ţ�
        # A0����ʾ��ʩ���ߡ����塢�����ߡ���0,2�ֱ��ʾA0���ڵ���ʼ��������ֹ�������˾�����2��A0���ֱ��ǡ��°����������ֶ١���������Χ����0-2��
        # TMP����ʾ��ʱ�䡱��3, 3�ֱ��ʾTMP���ڵ���ʼ��������ֹ��������������
        # LOC����ʾ���ص㡱��4, 5�ֱ��ʾLOC���ڵ���ʼ��������ֹ���������ڡ�,���׹�����
        # A1����ʾ�������ߡ���8, 8�ֱ��ʾLOC���ڵ���ʼ��������ֹ����������˵����
        print("�����ɫ��ע---->roles_dict = {0}".format(roles_dict))
        print("-" * 50, "�����ɫ��ע������", "-" * 50)
        return roles_dict

    # parser������
    def parser_main(self, sentence):
        # �ִ�
        words = list(self.segmentor.segment(sentence))
        # ���Ա�ע
        postags = list(self.postagger.postag(words))
        # ����䷨����
        child_dict_list, format_parse_list = self.build_parse_child_dict(words, postags)
        # �����ɫ��ע
        roles_dict = self.format_labelrole(words, postags)

        return words, postags, child_dict_list, format_parse_list, roles_dict

# ��ϵ��ȡ��
class TripleExtractor:
    def __init__(self):
        self.parser = LtpParser()

    '''���·־䴦��, �зֳ��䣬ð�ţ��ֺţ���̾�ŵ����зֱ�ʶ'''
    def split_sents(self, content):
        return [sentence for sentence in re.split(r'[��?��!����;��:��,\n\r]', content) if sentence]

    '''���������ɫ��ע,ֱ�ӻ�ȡ��ν����Ԫ��,����A0,A1,A2'''
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

    '''��Ԫ���ȡ������'''
    def ruler2(self, words, postags, child_dict_list, format_parse_list, roles_dict):
        svos = []
        for index in range(len(postags)):
            tmp = 1
            # �Ƚ��������ɫ��ע�Ľ����������Ԫ���ȡ
            if index in roles_dict:
                flag, triple = self.ruler1(words, postags, roles_dict, index)
                if flag == '1':
                    svos.append(triple)
                    tmp = 0
            if tmp == 1:
                # ��������ɫ���Ϊ�գ���ʹ������䷨���г�ȡ
                # if postags[index] == 'v':
                if postags[index]:
                # ��ȡ��ν��Ϊ���ĵ���ʵ��Ԫ��
                    child_dict = child_dict_list[index]
                    # ��ν��
                    if 'SBV' in child_dict and 'VOB' in child_dict:
                        r = words[index]
                        e1 = self.complete_e(words, postags, child_dict_list, child_dict['SBV'][0])
                        e2 = self.complete_e(words, postags, child_dict_list, child_dict['VOB'][0])
                        svos.append([e1, r, e2])

                    # ������ã�������ϵ
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
                    # ���н����ϵ����ν������ϵ
                    if 'SBV' in child_dict and 'CMP' in child_dict:
                        e1 = self.complete_e(words, postags, child_dict_list, child_dict['SBV'][0])
                        cmp_index = child_dict['CMP'][0]
                        r = words[index] + words[cmp_index]
                        if 'POB' in child_dict_list[cmp_index]:
                            e2 = self.complete_e(words, postags, child_dict_list, child_dict_list[cmp_index]['POB'][0])
                            svos.append([e1, r, e2])
        return svos

    '''���ҳ���������߱��������չ�������й�ϵ  ATT ��ƻ�� (�� <�C ƻ��)��'''
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


    '''�������غ���'''
    def triples_main(self, text):
        sentences = self.split_sents(text)
        svos = []
        for index, sentence in enumerate(sentences):
            print("="*50, "��{}�䣺��ʼ".format(index + 1), "="*50)
            # words: �ִ�; postags: ���Ա�ע; child_dict_list: ����䷨����; roles_dict: �����ɫ��ע
            words, postags, child_dict_list, format_parse_list, roles_dict = self.parser.parser_main(sentence)
            svo = self.ruler2(words, postags, child_dict_list, format_parse_list, roles_dict)
            print("svo = {0}".format(svo))
            print("=" * 50, "��{}�䣺����".format(index + 1), "=" * 50)
            svos += svo
        return svos

# ��ϵ��ȡ
def run_extractor(text):
    extractor = TripleExtractor()
    svos = extractor.triples_main(text)
    return svos


