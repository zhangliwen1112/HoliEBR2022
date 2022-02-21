# -*- coding: utf-8 -*- 
# @Time : 2020/11/19 9:37 
# @Author : 张丽雯 
# @File : pageEqpcategory.py
# @中文描述 :  接口管理-设备类别接口

from ElementApp.EqpcategoryPage import *
from src.public.common.Login import *


# 进入接口管理-设备类别接口界面
def login_Eqp_Category():
    new_click(device)
    new_click(eqp)
    new_click(eqpcategory)
    print('进入接口管理-设备类别接口')


# 筛选类别
def search_Eqp_Category(text):
    new_click(select)
    new_click(select_code)
    new_type(code_text, text)


# 关闭退出类别界面
def close_Eqp_Category():
    new_click(close)


# 进入编辑页面
def edit_Eqp_Category():
    new_click(edit)
    sleep(2)
    new_click(yes_button)


# 编辑页面确定退出
def edit_out_Eqp_Category():
    new_click(submit)


# 在编辑页面新增接口
def edit_add_Eqp(eqpcode, eqpname):
    new_click(add)
    new_type(eqp_code, eqpcode)
    new_type(eqp_name, eqpname)


# 切换到输出tab页
def change_Eqp_out():
    new_click(eqp_out)


# 新增输出类别接口
def add_Eqp_out(code, name, type):
    new_click(out_add)
    new_type(out_code, code)
    new_type(out_name, name)
    new_click(out_type)
    if type in '文本':
        new_click(out_type1)
    else:
        new_click(out_type2)
    new_click(out_submit)


# 编辑输出接口
def edit_Eqp_out(name, type):
    new_click(out_edit)
    new_type(out_name, name)
    new_click(out_type)
    if type in '文本':
        new_click(out_type1)
    else:
        new_click(out_type2)
    new_click(out_submit)


# 删除输出接口
def delete_Eqp_out():
    new_click(out_delete)
    sleep(2)
    new_click(yes_button)
