# -*- coding: utf-8 -*- 
# @Time : 2020/11/18 14:12 
# @Author : 张丽雯 
# @File : pageattributivelist.py 
# @中文描述 :  属性列表
from ElementApp.AttributiveListPage import *
from src.public.common.Login import *
from DataApp.AttributivelistData import *

# 进入属性列表界面
def login_attributive_list():
    new_click(device)
    new_click(attributive)
    print('进入属性列表界面')

#点击编辑按钮
def edit_button():
    new_click(edit)

#点击新增、编辑确定按钮
def submit_button():
    new_click(submit)

# 新增属性
def add_attributive_list(attributive_code, attributive_type, attributive_name):
    new_click(add)
    new_type(code, attributive_code)
    new_click(type)
    if attributive_type in '文本':
        new_click(text_type)
        new_type(name, attributive_name)
        new_type(text, '文本最大长度测试')
    if attributive_type == '数字':
        new_click(num_type)
        new_type(name, attributive_name)
        new_click(select1)
        new_click(select2)
        new_click(select3)
    if attributive_type == '列表':
        new_click(list_type)
        new_type(name, attributive_name)
        new_click(select1)
        new_click(select2)
        new_click(select3)
        new_click(select4)
    if attributive_type == '状态':
        new_click(status_type)
        new_type(name, attributive_name)
        add_status(code_value, code_name, select_rule)
    new_click(submit)


# 状态属性新增
def add_status(code_value, code_name, select_rule):
    new_click(status_button)
    new_type(status_code, code_value)
    new_type(status_name, code_name)
    new_click(status_select1)
    new_click(status_select2)
    new_click(status_select3)
    new_click(status_submit)
    new_click(rule_button)
    new_click(start_code)
    new_click(start_code1)
    new_click(rule_type)
    if select_rule in '超过有效期':
        new_click(rule_type1)
    if select_rule in '生产步骤':
        new_click(rule_type2)
    if select_rule in '超过最大循环数':
        new_click(rule_type3)
    new_click(end_code)
    new_click(end_code1)
    new_click(rule_submit)


# 编辑状态属性的状态信息
def edit_status(code_name):
    new_click(status_first)
    new_click(status_edit)
    new_type_double(status_name, code_name)
    new_click(status_submit)

# 删除状态属性的状态信息
def delete_status(isdelete):
    new_click(status_first)
    new_click(status_delete)
    sleep(2)
    if isdelete == '否':
        new_click(cancle_button)
    else:
        new_click(yes_button)

# 编辑状态转换信息
def edit_rule(select_rule):
    new_click(rule_first)
    new_click(rule_edit)
    new_click(rule_type)
    if select_rule in '超过有效期':
        new_click(rule_type1)
    if select_rule in '生产步骤':
        new_click(rule_type2)
    if select_rule in '超过最大循环数':
        new_click(rule_type3)
    new_click(rule_submit)

# 删除状态属性的状态信息
def delete_rule():
    new_click(rule_first)
    new_click(rule_delete)
    new_click(yes_button)

# 编辑属性
def edit_attributive_list(attributive_name):
    new_click(edit)
    new_type_double(name, attributive_name)
    new_click(submit)


# 复制
def copy_attributive_list(attributive_code, attributive_name):
    new_click(copy)
    sleep(2)
    new_type(code, attributive_code)
    new_type_double(name, attributive_name)
    new_click(submit)


# 失效
def noeffect_attributive_list():
    new_click(noeffect)
    new_click(yes_button)


# 生效
def effect_attributive_list():
    new_click(effect)
    new_click(yes_button)


# 筛选
def select_attributive_list(nametext):
    new_click(select)
    new_click(select_name)
    new_type_double(name_text, nametext)
