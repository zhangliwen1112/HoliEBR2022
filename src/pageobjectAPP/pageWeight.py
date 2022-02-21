# -*- coding: utf-8 -*- 
# @Time : 2020/10/14 10:05 
# @Author : 张丽雯 
# @File : pageweight.py
# @中文描述 :  砝码配置

from ElementApp.WeightPage import *
from src.public.common.Login import *
from src.public.common.elements import *
#进入砝码配置界面

def login_weight():
    new_click(weightmanage)
    new_click(weight)
    print('进入砝码配置页面')

#新增砝码

def weight_add(weightname,value,unit):
    new_click(add)
    new_type(name, weightname)
    sleep(1)
    new_type(weight_value, value)
    new_click(weight_unit)
    if unit == 'mg':
        new_click(unit_mg)
    elif unit == 'g':
        new_click(unit_g)
    elif unit == 'lb':
        new_click(unit_lb)
    else:
        new_click(unit_kg)
    new_click(submit)

    # 异常判断
    if is_element_present(error_message):
        new_get_text(error_message)
        new_click(cancel)
    if is_element_present(error_message2):
        new_get_text(error_message2)
        new_click(cancel)


#编辑砝码
def weight_edit(value,unit):
    new_click(edit)
    new_type_double(weight_value,value)
    new_click(weight_unit)
    if unit == 'mg':
        new_click(unit_mg)
    elif unit == 'g':
        new_click(unit_g)
    elif unit == 'lb':
        new_click(unit_lb)
    else:
        new_click(unit_kg)
    new_click(submit)
    # 异常判断
    if is_element_present(error_message):
        new_get_text(error_message)
        new_click(cancel)
    if is_element_present(error_message2):
        new_get_text(error_message2)
        new_click(cancel)

#删除砝码
def weight_delete():
    new_click(delete)
    sleep(1)
    new_click(yes_button)
