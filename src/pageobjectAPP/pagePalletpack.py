# -*- coding: utf-8 -*- 
# @Time : 2020/11/16 17:45 
# @Author : 张丽雯 
# @File : pagepalletpack.py 
# @中文描述 :  托盘包装方式

from ElementApp.PalletPackPaga import *
from src.public.common.Login import *


# 进入托盘包装方式界面
def login_pallet_pack():
    new_click(inventory)
    new_click(pallet)
    new_click(palletpack)
    print('进入托盘包装页面')

# 新增托盘包装方式
def add_pallet_pack(volume,*args):
    new_click(add)
    new_click(material)
    if args[0] != '':
        new_type(material_select, args[0])
        sleep(1)
    new_click(material1)
    new_click(material_submit)
    new_click(supplier)
    new_click(supplier1)
    new_click(supplier_submit)
    new_click(material_title)
    new_type_double()
    new_type(container, volume)
    new_click(submit)

# 删除
def delete_pallet_pack():
    # new_click(first)
    new_click(delete)
    new_click(yes_button)

#编辑
def edit_pallet_pack(vol):
    # new_click(first)
    new_click(edit)
    new_click(material_title)
    new_backspace(container)
    new_backspace(container)
    new_backspace(container)
    new_backspace(container)
    new_type(container, vol)
    new_click(submit)