# -*- coding: utf-8 -*- 
# @Time : 2021/1/18 17:01 
# @Author : 张丽雯 
# @File : Search_Item.py
# @中文描述 :  筛选--按查询条件筛选

from src.public.common.elements import *
from src.public.FunctionSet import *


# 查询条件search_item，搜索内容为text,若清除筛选条件，text为' '
def search_item(search_item, text):
    new_click(search)
    new_click(searchitem(search_item))
    new_type_double(search_text, text)
    new_click(searchitem(search_item))
    new_click(search)


# 查询条件search_option，搜索内容为选项,若清除筛选条件，text为'---请选择---'
def search_option(search_item, text):
    new_click(search)
    new_click(searchitem(search_item))
    new_click(search_select)
    new_click(searchoption(text))
    new_click(searchitem(search_item))
    new_click(search)
