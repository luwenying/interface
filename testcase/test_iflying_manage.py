#coding:utf-8
import json

from APIbase.base_request import send
from common.get_logger import get_logger
from common.read_data import read_excel
from get_path import *
from common.login import login
import ast


class TestIfyingManage():

    def setup_class(self):
        # self.session = login()
        self.logger = get_logger()


    def test_ifying_manage(self):
        session = {"session": "user_session_cache:manage:689725e4-54eb-462f-8805-0c9916b16d87"}
        data_list = read_excel(iflying_manage_data,"api")
        self.logger.info(f"test_ifying_manage的数据{data_list}")
        for data in data_list:
            url = None
            method = None
            headers = None
            body = None
            if data["url"]:
                url = data["url"]
            if data["method"]:
                method = data["method"]
            if data["headers"]:
                headers = ast.literal_eval(data["headers"])
            if data["body"]:
                body = ast.literal_eval(data["body"])
                # body["session"] = self.session
                body = dict(body,**session)
                # print(body)
                # print(type(body))
                self.logger.info(f"body:{body}")
            try:
                print(body)
                res = send(url=url, method=method, headers=headers, json=body, verify=False)
                self.logger.info(f"返回的结果{res}")
                # session = res["data"]["session"]
                # self.logger.info(f"登录的session{session}")
                # res_account = res["data"]["account"]
                # if body["account"] == res_account:
                #     return res
            except Exception as e:
                print(e)
                # self.logger.error(e.__str__())


