# -*- coding: utf-8 -*-

# @Time : 2021/1/13
# @Author : lianxiujuan
# @File : pageworkstation.py
# @中文描述 :  工作站

from ElementAdmin.WorkstationPage import *
from src.public.FunctionSet import *


# 进入工作站界面
def login_workstation():
    new_click(workcenter)
    new_click(worksta)

# 新增工作站
def workstation_add(addname, addcode):
    new_click(add)
    new_send_keys(name, addname)
    new_send_keys(code, addcode)
    new_click(extdevice)
    new_click(extdevice_all)
    # ele = new_find_elements(yes_button)
    # new_click_ele(ele[1])
    new_click(yes_button)

    new_click(submit)

# 编辑工作站
def workstation_edit(editname):
    new_click(edit)
    new_type(name, editname)
    new_click(submit)

# 删除工作站
def workstation_delete():
    new_click(delete)
    new_click(delete_yes_button)
