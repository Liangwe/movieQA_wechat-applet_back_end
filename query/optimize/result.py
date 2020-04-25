# -*- coding:utf-8 -*-
from query.util.get_image import getImage


class OptimizeResult:
    def isChinese(ch):
        if ch >= '\u4e00' and ch <= '\u9fa5':
            return True
        else:
            return False

    def lenStr(tem_str):
        count = 0
        for line in tem_str:
            if OptimizeResult.isChinese(line) or line in ['：', '，', '！', '。', '？', '“',
                                                          '”', 'Ⅰ', 'Ⅱ', 'Ⅲ', 'Ⅳ', 'Ⅴ', '、', '·',
                                                          '·', '（', '）', '—']:
                count = count + 2
            else:
                count = count + 1
        return count

    def parse(self, candidate_list):
        movie_info = []
        movie_list = []
        cooperate_list = []
        person_info = []
        siminfo_list = []
        hot_list = []
        person_list = []
        for i in range(0, len(candidate_list)):
            if candidate_list[i][0] == 1 :
                if len(candidate_list[i][1]) != 0:
                    movie_info.append((candidate_list[i][1]))
            elif candidate_list[i][0] == 2:
                if len(candidate_list[i][1]) != 0:
                    person_info.append((candidate_list[i][1]))
            elif candidate_list[i][0] == 3:
                if len(candidate_list[i][1]) != 0:
                    movie_list.append((candidate_list[i][1]))
            elif candidate_list[i][0] == 4:
                if len(candidate_list[i][1]) != 0:
                    cooperate_list.append((candidate_list[i][1]))
            elif candidate_list[i][0] == 5:
                if len(candidate_list[i][1]) != 0:
                    siminfo_list.append((candidate_list[i][1]))
            elif candidate_list[i][0] == 6:
                if len(candidate_list[i][1]) != 0:
                    hot_list.append((candidate_list[i][1]))
            elif candidate_list[i][0] == 7:
                if len(candidate_list[i][1]) != 0:
                    person_list.append((candidate_list[i][1]))

        if movie_list:
            movie_tmp = []
            movie_data = {}
            if len(movie_list[0])/2 > 30 :
                result = ('共查询到{}条信息，如下所示(按照电影评分排名，仅显示前三十条)：\n'.format(int(len(movie_list[0]) / 2)))
            else:
                result = ('共查询到{}条信息，如下所示(按照电影评分排名)：\n'.format(int(len(movie_list[0]) / 2)))
            for i in range(0, len(movie_list[0]), 2):
                tmp = {}
                if len(movie_list[0])/2 < 30:
                    tmp["movie_name"] =  movie_list[0][i]
                    tmp["movie_score"] = movie_list[0][i + 1]
                    movie_tmp.append(tmp)
                else:
                    if i < 60:
                        tmp["movie_name"] = movie_list[0][i]
                        tmp["movie_score"] = movie_list[0][i + 1]
                        movie_tmp.append(tmp)
                    else:
                        break
            movie_data['movie_list_info'] = result
            movie_data["movie_list"] = movie_tmp
            return movie_data

            # result = '共查询到{}条信息，如下所示(按照电影评分排名)：\n'.format(int(len(movie_list[0]) / 2))
            # for i in range(0, len(movie_list[0]), 2):
            #     if movie_list[0][i + 1] == '':
            #         movie_list[0][i + 1] = '暂无评分信息'
            #     tmp = {}
            #     tmp["movie_name"] = movie_list[0][i]
            #     tmp["movie_score"] = movie_list[0][i + 1]
            #     movie_tmp.append(tmp)
            #
            # movie_data['movie_list_info'] = result
            # movie_data["movie_list"] = movie_tmp
            # return movie_data

        if person_list:
            person_tmp = []
            person_data = {}
            result = '共查询到{}条信息，如下所示(按照演电影数量排名)：\n'.format(int(len(person_list[0]) / 2))
            for i in range(0, len(person_list[0]), 2):
                if person_list[0][i + 1] == '':
                    person_list[0][i + 1] = '暂无信息'
                tmp = {}
                tmp["person_name"] = person_list[0][i]
                tmp["person_movie_num"] = person_list[0][i + 1]
                person_tmp.append(tmp)
            person_data['person_list_info'] = result
            person_data["person_list"] = person_tmp
            return person_data

        if cooperate_list:
            cooperate_tmp = []
            cooperate_data = {}
            if len(cooperate_list[0])/3 > 90 :
                result = ('共查询到{}条信息，如下所示(按照合作次数排名，仅显示前三十条)：\n'.format(int(len(cooperate_list[0]) / 3)))
            else:
                result = ('共查询到{}条信息，如下所示(按照合作次数排名)：\n'.format(int(len(cooperate_list[0]) / 3)))
            for i in range(0, len(cooperate_list[0]), 3):
                tmp = {}
                if len(cooperate_list[0])/3 < 30:

                    tmp["cooperate_name"] =  cooperate_list[0][i]
                    tmp["cooperate_times"] = cooperate_list[0][i + 1]
                    tmp["ori_name"] = cooperate_list[0][i + 2]
                    cooperate_tmp.append(tmp)
                else:
                    if i < 90:
                        tmp["cooperate_name"] = cooperate_list[0][i]
                        tmp["cooperate_times"] = cooperate_list[0][i + 1]
                        tmp["ori_name"] = cooperate_list[0][i + 2]
                        cooperate_tmp.append(tmp)
                    else:
                        break
            cooperate_data['cooperate_info'] = result
            cooperate_data["cooperate_list"] = cooperate_tmp
            return cooperate_data

        if hot_list:
            hot_tmp = []
            hot_data = {}
            if len(hot_list[0])/3 > 30 :
                result = ('共查询到{}条信息，如下所示(按照电影评分排名，仅显示前三十条)：\n'.format(int(len(hot_list[0]) / 3)))
            else:
                result = ('共查询到{}条信息，如下所示(按照电影评分排名)：\n'.format(int(len(hot_list[0]) / 3)))
            for i in range(0, len(hot_list[0]), 3):
                tmp = {}
                if len(hot_list[0])/3  < 30:
                    tmp["hot_name"] = hot_list[0][i]
                    tmp["hot_rating"] = hot_list[0][i + 1]
                    tmp["hot_time"] = hot_list[0][i + 2]
                    hot_tmp.append(tmp)
                else:
                    if i < 90:
                        tmp["hot_name"] = hot_list[0][i]
                        tmp["hot_rating"] = hot_list[0][i + 1]
                        tmp["hot_time"] = hot_list[0][i + 2]
                        hot_tmp.append(tmp)
                    else:
                        break
            hot_data["hot_info"] = result
            hot_data["hot_list"] = hot_tmp

            return hot_data

        if siminfo_list:
            siminfo_data = {}
            siminfo_tmp = []

            result = '查询到以下信息：\n'
            siminfo_data["siminfo_info"] = result
            if "https://img" not in ''.join(siminfo_list[0]):
                for i in range(0, len(siminfo_list[0]), 2):
                     siminfo_tmp.append(str(siminfo_list[0][i]))
                siminfo_data["siminfo_data"] = ','.join(siminfo_tmp)
            else:
                cover = str(getImage(siminfo_list[0][0]))
                siminfo_data["siminfo_data"] = cover
            return siminfo_data

        if person_info:
            person_data = {}
            result = '查询到以下信息：\n'
            for i in range(len(person_info)):
                if person_info[i] =='':
                    person_info[i] = '暂无此信息'
            try:
                name = ''.join(person_info[0])
            except:
                name = '暂无此信息'
            try:
                other_name = ''.join(person_info[1])
            except:
                other_name = '暂无此信息'
            try:
                gender = ''.join(person_info[2])
            except:
                gender = '暂无此信息'
            try:
                birthplace = ''.join(person_info[3])
            except:
                birthplace ='暂无此信息'
            try:
                birthday = ''.join(person_info[4])
            except:
                birthday = '暂无此信息'
            try:
                constellation = ''.join(person_info[5])
            except:
                constellation = '暂无此信息'
            try:
                profession = ''.join(person_info[6])
            except:
                profession ='暂无此信息'
            try:
                introduction = ''.join(person_info[7])
            except:
                introduction = '暂无此信息'
            try:
                image_url = ''.join(person_info[8])
                if image_url:
                    person_image = getImage(image_url)
                    if person_image == None:
                        person_image = '暂无此信息'
                else:
                    person_image = '暂无此信息'
            except:
                person_image ='暂无此信息'

            person_data["person_info"] = result
            person_data["person_name"] = name
            person_data["person_other_name"] = other_name
            person_data["person_gender"] = gender
            person_data["person_birthplace"] = birthplace
            person_data["person_birthday"] = birthday
            person_data["person_constellation"] = constellation
            person_data["person_profession"] = profession
            person_data["person_introduction"] = introduction
            person_data["person_image"] = person_image

            return person_data

        if movie_info:
            movie_info_data = {}
            data = []
            max_len = max(len(j) for j in movie_info)
            for j in movie_info:
                while len(j) != max_len:
                    j.append('')
            for k in range(max_len):
                tmp = []
                for i in movie_info:
                    tmp.append(i[k])
                data.append(tmp)
            result = ('共查询到{}条信息，如下所示：\n'.format(str(len(data))))
            for i in range(len(data)):
                for j in range(len(data[i])):
                    if data[i][j] == '':
                        data[i][j] = '暂无此信息'
            try:
                name = ''.join(data[0][0])
            except:
                name = '暂无此信息'
            try:
                other_name = ''.join(data[0][1])
            except:
                other_name = '暂无此信息'
            try:
                country = ''.join(data[0][2])
            except:
                country = '暂无此信息'
            try:
                language = ''.join(data[0][3])
            except:
                language = '暂无此信息'
            try:
                date = ''.join(data[0][4])
            except:
                date = '暂无此信息'
            try:
                duration = ''.join(data[0][5])
            except:
                duration = '暂无此信息'
            try:
                score = ''.join(data[0][6])
            except:
                score = '暂无此信息'
            try:
                tag = ''.join(data[0][7])
            except:
                tag = '暂无此信息'
            try:
                introduction = ''.join(data[0][8])
            except:
                introduction = '暂无此信息'
            try:
                cover = ''.join(data[0][9])
                if cover:
                    movie_image = getImage(cover)
                    if movie_image == None:
                        movie_image = '暂无此信息'
                else:
                    movie_image = '暂无此信息'
            except:
                movie_image = '暂无此信息'

            movie_info_data["movie_info"] = result
            movie_info_data["movie_name"] = name
            movie_info_data["movie_other_name"] = other_name
            movie_info_data["movie_country"] = country
            movie_info_data["movie_language"] = language
            movie_info_data["movie_date"] = date
            movie_info_data["movie_duration"] = duration
            movie_info_data["movie_score"] = score
            movie_info_data["movie_tag"] = tag
            movie_info_data["movie_introduction"] = introduction
            movie_info_data["movie_image"] = movie_image
            return movie_info_data
        else:
            result ={}
            result["result_info"] = '对不起, 我不知道这个问题答案.\n' \
                    '你可以回复\"问答\", 来了解我可以回答的问题类型.'

            return result



