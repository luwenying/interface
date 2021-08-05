#coding:utf-8
import os

base_path = os.path.dirname(__file__)
config_path = base_path+"/config"
log_config_path = config_path+"/log.conf"
log_path = base_path+"/log"
report_path = base_path+"/report"
result_path = base_path+"/result"
data_path = base_path+"/data"
#管理端请求数据
iflying_manage_data = data_path+"/iflying_manage_data.xlsx"
#商户端请求数据
iflying_data = data_path+"/iflying_data.xlsx"
db_config = data_path+"/db.yaml"

# print(config_path)