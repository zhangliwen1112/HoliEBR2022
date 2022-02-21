# -*- coding: utf-8 -*- 
# @Time : 2021/1/18 17:46 
# @Author : 张丽雯 
# @File : pageFactoryManage.py 
# @中文描述 :  工厂模型-厂区管理页面
from src.public.common.Login import *
from ElementAdmin.factorymodePage import *


# 进入工厂模型-厂区管理页面
def login_Factory_Manage():
    new_click(Factory_Mode)
    new_click(Factory_Manage)
    print('工厂模型-厂区管理页面！')

# 新增厂区
def Factory_Manage_add(code,name):
    new_click(add)
    new_type(Code,code)
    new_type(Name,name)
    new_click(submit)
    sleep(2)


# 编辑厂区
def Factory_Manage_edit(Factory_Name,Adr1='',Adr2='',Adr3='',Adr4=''):
    new_click(edit)
    new_type(Name,Factory_Name)
    new_type(Factory_Adr1,Adr1)
    new_type(Factory_Adr2, Adr2)
    new_type(Factory_Adr3, Adr3)
    new_type(Factory_Adr4, Adr4)
    new_click(submit)
    sleep(1)

# 删除区域
def Factory_Manage_delete():
    new_click(delete)
    new_click(delete_submit)
    sleep(1)

