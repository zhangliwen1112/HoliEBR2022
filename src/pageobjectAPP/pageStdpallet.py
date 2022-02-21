# -*- coding: utf-8 -*- 
# @Time : 2021/1/19 15:04 
# @Author : lianxiujuan 
# @File : pageStdpallet.py
# @中文描述 : 标准托盘-page


from ElementApp.StdpalletPage import *
from src.public.FunctionSet import *


# 进入标准托盘界面
def login_stdpallet():
    new_click(inventory)
    new_click(pallet)
    new_click(stdpallet)

# 新增标准托盘
def stdpallet_add(addname, addtare,addweight='100', addheight='100', addlongth='100', addwidth='100', addratio='1'):
    new_click(add)
    ele = new_find_elements(allselect)
    new_click_ele(ele[0])
    new_click(type1)
    ele = new_find_elements(allinput)
    new_type_double_ele(ele[1], addname)
    new_type_double_ele(ele[2], addweight)
    new_type_double_ele(ele[3], addheight)
    new_type_double_ele(ele[4], addlongth)
    new_type_double_ele(ele[5], addwidth)
    new_type_double_ele(ele[6], addratio)
    new_type_double_ele(ele[7], addtare)
    new_click(yes_button)

# 编辑标准托盘
def stdpallet_edit(editname, edittare,editweight='100', editheight='100', editlongth='100', editwidth='100', editratio='1'):
    new_click(first)
    new_click(edit)
    ele = new_find_elements(allinput)
    new_type_double_ele(ele[1], editname)
    new_type_double_ele(ele[2], editweight)
    new_type_double_ele(ele[3], editheight)
    new_type_double_ele(ele[4], editlongth)
    new_type_double_ele(ele[5], editwidth)
    new_type_double_ele(ele[6], editratio)
    new_type_double_ele(ele[7], edittare)
    new_click(yes_button)

# 删除标准托盘
def stdpallet_delete():
    new_click(delete)
    new_click(delete_yes_button)
