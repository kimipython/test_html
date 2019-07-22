#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import requests

url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
params = {
    'mobilephone':'15814447890',
    'pwd':'123456'
}
res = requests.get(url,params=params)
print('查看响应码{}'.format(res.status_code))
print(res.text)
# print(eval(res.text))
print('查看响应头{0}'.format(res.headers))
print('查看json数据{0}'.format(type(res.json())))
print('查看json数据{0}'.format(res.json()['code']))
print(res.cookies)
print(res.url)
cookies = res.cookies

#  post

# url = 'http://test.lemonban.com/futureloan/mvc/api/member/recharge'
# params1 = {
#     'mobilephone':'15814447890',
#     'amount':100,
# }
# res1 = requests.post(url,data=params1,cookies=cookies)
# print(res1.text)


# a = eval(res1.text)
# json1 = json.loads(res1.text)
# dict = json.dumps(json1)
# print(a)



# url = 'https://kennethreitz.org'
# res2 = requests.get('https://kennethreitz.org', cert=('/path/client1.csr', '/path/client1.key'))
# print(res2)