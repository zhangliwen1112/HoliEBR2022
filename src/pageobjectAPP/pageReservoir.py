# -*- coding: utf-8 -*- 
# @Time : 2021/1/29 16:53 
# @Author : 张丽雯 
# @File : pageReservoir.py
# @中文描述 : 库区管理
from ElementApp.KuquPage import *
from src.public.common.Login import *
from src.public.common.elements import *


# 进入库区配置界面
def login_reservoir():
    new_click(inventory)
    new_click(reservoir)
    print('进入库区管理页面')


# 新增库区
def kuqu_add(kuqu_code, kuqu_name):
    new_click(add)
    new_type(code, kuqu_code)
    new_type(name, kuqu_name)
    new_click(changqu)
    new_click(select_changqu1)
    new_click(select_submit)
    new_click(quyu)
    new_click(select_quyu1)
    new_click(location)
    new_click(add_location1)
    new_click(submit)
    # 异常判断
    if is_element_present(error_message):
        new_get_text(error_message)
        new_click(cancle)
    if is_element_present(error_message2):
        new_get_text(error_message2)
        new_click(cancle)


# 编辑库区
def kuqu_edit(kuqu_editname):
    new_click(edit)
    new_type_double(name, kuqu_editname)
    new_click(location)
    new_click(edit_location2)
    new_click(submit)
    # 异常判断
    if is_element_present(error_message):
        new_get_text(error_message)
        new_click(cancle)
    if is_element_present(error_message2):
        new_get_text(error_message2)
        new_click(cancle)


# 删除
def kuqu_delete():
    new_click(delete)
    sleep(2)
    new_click(yes_button)


# 关联库位
def kuqu_relation_kuwei():
    new_click(relation)
    sleep(2)
    new_click(relation_kuwei)
    new_click(relation_button)
    new_click(submit)


# 去关联库位
def kuqu_remove_kuwei():
    new_click(relation)
    sleep(2)
    new_click(remove_first)
    new_click(remove_button)
    new_click(submit)
