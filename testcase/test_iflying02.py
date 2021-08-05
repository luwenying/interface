#coding:utf-8

import sys

import pytest

from common.read_data import *
from get_path import *
from common.get_logger import get_logger
from APIbase.base_request import send

logger = get_logger()
class TestIflying02():

    requsts_data = read_excel(iflying_data, "api")
    row = list(range(2, len(requsts_data)+2))
    datas = list(zip(requsts_data, row))
    logger.info(f"全部请求数据{datas}")
    # response_list = []

    def setup_class(self):
        const_data = read_const_excel(iflying_data,"const")
        self.environment = const_data["environment"]
        self.session = const_data["session"]
        self.account = const_data["account"]
        self.merchantId = const_data["merchantId"]
        self.operatorId = const_data["operatorId"]
        self.body01 = {
            "session":self.session,"account":self.account,"merchantId":self.merchantId,"operatorId":self.operatorId,
            "platform":"iflying"
        }


    def common(self,data,row):
        # row = 2
        # for data in self.requsts_data:
            # if data["testcase"] == funcname:
        url = data["url"]
        code = data["code"]
        headers = {"Content-Type": "application/json; charset=UTF-8"}
        body = data["body"]
        body02 = {}
        assert_data = data["assert_data"]
        assert_type = data["assert_type"]

        if data["headers"]:
            headers = eval(data["headers"])
        if body:
            body02 = eval(data["body"])
        method = data["method"]
        if code == 1:
            url = self.environment + data["url"]
            body02["method"] = data["url"]
            body = dict(body02, **self.body01)
        else:
            body = body02

        logger.info(body)
        res = None
        if method=="post":
            res = send(url=url, method=method, headers=headers, json=body, verify=False)

        elif method=="get":
            res = send(url=url, method=method, headers=headers, params=body, verify=False)
        # self.response_list.append(res)
        logger.info(f"接口返回数据{res}")
        write_into_excel(iflying_data, "api", row, 12, str(res))
        # self.commom_assert(res,row,assert_type,assert_data)
        #断言
        assert_type = eval(assert_type)
        logger.info(f"——————————————————断言的assert_type:{assert_type}")
        logger.info(f"——————————————————assert_data:{assert_data}")
        assert_result = assert_data in assert_type
        print(assert_result)
        if assert_result:
            write_into_excel(iflying_data, "api", row, 13, "pass")
            assert True
        else:
            write_into_excel(iflying_data, "api", row, 13, "fail")
            assert False


    @pytest.mark.parametrize("data,row",datas)
    def testall(self,data,row):
        self.common(data,row)

