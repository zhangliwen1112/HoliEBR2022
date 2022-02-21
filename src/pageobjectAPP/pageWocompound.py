# -*- coding: utf-8 -*- 
# @Time : 2021/1/4 15:45 
# @Author : 张丽雯 
# @File : pagecompounding.py 
# @中文描述 :  工单集中

from ElementApp.WoCompoundPage import *
from src.pageobjectAPP.pagelogin import *


# 进入工单集中界面
def login_Compounding():
    new_click(workorder)
    new_click(compounding)
    print('进入工单集中页面')


# 集中
def Concentrate(ID):
    new_click(concentrate)
    new_type(kucunID, ID)
    new_click(concentrate_submit)
    sleep(3)
    new_click(close)


# 强制集中
def Concentrate_Force():
    new_click(concentrate)
    new_click(reconcent)
    new_click(yes_button)
    sleep(3)
    new_click(close)


# 开启集中
def Concentrate_Open():
    new_click(concentrate)
    new_click(openconcent)
    new_click(yes_button)
    sleep(3)
    new_click(close)


# 混合
def Compounding(ID):
    new_click(compound)
    new_type(kuID, ID)
    new_click(overcontainer)
    new_click(compound_submit)
    sleep(3)
    new_click(close)


# 强行混合
def Compounding_Force():
    new_click(compound)
    new_click(recompound)
    new_click(yes_button)
    sleep(3)
    new_click(close)


# 开启混合
def Compounding_open():
    new_click(compound)
    new_click(opencompound)
    new_click(yes_button)
    new_click(3)
    new_click(close)
