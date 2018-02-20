# coding=utf-8
from django.shortcuts import render

# Create your views here.
import json
import time
import urllib
import urllib2
import collections
import hashlib

from search_info import models
from login.models import Pro
from django.contrib.auth.models import User

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def auth(func):
    def inner(request, *args, **kwargs):
        v = request.COOKIES.get('username')
        if not v:
            # return redirect('/login')
            return func(request, *args, **kwargs)
        return func(request, *args, **kwargs)
    return inner


def post(req_url, req_data, timeout=10):
    if isinstance(req_data, dict):
        req_data = urllib.urlencode(req_data)
    request = urllib2.Request(url=req_url, data=req_data)
    return urllib2.urlopen(request, timeout=timeout)


def __params_encode(params, secret):
    ordered_params = collections.OrderedDict(sorted(params.items(), key=lambda t: t[0]))
    items = []
    for key in ordered_params.keys():
        items.append(key + '=' + str(ordered_params[key]))
    items.append(secret)
    params_str = '&'.join(items)
    print params_str
    return hashlib.md5(params_str.encode('utf-8')).hexdigest()


def add_sign(params, secret):
    sign = __params_encode(params, secret)
    params['sign'] = sign
    return params


def search(request):
    print('search')
    return render(request, 'search.html', {'res': {}})


def search_info(request):
    try:
        user_info = {}
        username = request.COOKIES.get('username')
        user_id = User.objects.get(username=username).id
        app_id = Pro.objects.get(user_id=int(user_id)).app_id
        request.encoding = 'utf-8'
        user_info['name'] = request.GET['name']
        user_info['idcard'] = request.GET['idcard']
        user_info['phone'] = request.GET['phone']
        user_info['service'] = request.GET['service']
        # user_info['appid'] = int(appid)
        user_info['appid'] = 100256
        data = {
            'appid': user_info['appid'],
            'idcard': user_info['idcard'],
            'phone': user_info['phone'],
            'name': user_info['name'],
            'service': user_info['service'],
            'report_id': '',
            'function_id': 3,
        }
        if user_info['name']:
            add_sign(data, 'a1a8fd0bef522844')
            res = post('http://10.141.148.247/api/get_data', data).read()
            if res:
                res_new = json.loads(res)
                res_data = res_new.get('data')
                response = {}
                if isinstance(res_data, basestring):
                    res_data = json.loads(res_data)
                if res_data.get('is_black') == 1:
                    response['is_black'] = u'是'
                else:
                    response['is_black'] = u'否'
                response['model_score'] = res_data.get('model_score', '')
                response['credit_score'] = res_data.get('credit_score', '')
                response['sub_features'] = res_data.get('sub_features', '')
                report_id = res_data.get('report_id', '')
                # report_id = '100273151599924881650'
                data2 = {
                    'appid': user_info['appid'],
                    'service': 'S23',
                    'report_id': report_id,
                    'function_id': 2,
                }
                add_sign(data2, 'a1a8fd0bef522844')
                res = post('http://10.141.148.247/api/get_data', data2).read()
                data3 = json.loads(res)['data']
                if data3:
                    response['report_id'] = report_id
                else:
                    response['report_id'] = '0'
                user_info['report_id'] = report_id
                user_info['create_time'] = int(time.time())
                user_info['search_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                # 查询历史写入数据库
                models.SearchHistory.objects.create(**user_info)
                return render(request, 'search.html', {'res': response, 'userinfo': user_info})
            else:
                print 'json-loads res ------None'
                return render(request, 'search.html', {'res': {}})
        else:
            return render(request, 'search.html', {'res': {}})

    except:
        return render(request, 'search.html', {'res': {}})
