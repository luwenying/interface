#coding:utf-8
import requests
from requests.packages import urllib3
from common.get_logger import get_logger

def send(**kwargs):
    logger = get_logger()
    urllib3.disable_warnings()
    try:
        session = requests.session()
        return session.request(**kwargs).json()
    except Exception as e:
        logger.error(e)




if __name__=="__main__":

    url = "https://admindev.robot.com/iflying/api/route/rest/merchant_platform_list"
    # data = {"method":"merchant_role_list","session":"user_session_cache:business:f0dcaabd-d71e-4e37-992f-65f880ce4e92","v":"1.0","account":"woVVL9DgAAo8JcQTSAigfzKxNYA7WemQ",
    #         "operatorId":"1924093577896263681","merchantId":"1924093577040625664","platform":"iflying","data":{"currentPage":1,"pageSize":10}}
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
        "Referer":"https://admindev.robot.com",
        "Origin":"https://admindev.robot.com",
        "Host": "iflying - manage - dev.zhilingsd.com",
        "Content-Type":"application/json; charset=UTF-8",
        "Connection":"keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Accept": "application/json, text/plain,*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Content-Length": "293",
    }
    data = {"data":{"currentPage":1,"pageSize":10,"platform":"iflying"},"method":"merchant_platform_list","platform":"iflying",
            "session":"user_session_cache:manage:86f0c796-5a45-485e-ab55-30d2e3c0f59d","v":"1.0"}
    res = send(url=url,method="post",headers=headers,json=data,verify=False)
    print(res)








