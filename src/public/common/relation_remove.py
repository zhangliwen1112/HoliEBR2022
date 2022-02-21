# -*- coding: utf-8 -*- 
# @Time : 2021/1/20 14:08 
# @Author : 张丽雯 
# @File : relation_remove.py 
# @中文描述 :关联、去关联，（企业、区域、区段、厂区、工作中心模块）

from ElementAdmin.factorymodePage import *
from src.public.FunctionSet import *

# 关联-关联第一个
def Manage_relation():
    new_click(ralated)
    new_click(movefirst)
    new_click(moveleft)
    new_click(submit)
    time.sleep(2)

# 去关联-去关联第一个
def Manage_remove():
    new_click(ralated)
    new_click(removefirst)
    new_click(moveright)
    new_click(submit)
    time.sleep(2)