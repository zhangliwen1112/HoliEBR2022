# -*- coding: utf-8 -*-

# @Time : 2021/1/13
# @Author : lianxiujuan
# @File : pageusermg.py
# @中文描述 :  用户管理

from ElementAdmin.UsermgPage import *
from src.public.FunctionSet import *


# 进入用户管理界面
def login_usermg():
    new_click(usermg)

# 新增用户
def user_add(addname, addmail, addrfid):
    new_click(add)
    time.sleep(2)
    ele = new_find_elements(username_mail_rfid)
    new_send_keys_ele(ele[1], addname)
    new_send_keys_ele(ele[2], addmail)
    new_send_keys_ele(ele[3], addrfid)
    ele = new_find_elements(people_group)
    new_click_ele(ele[0])
    select = new_find_elements(select_list)
    new_click_ele(select[0])
    # new_click(people_select)
    new_click(role1)
    new_click_ele(ele[1])
    new_click(admingp)
    submit = new_find_elements(submit_button)
    new_click_ele(submit[1])
    # new_click(yes_button)

# 编辑用户
def user_edit(editmail):
    new_click(edit)
    time.sleep(2)
    ele = new_find_elements(username_mail_rfid)
    new_type_ele(ele[1], editmail)
    new_click(role2)
    ele = new_find_elements(people_group)
    new_click_ele(ele[1])
    new_click(usergp)
    # new_click(yes_button)
    submit = new_find_elements(submit_button)
    new_click_ele(submit[1])

# 激活用户
def user_active(newpassd, confirmpassd):
    new_click(active)
    ele = new_find_elements(password)
    new_send_keys_ele(ele[0],newpassd)
    new_send_keys_ele(ele[1],confirmpassd)
    new_click(yes_button)
    # new_send_keys(newpw, newpassd)
    # new_send_keys(confirmpw, confirmpassd)
    # ele = new_find_elements(yes_button)
    # new_click_ele(ele[1])

# 锁定用户
def user_lock():
    new_click(lock)
    new_click(lock_delete_yes_button)

# 解锁用户
def user_unlock():
    new_click(unlock)

# 删除用户
def user_delete():
    new_click(delete)
    new_click(lock_delete_yes_button)

# 刷新用户
def user_refresh():
    new_click(refresh)
