# -*- coding: utf-8 -*-

# @Time : 2021/1/13
# @Author : lianxiujuan
# @File : pageSignpath.py
# @中文描述 :  签名路径

from ElementAdmin.SignpathPage import *
from src.public.FunctionSet import *


# 进入签名路径界面
def login_signpath():
    new_click(sysset)
    new_click(signpath)

# 新增签名路径
def signpath_add(addcode, addname, addlevel):
    new_click(add)
    ele = new_find_elements(code_name_level)
    new_send_keys_ele(ele[1], addcode)
    new_send_keys_ele(ele[2], addname)
    new_click(addsignlevel)
    ele = new_find_elements(code_name_level)
    new_send_keys_ele(ele[3], addlevel)
    new_click(group)
    new_click(admingp)
    ele = new_find_elements(yes_button)
    new_click_ele(ele[2])
    ele = new_find_elements(yes_button)
    new_click_ele(ele[1])

# 新增签名路径，签名级别异常
def signpath_add_abnormal(addcode, addname, addlevel):
    new_click(add)
    ele = new_find_elements(code_name_level)
    new_send_keys_ele(ele[1], addcode)
    new_send_keys_ele(ele[2], addname)
    new_click(addsignlevel)
    ele = new_find_elements(code_name_level)
    new_send_keys_ele(ele[3], addlevel)
    new_click(group)
    new_click(admingp)
    ele = new_find_elements(yes_button)


# 编辑签名路径
def signpath_edit(editname):
    new_click(edit)
    ele = new_find_elements(code_name_level)
    new_type_ele(ele[1], editname)
    ele = new_find_elements(yes_button)
    new_click_ele(ele[1])

# 验证签名路径
def signpath_verify():
    new_click(verify)

# 取消验证签名路径
def signpath_cancelverify():
    new_click(cancelverify)

# 删除签名路径
def signpath_delete():
    new_click(delete)
    new_click(yes_button)
