# -*- coding: utf-8 -*-

# @Time : 2021/1/13
# @Author : lianxiujuan
# @File : pageCodeconfig.py
# @中文描述 :  编码配置

from ElementAdmin.CodeconfigPage import *
from src.public.FunctionSet import *


# 进入编码配置界面
def login_codeconfig():
    new_click(syset)
    new_click(codeconfig)

# 新增编码配置
def codeconfig_add(addcode, addname, adddesc, addcircleway):
    new_click(add)
    new_send_keys(code, addcode)
    new_send_keys(name, addname)
    new_send_keys(desc, adddesc)
    new_click(insertitem)
    new_click(insert)
    new_click(circleway)
    if addcircleway == "年":
        new_click(circlevalue1)
    elif addcircleway == "月":
        new_click(circlevalue2)
    elif addcircleway == "日":
        new_click(circlevalue3)
    elif addcircleway == "最大值":
        new_click(circlevalue4)
    ele = new_find_elements(yes_button)
    new_click_ele(ele[1])

# 编辑编码配置
def codeconfig_edit(editname, editdesc, editcircleway):
    new_click(edit)
    new_type(name, editname)
    new_type(desc, editdesc)
    new_click(circleway)
    if editcircleway == "年":
        new_click(circlevalue1)
    elif editcircleway == "月":
        new_click(circlevalue2)
    elif editcircleway == "日":
        new_click(circlevalue3)
    elif editcircleway == "最大值":
        new_click(circlevalue4)
    ele = new_find_elements(yes_button)
    new_click_ele(ele[1])

# 删除编码配置
def codeconfig_delete():
    new_click(delete)
    new_click(delete_yes_button)

# 重置编码配置
def codeconfig_reset():
    new_click(reset)
    new_click(reset_yes_button)