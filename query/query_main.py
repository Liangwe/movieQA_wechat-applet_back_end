# -*- coding:utf-8 -*-

"""
处理整个流程
"""
from query.ner.query_ner import QueryNER
from query.inference.query2sparql import Query2Sparql
from query.fuseki.sparql_query import SparqlQuery
from query.optimize.result import OptimizeResult
from query.util.handle_image import from_str_split_out_image


class Query:
    def __init__(self):
        """
        初始化
        """

        # 初始化Jena Fuseki服务器
        self.sparql_query = SparqlQuery()

        # NER初始化加载词
        self.query_ner = QueryNER(['query/ner/movie_name.txt', 'query/ner/person_name.txt'],"query/ner/stop_words.txt")

        # 初始化加载推理模型
        self.query2sparql = Query2Sparql()

        # 优化返回答案
        self.optimize_result = OptimizeResult()
        print("Query初始化完成...")

    def parse(self, question):
        """
        解析主流程
        :return:
        """
        if "问答" in str(question, encoding='utf-8') or "你好" in str(question, encoding='utf-8') \
                or "功能" in str(question, encoding='utf-8'):
            result = {}
            result["result_info"] = "你好啊, 我是智能的机器人月月，你可以问我关于电影领域的问题哟. 比如:<br />" \
                                    "1. 流浪地球的详细信息是什么呢？<br />" \
                                    "2. 流浪地球的主演/导演/编剧/海报/上映地区/上映时间/时长/其他名字/简介/评分/评价人数是什么？<br />" \
                                    "3. 吴京的详细信息是什么呢? <br />" \
                                    "4. 吴京的图片/性别/星座/生日/出生地/职业/其他名称/介绍/是什么? <br />" \
                                    "5. 吴京主演/导演/的电影有哪些？<br />" \
                                    "...等等其他类型电影问题"
            return result

        # 实体识别
        question_label = self.query_ner.get_ner_objects(question)
        # for value in question_label:
        #     print(value.token, value.pos)

        # Sparql模版推理
        sparql_list = self.query2sparql.parse(question_label)
        # for sparql in sparql_list:
        #     print(sparql[0], sparql[1])
        #     print('=' * 20)
        # Apache Jena 查询
        candidate_list = []
        for sparql_q in sparql_list:
            sparql_result = self.sparql_query.get_sparql_result(sparql_q[1])
            sparql_result_value = self.sparql_query.get_sparql_result_value(sparql_result)
            candidate_list.append((sparql_q[0], sparql_result_value))

        # 优化返回结果
        result = self.optimize_result.parse(candidate_list)
        return result


if __name__ == '__main__':
    query = Query()
    question = '流浪地球详细信息'
    while True:
        question = input('问题: ').encode('utf-8')
        ans = query.parse(question)
        if "b'RIFF" not in str(ans):
            print(str(ans))
        else:
            for i in from_str_split_out_image(ans):
                if i != '':
                    print(i)

