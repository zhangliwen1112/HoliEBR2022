# -*- coding: utf-8 -*- 
# @Time : 2021/1/20 16:45 
# @Author : 张丽雯 
# @File : Close_current_tab.py 
# @中文描述 :  关闭当前打开的页面

from src.public.common.elements import *
from src.public.common.Login import *

# 关闭当前打开的页面
def Close_current_tab():
    new_click1(close_tab)
    sleep(2)
