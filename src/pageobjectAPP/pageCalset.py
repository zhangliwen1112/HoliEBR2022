# -*- coding: utf-8 -*-

# @Time : 2021/1/13
# @Author : lianxiujuan
# @File : pageCalset.py
# @中文描述 : 校准设置

from ElementApp.Calset import *
from src.public.FunctionSet import *


# 进入校准设置界面
def login_cal():
    new_click(weigh)
    new_click(cal)

# 天平校准
def weigh_cal(weightype, expiresdata, wtimesdata, stepdata):
    global i, j
    if weightype == '天平':
        i, j = 0, 0
        new_click(balance)
    elif weightype == '地磅':
        i, j = 1, 3
        new_click(weighbridge)
    ele = new_find_elements(typeselect)
    new_click_ele(ele[i])
    time.sleep(1)
    ele = new_find_elements(typecontent)
    new_click_ele(ele[i])
    time.sleep(1)
    ele = new_find_elements(expires)
    new_type_double_ele(ele[j], expiresdata)
    ele = new_find_elements(weightimes)
    new_type_double_ele(ele[j], wtimesdata)
    ele = new_find_elements(step)
    new_type_double_ele(ele[j], stepdata)
    ele = new_find_elements(save)
    new_click_ele(ele[i])


# 删除校准
def delete_cal(weightype):
    global i
    if weightype == '天平':
        i = 0
    elif weightype == '地磅':
        i = 1
    new_click(delete)
    time.sleep(2)
    new_click(yes_button)
    time.sleep(2)
    ele = new_find_elements(save)
    new_click_ele(ele[i])

# 删除校准类型
def delete_caltype(weightype):
    global i
    if weightype == '天平':
        i = 0
    elif weightype == '地磅':
        i = 1
    new_click(delete)
    time.sleep(2)
    new_click(yes_button)
    time.sleep(2)