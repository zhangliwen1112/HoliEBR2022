# -*- coding: utf-8 -*- 
# @Time : 2021/1/13 16:23
# @Author : lianxiujuan 
# @File : pageSignpathapply.py 
# @中文描述 : 签名路径应用



from ElementAdmin.SignpathapplyPage import *
from src.public.common.Search_Item import *
from src.public.common.Select_Item import *


# 进入签名路径应用界面
def login_signpathapply():
    new_click(mimg)
    new_click(signpathapply)

# 配置签名路径
def signpathapply_config(micode, signpath):
    new_click(config)
    ele1 = new_find_elements(config_select)
    new_click_ele(ele1[0])
    # 搜索MI
    ele = new_find_elements(search)
    new_click_ele(ele[1])
    ele = new_find_elements(searchitem("MI编码"))
    new_click_ele(ele[1])
    new_type_double(search_text, micode)
    time.sleep(2)
    new_click(miresult_select)
    ele = new_find_elements(yes_button)
    new_click_ele(ele[1])
    # 选择应用类型、签名路径
    configitem = ['MI审批', '备注验证', '偏差验证', 'MI复核验证']
    for i in configitem:
        new_click(selectbutton)
        new_click(xpath_litype(i))
        ele3 = new_find_elements(config_select)
        new_click_ele(ele3[1])
        new_click(select_code)
        sleep(1)
        new_type(input_select,signpath)
        sleep(2)
        new_click(select)
        sleep(1)
        ele = new_find_elements(yes_button)
        new_click_ele(ele[1])
        # ele = new_find_elements(selectbutton)
        # new_click_ele(ele[1])
        # new_click(xpath_litype(signpath))
        # ele = new_find_elements(yes_button)
        # new_click_ele(ele[2])
    sleep(1)
    ele = new_find_elements(yes_button)
    new_click_ele(ele[0])

# 删除签名路径
def signpathapply_delete():
    new_click(first_row)
    new_click(delete)
    new_click(submit)
