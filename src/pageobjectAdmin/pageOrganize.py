# -*- coding: utf-8 -*- 
# @Time : 2021/1/19 16:30 
# @Author : 张丽雯 
# @File : pageOrganize.py 
# @中文描述 :  组织机构

from src.public.common.Login import *
from ElementAdmin.organizePage import *


# 进入外部设备页面
def login_organize_manage():
    new_click(organize)
    print('进入组织机构页面！')


# 新增企业
def organize_add_orgcom(name, code, type):
    new_click(o_add)
    ele = new_find_elements(input_text)
    new_type_ele(ele[0], name)
    new_type_ele(ele[1], code)
    if type == '公司':
        new_click(OrganType2)
    else:
        new_click(OrganType3)
    new_click(OrganUpper)
    new_click(Upper1)
    # new_click(Upper2)
    ele = new_find_elements(add_submit)
    new_click_ele(ele[2])


# 编辑企业
def organize_edit_orgcom(name, type):
    # new_click(group)
    new_click(company1)
    # new_click(company1_1)
    new_click(o_edit)
    ele = new_find_elements(input_text)
    new_type_ele(ele[0], name)
    if type == '公司':
        new_click(OrganType2)
    else:
        new_click(OrganType3)
    new_click(OrganUpper)
    new_click(Upper1)
    # new_click(Upper2)
    ele = new_find_elements(add_submit)
    new_click_ele(ele[2])


# 删除新增企业
def organize_delete_orgcom():
    new_click(company1)
    new_click(o_delete)
    new_click(delete_submit)


# 刷新左侧组织机构树表结构
def organize_refresh_orgcom():
    new_click(o_refresh)


# 新增用户名
def organize_user_add(name, code, tel, status, male):
    # new_click(company1)
    new_click(add)
    ele = new_find_elements(input_text)
    new_type_ele(ele[0],name)
    new_type_ele(ele[1], code)
    new_type_ele(ele[2], tel)
    new_click(add_UserSta)
    if status == '离职':
        new_click(UserSta_off)
    else:
        new_click(UserSta_online)
    if male == '男':
        new_click(UserMale1)
    else:
        new_click(UserMale2)
    new_click(UserDate)
    sleep(1)
    new_click(UserDate_first)
    new_click(UserOrg)
    ele1 = new_find_elements(add_submit)
    new_click_ele(ele1[4])


# 修改新增的用户
def organize_user_edit(name, tel, status):
    new_click(edit)
    ele = new_find_elements(input_text)
    new_type_ele(ele[0], name)
    new_type_ele(ele[1], tel)
    new_click(edit_UserSta)
    if status == '离职':
        new_click(UserSta_off)
    else:
        new_click(UserSta_online)
    # new_click(UserOrg)
    sleep(2)
    ele1 = new_find_elements(add_submit)
    new_click_ele(ele1[4])


# 删除增加的用户
def organize_user_delete():
    new_click(delete)
    new_click(DetUser_submit)


# 刷新列表
def organize_user_refresh():
    new_click(refresh)
