# -*- coding:utf-8 -*-
"""
问句实体识别
-----------------
现阶段使用jieba分词,demo
完成后训练NER命名实体识别
"""

import jieba
import jieba.posseg as pseg

class Word(object):
    def __init__(self, token, pos):
        self.token = token
        self.pos = pos

class QueryNER:
    def __init__(self, path_list, stopwords):
        """
        初始化, 加载外部词典
        :param dict_paths:
        """
        self.stopwordspath = stopwords

        for p in path_list:
            jieba.load_userdict(p)

        # jieba未正确切分词, 人工调整其频率
        jieba.suggest_freq('其他名字', True)
        jieba.suggest_freq('其他名称', True)
        jieba.suggest_freq('上映地区', True)
        jieba.suggest_freq('上映国家', True)
        jieba.suggest_freq('上映时间', True)
        jieba.suggest_freq('上映语言', True)
        jieba.suggest_freq('评分人数', True)
        jieba.suggest_freq('详细介绍', True)
        jieba.suggest_freq('个人信息', True)
        jieba.suggest_freq('时长', True)
        jieba.suggest_freq('出生时间', True)
        jieba.suggest_freq('中国大陆', True)
        jieba.suggest_freq('近期热门', True)
        jieba.suggest_freq('演', True)
        jieba.suggest_freq('不低于', True)
        jieba.suggest_freq('不高于', True)
        jieba.suggest_freq('不少于', True)
        jieba.suggest_freq('不多于', True)
        for i in range(1892,2025):
            jieba.suggest_freq(str(i), True)

    # 创建停用词list
    def stopwordslist(self):
        stopwords = [line.strip() for line in open(self.stopwordspath, 'r', encoding='gbk').readlines()]
        return stopwords

    def seg_sentence(self,sentence):
        """
        need txt
        :param sentence:
        :return:
        """
        sentence_seged = jieba.cut(sentence.strip())
        stopwords = QueryNER.stopwordslist(self)  # 这里加载停用词的路径
        outstr = []
        for word in sentence_seged:
            if word not in stopwords:
                if word != '\t':
                    outstr.append(word)
        return ''.join(outstr)

    def get_ner_objects(self, question):
        """
        对问题进行实体识别
        :param question:·
        :return:
        """
        output = QueryNER.seg_sentence(self,question)
        return [Word(word, tag) for word, tag in pseg.cut(output)]


if __name__ == '__main__':
    question_ner = QueryNER(['movie_name.txt', 'person_name.txt'],"stop_words.txt")
    question = '吴京的电影中不低于7分的电影有哪些'
    ner_object = question_ner.get_ner_objects(question)
    for value in ner_object:
        print(value.token, value.pos)
