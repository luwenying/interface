#coding:utf-8
import datetime
import time

import requests
from requests.packages import urllib3
from hamcrest import *

urllib3.disable_warnings()


# session = requests.Session()
#
# login_url = "https://admintest.robot.com/api/manage/login"
# headers = {
#         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
#         "Referer":"https://admindev.robot.com",
#         "Origin":"https://admindev.robot.com",
#         "Host": "iflying - manage - dev.zhilingsd.com",
#         "Content-Type":"application/json; charset=UTF-8",
#         "Connection":"keep-alive",
#         "Sec-Fetch-Dest": "empty",
#         "Sec-Fetch-Mode": "cors",
#         "Sec-Fetch-Site": "same-origin",
#         "Accept": "application/json, text/plain,*/*",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": "zh-CN,zh;q=0.9",
#         "Content-Length": "46",
#         "sec-ch-ua":'"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"'
#     }
# login_body = {"account":"luwenying","password":"Aa123456."}
# # login_res = requests.request(url=login_url,method="post",headers=headers,json=login_body,verify=False)
# print(time.time())
# login_res = session.post(url=login_url,headers=headers,json=login_body,verify=False).json()
# print(login_res)
# login_session = login_res["data"]["session"]
# url = "https://admindev.robot.com/iflying/api/route/rest/merchant_platform_list"
# data  = {"method":"merchant_platform_list","session":login_session,"v":"1.0","platform":"iflying",
#          "data":{"platform":"iflying","currentPage":1,"pageSize":10}}
# res = session.post(url=url,headers=headers,json=data,verify=False)
# print(res.text)

url = "https://iflying-manage-test.zhilingsd.com/api/iflying/uploadAuthFile"
data = {"method":"/iflying/uploadAuthFile","session":"","account":"","operatorId":"","merchantId":"","platform":""}
file = {"file":("WW_verify_cdfgI8tLYIqSqeDk.txt",open("data/WW_verify_cdfgI8tLYIqSqeDk.txt","rb"),"txt")}

# res = requests.post(url=url,files=file,data=data)
# print(res.text)


headers = {"Content-Type":"application/json; charset=UTF-8"}
url2 = "https://admintest.robot.com/iflying/api/route/rest/manage_customer_upload"

content = str(list[open("data/哈哈.png","rb")])
# print(content)
data2 = {"method":"manage_customer_upload","platform":"iflying","session":"user_session_cache:manage:999b0d50-2c43-4592-aa06-14644dcd7241","v":"1.0",
         "data":{"content":content,"fileCRC":953045120,"fileName":"哈哈.png","fileNameExt":"png"}}

file2 = {"data":("哈哈.png",open("data/哈哈.png","rb"),"png")}

# res2 = requests.post(url=url2,headers=headers,json=data2,verify=False)
# print(res2.text)
list01 = ["3","4"]
list02 = [1,2]
new_list = list(zip(list01,list02))
print(new_list)

# for i in new_list:
#     print(i)

res = {'get_merchant_industry_tree_response': [{'industryName': '车险', 'creator': '1929083343159033857', 'deleted': 'normal', 'created': '2021-07-02 14:36:36', 'modifier': '1895509910324707329', 'modified': '2021-07-15 17:16:33', 'id': '1930235479895048192',
                                                 'industryDescription': '车险', 'parentId': '1930226466570633216', 'domainId': '1846750438053904384'}, {'industryName': '名车险', 'creator': '1895509910324707329', 'deleted': 'normal', 'created': '2021-07-19 14:43:49', 'modifier': '1895509910324707329',
                                                   'modified': '2021-07-19 14:43:49', 'id': '1954885185761705984', 'industryDescription': '', 'parentId': '1930226466570633216', 'domainId': '1833118121041330176'}]}

# print(res.keys())
assert_data = "get_merchant_industry_tree_response"
# assert assert_data in res.keys()
print(assert_data in res)
res2 = {'code': 200000, 'msg': '操作成功', 'sysTime': '1628071370748', 'data': {'id': None, 'url': ''}}

assert_data2 = "操作成功"
print(assert_data2 in res2.values())
res3 = {'error_response': {'msg': '该平台下已存在此角色。', 'code': '7002', 'sub_msg': '该平台下已存在此角色。', 'sub_code': '7002'}}
print(list(res3["error_response"].items()))
# print("7002" in list(res3["error_response"].values()))
# res4 = ['【奖牌】该标签组下--【金牌】标签已存在，不允许添加相同标签', '800002', '【奖牌】该标签组下--【金牌】标签已存在，不允许添加相同标签', '800002']
# assert_data4 = "800002"
# assert_result = assert_data4 in res4
# print(assert_result)
# if assert_data4 in res4:
#     print("pass")
kk = sql = ["select id role_id from merchant_role where merchant_id='$merchant_id';","select id from merchant_user_role_relate where merchant_id='$merchant_id';"]
if str(kk).find("$01"):
    kk = str(kk).replace("$merchant_id","kk")
kk = eval(kk)
print(kk)

if __name__=="__main__":
    # pytest.main(["-sv","pra.py"])
    pass