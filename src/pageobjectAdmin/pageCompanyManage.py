# -*- coding: utf-8 -*- 
# @Time : 2021/1/18 16:37 
# @Author : 张丽雯 
# @File : pageCompanyManage.py 
# @中文描述 :  企业管理界面
from src.public.common.Login import *
from ElementAdmin.factorymodePage import *

# 进入工厂模型-企业管理页面
def login_Company_Manage():
    new_click(Factory_Mode)
    new_click(Company_Manage)
    print('工厂模型-企业管理页面！')


# 新增企业
def Company_Manage_add(company_code, company_name):
    new_click(add)
    new_type(Code, company_code)
    new_type(Name, company_name)
    sleep(1)
    new_click(submit)
    sleep(1)


# 编辑企业
def Company_Manage_edit(company_name):
    new_click(First)
    new_click(edit)
    new_type(Name,company_name)
    sleep(1)
    new_click(submit)
    sleep(1)


# 删除区域
def Company_Manage_delete():
    new_click(delete)
    new_click(delete_submit)
