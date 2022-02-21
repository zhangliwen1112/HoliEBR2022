# -*- coding: utf-8 -*- 
# @Time : 2020/11/16 15:01 
# @Author : 张丽雯 
# @File : pagestandardcontainer.py 
# @中文描述 :  标准容器界面

from ElementApp.StdContainerPage import *
from src.public.FunctionSet import *
from src.public.common.Login import *


# 进入标准容器界面
def login_standard_container():
    new_click(inventory)
    new_click(container)
    new_click(standardcontainer)
    print('进入标准容器页面')


# 新增标准容器
def add_standard_container(containername, tarevalue,q='100',h='100',l='100',w='100',r='1', unit='kg'):
    new_click(add)
    new_click(type)
    new_click(type1)
    new_type(name, containername)
    new_type_double(quality,q)
    new_type_double(hight,h)
    new_type_double(length,l)
    new_type_double(width,w)
    new_type_double(ratio,r)
    new_type(tare, tarevalue)
    new_click(slectunit)
    if unit in "g":
        new_click(unit1)
    else:
        new_click(unit2)
    new_click(submit)

# 删除
def delete_standard_container():
    new_click(first)
    new_click(delete)
    new_click(yes_button)


# 编辑
def edit_standard_container(containername,q,h,l,w,r, tarevalue, unit):
    new_click(first)
    new_click(edit)
    sleep(1)
    new_type_double(name, containername)
    new_type_double(quality, q)
    new_type_double(hight, h)
    new_type_double(length, l)
    new_type_double(width, w)
    new_type_double(ratio, r)
    new_type_double(tare, tarevalue)
    new_click(slectunit)
    if unit in "g":
        new_click(unit1)
    else:
        new_click(unit2)
    new_click(submit)

