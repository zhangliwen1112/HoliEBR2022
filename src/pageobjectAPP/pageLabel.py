# -*- coding: utf-8 -*- 
# @Time : 2021/1/19 15:04 
# @Author : lianxiujuan 
# @File : pagelabel.py
# @中文描述 : 标签管理-page


from ElementApp.LabelmgPage import *
from src.public.FunctionSet import *


# 进入标签界面
def login_label():
    new_click(labelmg)

# 新增标签
def label_add(addcode, addname, adddesc, addzpl):
    new_click(add)
    ele = new_find_elements(allinput)
    new_send_keys_ele(ele[0], addcode)
    new_send_keys_ele(ele[1], addname)
    new_send_keys_ele(ele[2], adddesc)
    new_send_keys(zpl, addzpl)
    sleep(1)
    new_click(yes_button)
    sleep(1)

# 编辑标签
def label_edit(editname, editdesc, editzpl):
    new_click(edit)
    ele = new_find_elements(allinput)
    new_send_keys_ele(ele[1], editname)
    new_send_keys_ele(ele[2], editdesc)
    new_send_keys(zpl, editzpl)
    new_click(yes_button)

# 设置默认模板
def label_setdefault():
    new_click(setdefault)

# 删除标签
def label_delete():
    new_click(delete)
    new_click(delete_yes_button)
