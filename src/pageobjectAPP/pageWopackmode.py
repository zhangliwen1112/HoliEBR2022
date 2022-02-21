# -*- coding: utf-8 -*- 
# @Time : 2021/1/7 17:19 
# @Author : 张丽雯 
# @File : pagewopackmode.py
# @中文描述 :  产品包装方式
from ElementApp.WopackModePage import *
from src.public.common.Login import *


# 进入工单包装界面
def login_wopack_mode():
    new_click(workorder)
    new_click(workpackmode)
    print('产品包装方式界面进入成功！')


# 新增产品包装
def add_wopack_mode(packname, isdefault, Ptare, unit, Ctare, num):
    new_click(add)
    new_click(mater)
    new_click(mater_1)
    new_click(mater_submit)
    new_click(station)
    new_click(station_1)
    new_click(station_submit)
    new_type(pack, packname)
    if isdefault in '是':
        new_click(default)
    else:
        pass
    new_click(pallet)
    new_click(pallet_P2)
    new_type_double(pallet_tare, Ptare)
    new_click(pallet_unit)
    if unit in '千克':
        new_click(unit_kg)
    else:
        new_click(unit_g)
    new_click(container)
    new_click(container_C1)
    new_type_double(container_tare, Ctare)
    # new_click(container_unit)
    # if unit in '千克':
    #     new_click(unit_kg)
    # else:
    #     new_click(unit_g)
    new_type(container_num, num)
    new_click(submit)
    sleep(2)
    if new_page_source('该产品已有默认包装方式'):
        new_click(yes_button)
    sleep(1)

# 编辑产品包装方式
def edit_wopack_mode(Ptare, Ctare, num):
    new_click(edit)
    sleep(2)
    new_click(default)
    new_click(pallet)
    new_click(pallet_P1)
    new_type_double(pallet_tare,Ptare)
    new_click(container)
    new_click(container_C2)
    new_type_double(container_tare, Ctare)
    new_type_double(container_num, num)
    new_click(submit)
    new_click(refresh)
    sleep(2)

# 删除产品包装方式
def delete_wopack_mode():
    new_click(delete)
    new_click(yes_button)
    new_click(refresh)

# 按包装说明筛选
def search_wopack_mode(text):
    new_click(search)
    new_click(packinfo)
    new_type(packinfo_text,text)
    sleep(2)
    new_click(search)

# 清除筛选结果
def clear_search_wopack_mode(text):
    new_click(search)
    new_type_double(packinfo_text,text)