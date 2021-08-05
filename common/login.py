#coding:utf-8
import json

from APIbase.base_request import send
from common.get_logger import get_logger
from common.read_data import read_excel
from get_path import *

logger = get_logger()

def login():
    re_data = read_excel(request_data,"login")[0]
    logger.info(f"登录的数据{re_data}")
    url = re_data["url"]
    method = re_data["method"]
    headers = eval(re_data["headers"])
    body=eval(re_data["body"])
    try:
        res = send(url=url,method=method,headers=headers,json=body,verify=False)
        logger.info(f"登录返回的结果{res}")
        session = res["data"]["session"]
        logger.info(f"登录的session{session}")
        res_account = res["data"]["account"]
        if body["account"]== res_account:
            return session
    except Exception as e:
        logger.error(e)





if __name__=="__main__":
    login()