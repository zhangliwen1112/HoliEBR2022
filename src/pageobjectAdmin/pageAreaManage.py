# -*- coding: utf-8 -*- 
# @Time : 2021/1/18 10:56 
# @Author : 张丽雯 
# @File : pageAreaManage.py 
# @中文描述 :  工厂模型-区域管理页面
from src.public.common.Login import *
from ElementAdmin.factorymodePage import *


# 进入工厂模型-区域管理页面
def login_Area_Manage():
    new_click(Factory_Mode)
    new_click(Area_Manage)
    print('工厂模型-区域管理页面！')


# 新增区域
def Area_Manage_add(area_code, area_name):
    new_click(add)
    new_type(Code, area_code)
    new_type(Name, area_name)
    new_click(submit)
    print('区域新增成功！')
    sleep(2)


# 编辑区域
def Area_Manage_edit(area_name):
    new_click(First)
    new_click(edit)
    new_type(Name, area_name)
    new_click(submit)
    sleep(2)


# 删除区域
def Area_Manage_delete():
    new_click(delete)
    new_click(delete_submit)
    sleep(2)
