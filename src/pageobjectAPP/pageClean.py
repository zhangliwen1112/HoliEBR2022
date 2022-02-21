# -*- coding: utf-8 -*- 
# @Time : 2020/10/14 10:56 
# @Author : 张丽雯 
# @File : pageclean.py 
# @中文描述 :  清洁配置
from ElementApp.CleanPage import *
from src.public.common.Login import *
from src.public.common.elements import *


# 进入清洁配置界面


def login_clean():
    new_click(cleanmanage)
    new_click(clean)
    print('进入清洁配置页面')


# 新增清洁配置

def clean_add(code, name, ruletype='工单'):
    new_click(add)
    sleep(1)
    new_types(rulecode, 0, code)
    new_types(rulecode, 1, name)
    new_click(select_area)
    new_click(area1)
    new_click(select_ruletype)
    if ruletype in "工单":
        new_click(rule_type1)
    else:
        new_click(rule_type2)
    new_click(submit)
    sleep(1)

    # 异常判断
    if is_element_present(error_message):
        new_get_text(error_message)
        new_click(cancle)
    if is_element_present(error_message2):
        new_get_text(error_message2)
        new_click(cancle)


# 编辑清洁配置
def clean_edit(name, ruletype='工单'):
    new_click(edit)
    new_types(rulecode, 1, name)
    new_click(select_area)
    new_click(area1)
    new_click(select_ruletype)
    if ruletype in "工单":
        new_click(rule_type1)
    else:
        new_click(rule_type2)
    new_click(submit)
    sleep(1)

    # 异常判断
    if is_element_present(error_message):
        new_get_text(error_message)
        new_click(cancle)
    if is_element_present(error_message2):
        new_get_text(error_message2)
        new_click(cancle)


# 筛选
def clean_search_web(text):
    new_click(select)
    new_click(select_name)
    new_type(name_text, text)
    sleep(1)
    new_click(select)


# 取消筛选
def clean_search_cancle():
    new_click(select)
    new_click(select_name)
    new_backspace(select_name)
    new_click(select)


# 删除
def clean_delete():
    new_click(delete)
    sleep(1)
    new_click(yes_button)


# 一组元素，通过index输入:i表示第几个元素，如0,1,2，
def new_types(ele, i, p_value):
    ele = driver.find_elements_by_xpath(ele)[i]
    sleep(1)
    new_double_click_ele(ele)
    ele.send_keys(p_value)