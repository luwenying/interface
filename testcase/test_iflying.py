#coding:utf-8
import inspect
import sys
from common.read_data import *
from get_path import *
from common.get_logger import get_logger
from APIbase.base_request import send
from hamcrest import  *


logger = get_logger()
class TestIflying():

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
        self.requsts_data = read_excel(iflying_data,"api")


    def common(self,funcname):
        for data in self.requsts_data:
            if data["testcase"] == funcname:
                url = self.environment + data["url"]
                headers = {"Content-Type":"application/json; charset=UTF-8"}
                if data["headers"]:
                    headers = eval(data["headers"])
                body02={}
                if data["body"]:
                    body02 = eval(data["body"])
                body02["method"] = data["url"]
                body = dict(body02, **self.body01)
                method = data["method"]
                assert_data = data["assert_data"]
                logger.info(body)
                res = send(url=url, method=method, headers=headers, json=body, verify=False)
                logger.info(res)
                return res,assert_data

    def commom_assert(self,res,assert_data,row):
        write_into_excel(iflying_data, "api", row, 10, str(res))
        if res == assert_data:
            write_into_excel(iflying_data, "api", row, 11, "pass")
            assert True
        else:
            write_into_excel(iflying_data, "api", row, 11, "fail")
            assert False

    def test_get_merchant_industry_tree(self):
        """获取商户的已分配的行业"""
        funcname= sys._getframe().f_code.co_name
        res,assert_sql = self.common(funcname)
        assert_sql = assert_sql.replace("$merchant_id",self.merchantId)
        res_industry_id_list = [i["id"] for i in res["get_merchant_industry_tree_response"]]
        db_industry_id_list = [str(i["industry_id"])for i in con_mysql("merchant_center","selectall",assert_sql)]
        logger.info(f"接口返回行业id{res_industry_id_list}")
        logger.info(f"数据库查询到的行业id{db_industry_id_list}")
        write_into_excel(iflying_data,"api",2,10,str(res))
        # assert_res = assert_that(res_industry_id_list,equal_to(db_industry_id_list))
        if res_industry_id_list.sort()==db_industry_id_list.sort():
            write_into_excel(iflying_data, "api", 2, 11, "pass")
            write_into_excel(iflying_data, "api", 2, 12,str({"industry_id":db_industry_id_list}))
            assert True
        else:
            write_into_excel(iflying_data, "api", 2, 11, "fail")
            assert False



    def test_script_category_list(self):
        """获取商户的全部场景"""
        funcname= sys._getframe().f_code.co_name
        res,assert_sql = self.common(funcname)
        assert_sql = assert_sql.replace("$merchant_id", self.merchantId)
        res_list = [i["id"] for i in res["script_category_list_response"]]
        db_list = [str(i["id"]) for i in con_mysql("iflying", "selectall", assert_sql)]
        logger.info(f"接口返回场景id{res_list}")
        logger.info(f"数据库查询到的场景id{db_list}")
        write_into_excel(iflying_data, "api", 3, 10, str(res))
        if res_list.sort() == db_list.sort():
            write_into_excel(iflying_data, "api", 3, 11, "pass")
            write_into_excel(iflying_data, "api", 3, 12, str({"category_id": db_list}))
            assert True
        else:
            write_into_excel(iflying_data, "api", 3, 11, "fail")
            assert False

    def test_script_category_add(self):
        """增加场景"""
        funcname = sys._getframe().f_code.co_name
        res, assert_data = self.common(funcname)
        write_into_excel(iflying_data, "api", 4, 10, str(res))
        if res == {'script_category_add_response': ''}:
            write_into_excel(iflying_data, "api", 4, 11, "pass")
            assert True
        else:
            write_into_excel(iflying_data, "api", 4, 11, "fail")
            assert False

    def test_script_category_update(self):
        funcname = sys._getframe().f_code.co_name
        res, assert_data = self.common(funcname)
        write_into_excel(iflying_data, "api",5, 10, str(res))
        if res == {'script_category_update_response': ''}:
            write_into_excel(iflying_data, "api", 5, 11, "pass")
            assert True
        else:
            write_into_excel(iflying_data, "api", 5, 11, "fail")
            assert False


    def test_script_config_synQa(self):
        funcname = sys._getframe().f_code.co_name
        res, assert_data = self.common(funcname)
        assert_data = {'script_config_synQa_response': ''}
        self.commom_assert(res,assert_data,6)





