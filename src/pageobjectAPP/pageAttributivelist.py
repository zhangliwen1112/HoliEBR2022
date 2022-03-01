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
def add_attributive_list(attributive_code, attributive_type, attributive_name,*args):
    new_click(add)
    sleep(1)
    field_text = new_find_elements(input_text)
    sleep(1)
    new_type_ele(field_text[0], attributive_code)
    new_click(type)
    if attributive_type in '文本':
        new_click(text_type)
        new_type_ele(field_text[1], attributive_name)
        new_type_ele(field_text[2], args[0])
    if attributive_type == '数字':
        new_click(num_type)
        new_type_ele(field_text[1], attributive_name)
        sleep(1)
        selections = new_find_elements(selection)
        new_click_ele(selections[0])
        new_click_ele(selections[1])
        new_click_ele(selections[2])
    if attributive_type == '列表':
        new_click(list_type)
        new_type_ele(field_text[1], attributive_name)
        sleep(1)
        selections = new_find_elements(selection)
        new_click_ele(selections[0])
        new_click_ele(selections[1])
        new_click_ele(selections[2])
        new_click_ele(selections[3])
    if attributive_type == '状态':
        new_click(status_type)
        new_type_ele(field_text[1], attributive_name)
        add_status(code_value, code_name, select_rule)
    new_click(submit)


# 状态属性新增
def add_status(code, name, select_rule):
    # 新增状态信息
    new_click(status_button)
    field_text = new_find_elements(input_text)
    sleep(1)
    new_type_ele(field_text[2], code)
    new_type_ele(field_text[3], name)
    new_click(status_select1)
    new_click(status_select2)
    new_click(status_select3)
    ele = new_find_elements(submit)
    new_click_ele(ele[1])
    # 新增状态转换信息
    new_click(rule_add)
    select_button = new_find_elements(select)
    new_click_ele(select_button[3])
    new_click(select_option)
    new_click_ele(select_button[4])
    if select_rule in '超过有效期':
        new_click(rule_type1)
    if select_rule in '生产步骤':
        new_click(rule_type2)
    if select_rule in '超过最大循环数':
        new_click(rule_type3)
    new_click_ele(select_button[5])
    new_click(select_option)
    sleep(1)
    ele = new_find_elements(submit)
    new_click_ele(ele[1])


# 编辑状态属性的状态信息
def edit_status(code_name):
    new_click(status_first)
    new_click(status_edit)
    field_text = new_find_elements(input_text)
    sleep(1)
    new_type_double_ele(field_text[3], code_name)
    ele = new_find_elements(submit)
    new_click_ele(ele[1])


# 删除状态属性的状态信息
def delete_status(isdelete):
    new_click(status_first)
    sleep(1)
    new_click(status_delete)
    sleep(2)
    if isdelete == '否':
        new_click(cancle_button)
    else:
        new_click(yes_button)

# 编辑状态转换信息
def edit_rule(select_rule):
    first_row = new_find_elements(status_first)
    new_click_ele(first_row[1])
    edit = new_find_elements(status_edit)
    new_click_ele(edit[1])
    sleep(1)
    rule_type = new_find_elements(select)
    new_click_ele(rule_type[4])
    if select_rule in '超过有效期':
        new_click(rule_type1)
    if select_rule in '生产步骤':
        new_click(rule_type2)
    if select_rule in '超过最大循环数':
        new_click(rule_type3)
    ele = new_find_elements(submit)
    new_click_ele(ele[1])

# 删除状态属性的状态信息
def delete_rule():
    first_row = new_find_elements(status_first)
    new_click_ele(first_row[1])
    delete = new_find_elements(status_delete)
    new_click_ele(delete[1])
    new_click(yes_button)

# 编辑属性
def edit_attributive_list(attributive_name):
    new_click(edit)
    field_text = new_find_elements(input_text)
    new_type_double_ele(field_text[1], attributive_name)
    new_click(submit)


# 复制
def copy_attributive_list(attributive_code, attributive_name):
    new_click(copy)
    sleep(2)
    field_text = new_find_elements(input_text)
    new_type_double_ele(field_text[0], attributive_code)
    sleep(1)
    new_type_double_ele(field_text[1], attributive_name)
    new_click(submit)


# 失效
def noeffect_attributive_list():
    new_click(noeffect)
    new_click(yes_button)


# 生效
def effect_attributive_list():
    new_click(effect)
    new_click(yes_button)
