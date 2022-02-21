# -*- coding: utf-8 -*- 
# @Time : 2021/1/19 11:50 
# @Author : 张丽雯 
# @File : pageSectionManage.py 
# @中文描述 :  区段管理界面
from src.public.common.Login import *
from ElementAdmin.factorymodePage import *

# 进入工厂模型-区段管理页面
def login_section_manage():
    new_click(Factory_Mode)
    new_click(Section_Manage)
    print('工厂模型-区段管理页面！')

# 新增区段
def section_manage_add(code,name,type='生产',type2 = '原材料'):
    new_click(add)
    new_type(Code,code)
    new_type(Name,name)
    new_click(section_type)
    if type == '仓库':
        new_click(section_type2)
        new_click(store_type)
        if type2 == '原材料':
            new_click(store_type1)
        elif type2 == '半成品':
            new_click(store_type2)
        elif type2 == '包材':
            new_click(store_type3)
        else:
            new_click(store_type4)
    else:
        new_click(section_type1)
    new_click(submit)
    sleep(1)

#编辑区段
def section_manage_edit(name,type='生产',type2 = '原材料'):
    new_click(First)
    new_click(edit)
    new_type(Name,name)
    new_click(section_type)
    if type == '仓库':
        new_click(section_type2)
        new_click(store_type)
        if type2 == '原材料':
            new_click(store_type1)
        elif type2 == '半成品':
            new_click(store_type2)
        elif type2 == '包材':
            new_click(store_type3)
        else:
            new_click(store_type4)
    else:
        new_click(section_type1)
    new_click(submit)
    sleep(1)

# 删除区域
def section_manage_delete():
    new_click(delete)
    new_click(delete_submit)
    sleep(1)
