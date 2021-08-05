#coding:utf-8
# from logging.config import fileConfig
from get_path import *
import logging
import logging.config

def get_logger(name=None):
    # CONFIG = '../config/log.conf'
    logging.config.fileConfig(log_config_path)
    # print("日记存放目录：",log_config_path)
    logger = logging.getLogger(name)
    # logger.info("jjfsdf")
    return logger



if __name__=="__main__":
    print(log_config_path)
    # log = get_logger("root")
    # log.info("hhhh3123")
    logger = get_logger()
    logger.info("jkfsdfsd")
