# -*- coding: utf-8 -*- 
# @Time : 2021/1/19 11:22 
# @Author : 张丽雯 
# @File : pageLocationManage.py 
# @中文描述 :  位置管理页面

from src.public.common.Login import *
from ElementAdmin.factorymodePage import *


# 进入工厂模型-位置管理页面
def login_Location_Manage():
    new_click(Factory_Mode)
    new_click(Location_Manage)
    print('工厂模型-位置管理页面！')

# 新增位置
def Location_Manage_add(location_code,location_name):
    new_click(add)
    new_type(Code,location_code)
    new_type(Name,location_name)
    new_click(submit)
    sleep(1)


# 编辑位置
def Location_Manage_edit(location_name):
    new_click(First)
    new_click(edit)
    sleep(1)
    new_type(Name,location_name)
    new_click(submit)
    sleep(1)

# 删除位置
def Location_Manage_delete():
    new_click(First)
    new_click(delete)
    new_click(delete_submit)
    sleep(2)
