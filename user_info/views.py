# coding=utf-8
from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from django.http import JsonResponse
import time
import numpy
import datetime
from user_info import models
from django.utils.timezone import now, timedelta


def index(request):
    return render(request, 'index_info.html', {'res': {}})


def index_info(request):
    return render(request, 'index_info.html', {'res': {}})


# 返回需要查询的过去12时， 12日，12周，12月的时间list
class GetDate(object):
    def get_mon(self):
        # 查询的开始时间与结束时间，从当前日期的开始，向前数12个月（包括本月）
        # django ORM 中，使用range按照时间段查询，与Python中range一样，不包括最后一项。因此查询到今天，得到结果相当于查询到昨天
        self.now_date = time.localtime()
        self.now_mon = self.now_date.tm_mon
        self.now_year = self.now_date.tm_year - 1
        if int(self.now_mon) == 12:
            self.now_mon = 0
            self.now_year += 1
        self.start_time = datetime.date(self.now_year, self.now_mon, 1)
        self.end_time = now().date()

        # 最近12个月的list（年-月）
        if int(self.end_time.month) == 12:
            all_month = map(lambda x: str(self.now_year) + '-' + str(x) + '-1', range(self.start_time.month, 13))
        else:
            all_month = map(lambda x: str(self.now_year) + '-' + str(x) + '-1', range(self.start_time.month, 13)) + \
                        map(lambda x: str(self.now_year + 1) + '-' + str(x) + '-1', range(1, self.end_time.month + 1))
        return all_month[::-1]

    def get_week(self):
        # 过去的12周
        date_week = []
        # 今天是本周的第几天，从0开始
        now_wday = time.localtime().tm_wday
        # 本周时间，从周一开始，到昨天
        week11 = []
        for i in range(now_wday + 1):
            week11.append((now().date() + timedelta(days=-i)).strftime('%Y-%m-%d'))
        date_week.append(week11)
        # 其余11周日期
        for each in range(12):
            week12 = []
            for j in range(8):
                week12.append(
                    time.strftime('%Y-%m-%d', time.localtime(time.time() - 24 * 60 * 60 * (now_wday + 7 * each + j)))
                )
            date_week.append(week12)
        return date_week

    def get_day(self):
        # 过去的12天
        res_day = []
        for i in range(13):
            select_day = (now().date() + timedelta(days=-i)).strftime('%Y-%m-%d')
            res_day.append(select_day)
        return res_day

    def get_hour(self):
        res_hour = [int(time.time())]
        for i in range(1, 13):
            res_hour.append(int(time.time()) - 3600 * i)
        return res_hour


def sex(request):
    app_id = 100256
    _time = GetDate()
    # 性别统计
    try:
        once_zichanbao = request.GET['zichanbao']
    except:
        once_zichanbao = 'all'
    # 过去的12天
    res_day = []
    for index, each in enumerate(_time.get_day()[:-1]):
        day_start_time = int(time.mktime(time.strptime(_time.get_day()[index + 1], "%Y-%m-%d")))
        day_end_time = int(time.mktime(time.strptime(each, "%Y-%m-%d")))
        res = models.UserInfoForStatistics.objects.filter(app_id=app_id,
                                                          create_time__range=(day_start_time, day_end_time))

        # 统计性别个数，如 男 女 两个
        sex_set = set()
        # 统计资产包个数
        option_set = set()
        for i in res:
            sex_set.add(i.sex)
            option_set.add(i.source)
        sex_list = sorted(list(sex_set))
        option_list = sorted(list(option_set))
        res_data = []
        for i in option_list:
            data = {
                'source': i,
                'option': sex_list,
                'count': [0] * len(sex_list)
            }
            res_data.append(data)
        for i in res:
            res_data[option_list.index(i.source)]['count'][sex_list.index(i.sex)] += 1
        # 统计总量
        all_count_one_day = []
        for i in res_data:
            all_count_one_day.append(i.get('count'))
        res_data.append({
            'source': 'all',
            'option': sex_list,
            'count': map(sum, list(zip(*all_count_one_day)))
        })
        res_day.append({'time': time.strftime('%Y-%m-%d', time.localtime(day_end_time)), 'data': res_data})

    list_day_1 = []
    for i in res_day:
        try:
            list_day_1.append(i.get('data')[0].get('count')[0])
        except:
            list_day_1.append(0)
    list_day_2 = []
    for i in res_day:
        try:
            list_day_2.append(i.get('data')[0].get('count')[1])
        except:
            list_day_2.append(0)
    data = {
        'res_day': res_day,
        'list_day_1': list_day_1,
        'list_day_2': list_day_2
    }
    return JsonResponse(data)


def age(request):
    app_id = 100256
    _time = GetDate()
    # 性别统计
    try:
        once_zichanbao = request.GET['zichanbao']
    except:
        once_zichanbao = 'all'
    # 过去的12天
    res_day = []
    for index, each in enumerate(_time.get_day()[:-1]):
        day_start_time = int(time.mktime(time.strptime(_time.get_day()[index + 1], "%Y-%m-%d")))
        day_end_time = int(time.mktime(time.strptime(each, "%Y-%m-%d")))
        res = models.UserInfoForStatistics.objects.filter(app_id=app_id,
                                                          create_time__range=(day_start_time, day_end_time))

        # 统计年龄
        res_age = [0, 0, 0, 0, 0, 0, 0]
        res_data = []
        for i in res:
            age = int(time.localtime().tm_year) - int(i.id_card[6:10])
            if 18 <= age <= 22:
                res_age[0] += 1
            elif 23 <= age <= 27:
                res_age[1] += 1
            elif 28 <= age <= 32:
                res_age[2] += 1
            elif 33 <= age <= 37:
                res_age[3] += 1
            elif 38 <= age <= 42:
                res_age[4] += 1
            elif 43 <= age <= 47:
                res_age[5] += 1
            else:
                res_age[6] += 1
        res_data.append({
            'source': 'all',
            'option': ['18-22', '23-27', '28-32', '33-37', '38-42', '43-47', '47及以上'],
            'count': res_age,
            'sum': sum(res_age)
        })
        res_day.append({'time': time.strftime('%Y-%m-%d', time.localtime(day_end_time)), 'data': res_data})
    data = {
        'res_day': res_day,
    }
    print(data)
    return JsonResponse(data)


def age_info(request):
    return render(request, 'user_age_info.html', {})

def comp_info(request):
    return render(request, 'comp_info.html', {})


# 通过开始时间及结束时间查询，返回申请量，通过量，通过率
def count_number(start_time, end_time):

    all_num = len(models.ModelRunningRecord.objects.filter(created_time__range=(start_time, end_time)))
    pass_num = len(
        models.ModelRunningRecord.objects.filter(
            Q(created_time__range=(start_time, end_time)), Q(category=2) | Q(category=1)
        )
    )
    if int(all_num) == 0:
        res = [time.strftime("%Y-%m-%d", time.localtime(end_time)), 0, 0, 0]
    else:
        res = [time.strftime("%Y-%m-%d", time.localtime(end_time)), all_num,
               pass_num, (round(pass_num/float(all_num), 2) * 100)]
    return res

def app_pass(request):
    app_id = 100256
    _time = GetDate()

    # # 申请量，通过量，通过率
    # res_hour = []
    # for index, j in enumerate(_time.get_hour()[:-1]):
    #     res_hour.append(count_number(_time.get_hour()[index + 1], j))

    # 过去的12天
    res_day = []
    for index, each in enumerate(_time.get_day()[:-1]):
        day_start_time = int(time.mktime(time.strptime(_time.get_day()[index + 1], "%Y-%m-%d")))
        day_end_time = int(time.mktime(time.strptime(each, "%Y-%m-%d")))
        res_day.append(count_number(day_start_time, day_end_time))

    # # 过去的12周
    # res_week = []
    # for w_each in _time.get_week():
    #     week_start_time = int(time.mktime(time.strptime(w_each[-1], "%Y-%m-%d")))
    #     week_end_time = int(time.mktime(time.strptime(w_each[0], "%Y-%m-%d")))
    #     res_week.append(count_number(week_start_time, week_end_time))
    #
    # # 过去的12个月
    # res_mon = []
    # for index, each in enumerate(_time.get_mon()[:-1]):
    #     mon_start_time = int(time.mktime(time.strptime(_time.get_mon()[index + 1], "%Y-%m-%d")))
    #     mon_end_time = int(time.mktime(time.strptime(each, "%Y-%m-%d")))
    #     res_mon.append(count_number(mon_start_time, mon_end_time))
    # return render(request, 'app_user.html', {'res_hour': res_hour, 'res_day': res_day, 'res_week': res_week, 'res_mon': res_mon})
    return render(request, 'app_user.html', {'res_day': res_day})



def score_content(start_time, end_time):
    data = models.ModelRunningRecord.objects.filter(
        Q(created_time__range=(start_time, end_time)), ~Q(module='simple_zhengxin_policy'),
        ~Q(module='policy'), ~Q(module='finally'), ~Q(module='old_user_model')
    )
    return data


def not_pass_content(start_time, end_time):
    data = models.ModelRunningRecord.objects.filter(
        Q(created_time__range=(start_time, end_time)), Q(module='simple_zhengxin_policy') |
        Q(module='policy') | Q(module='finally') | Q(module='old_user_model')
    )
    all_num = len(models.ModelRunningRecord.objects.filter(created_time__range=(start_time, end_time)))
    return data, all_num


# 模型评分
def mod_grade(request):
    try:
        score_select = request.GET['score_select']
        count_basis = request.GET['count_basis']
    except:
        score_select = 'pass'
        count_basis = 'ass'
    if score_select == 'pass':
        if count_basis == 'ass':
            data = GetDate()
            # # 过去的12时
            # res_hour = []
            # res_hour2 = []
            # for index, j in enumerate(data.get_hour()[:-1]):
            #     res, end_time = score_content(data.get_hour()[index + 1], j)
            #     alist_hour, pro_list_hour, end_time_hour = not_pass_content(data.get_hour()[index + 1], j)
            #     res_hour.append([res, end_time])
            #     res_hour2.append([alist_hour, pro_list_hour, time.strftime("%H:%M:%S", time.localtime(end_time_hour))])
            # response_hour = []
            # hour_data_list = []
            # for i in res_hour:
            #     h_data_list, res = do_count(i[:-1])
            #     if h_data_list:
            #         hour_data_list = h_data_list
            #     res.insert(0, time.strftime("%H:%M:%S", time.localtime(i[-1])))
            #     response_hour.append(res)

            # 过去12天
            res_day = []
            res_day2 = []
            print data.get_day()
            for index, each in enumerate(data.get_day()[:-1]):
                day_start_time = int(time.mktime(time.strptime(data.get_day()[index + 1], "%Y-%m-%d")))
                day_end_time = int(time.mktime(time.strptime(each, "%Y-%m-%d")))
                # 通过模型的，计算模型AVG MIN P5 P25 P50 P75 P95 MAN等值
                res_score = score_content(day_start_time, day_end_time)
                # module 为 policy/finally/old_user_module, simple_zhengxin_policy时统计策略命中量及命中率
                res_stratrgy = not_pass_content(day_start_time, day_end_time)
                a_set = set()
                for i in res_score:
                    a_set.add(i.module)
                a_list = sorted(list(a_set))
                res_json = {}
                for i in a_list:
                    res_json[i] = []
                for i in res_score:
                    res_json[i.module].append(i.score)
                res_day.append([day_end_time, res_json])
            response_day = []
            for i in res_day:
                for k, v in i[1].items():
                    res1 = {
                        'time': time.strftime('%Y-%m-%d', time.localtime(i[0])),
                        'module': k,
                        'data': [
                            round(numpy.average(v), 2),
                            round(numpy.min(v), 2),
                            round(numpy.percentile(v, 5), 2),
                            round(numpy.percentile(v, 25), 2),
                            round(numpy.percentile(v, 50), 2),
                            round(numpy.percentile(v, 75), 2),
                            round(numpy.percentile(v, 95), 2),
                            round(numpy.max(v), 2),
                        ]
                    }
                    response_day.append(res1)
            # a_set = set()
            # for i in res_day:
            #     for j in i:
            #         a_set.add(j.module)
            # a_list = sorted(list(a_set))
            # res_json = {}
            # for i in a_list:
            #     res_json[i] = []
            # for ixdex, i in enumerate(res_day):
            #     for j in i:
            #         res_json[j.module].append(j.score)
            print 'response_day'
            print response_day
            # print res1
            # print len(res1)
            # print len(zip(*res1))

            ## 测试数据
            aa = [
                {'module': 'v2', 'test_data': [0.1, 0.01, 0.02, 0.04, 0.08, 0.13, 0.28, 0.42]},
                {'module': 'v1', 'test_data': [553.22, 385.0, 443.6, 505.0, 554.0, 602.0, 651.0, 692.0]}
                ]
            return render(request, 'mod_user.html', {'response_day': response_day,
                                                      'option': count_basis,
                                                      'res_test': aa})
        else:
            return render(request, 'mod_user.html', {'option': count_basis})


def mod_info(request):
    return render(request, 'mod_grade.html', {})

def app_info(request):
    return render(request, 'app_pass.html', {})

    #     alist_day, pro_list_day, end_time_day = not_pass_content(day_start_time, day_end_time)
    #     res_day.append([res, end_time])
    #     res_day2.append([alist_day, pro_list_day, time.strftime("%Y-%m-%d", time.localtime(end_time_day))])
    # response_day = []
    # day_data_list = []
    # for i in res_day:
    #     d_data_list, res = do_count(i[:-1])
    #     if d_data_list:
    #         day_data_list = d_data_list
    #     res.insert(0, time.strftime("%Y-%m-%d", time.localtime(i[-1])))
    #     response_day.append(res)
    # print response_day
    # return render(request, 'mod_grade.html', {'response_day': response_day[::-1], 'res_day2': res_day2})

    # # 过去的12周
    # res_week = []
    # for w_each in data.get_week():
    #     week_start_time = int(time.mktime(time.strptime(w_each[-1], "%Y-%m-%d")))
    #     week_end_time = int(time.mktime(time.strptime(w_each[0], "%Y-%m-%d")))
    #     res, end_time = score_content(week_start_time, week_end_time)
    #     res_week.append([res, end_time])
    # response_week = []
    # week_data_list = []
    # for i in res_week:
    #     w_data_list, res = do_count(i[:-1])
    #     if w_data_list:
    #         week_data_list = w_data_list
    #     res.insert(0, time.strftime("%Y-%m-%d", time.localtime(i[-1])))
    #     response_week.append(res)
    # print 'response_week'
    # print response_week

    # # 过去的12个月
    # res_mon = []
    # for index, each in enumerate(data.get_mon()[:-1]):
    #     mon_start_time = int(time.mktime(time.strptime(data.get_mon()[index + 1], "%Y-%m-%d")))
    #     mon_end_time = int(time.mktime(time.strptime(each, "%Y-%m-%d")))
    #     res, end_time = score_content(mon_start_time, mon_end_time)
    #     res_mon.append([res, end_time])
    # response_mon = []
    # mon_data_list = []
    # for i in res_mon:
    #     m_data_list, res = do_count(i[:-1])
    #     if m_data_list:
    #         mon_data_list = m_data_list
    #     res.insert(0, time.strftime("%Y-%m-%d", time.localtime(i[-1])))
    #     response_mon.append(res)
    #
    # desc_list = model_feature()
    # _list = []
    # for j in desc_list:
    #     _list.append(j.description)
    # for i in res_day2:
    #     num_list = zip(_list, zip(*i[:2]))

    # return render(request, 'mod_grade.html', {'response_hour': response_hour, 'response_day': response_day[::-1],
    #                                           'response_week': response_week, 'response_mon': response_mon,
    #                                           'mod_h': hour_data_list, 'mod_d': day_data_list, 'mod_w': week_data_list,
    #                                           'mod_m': mon_data_list, 'res_day2': res_day2, 'num_list': num_list})
