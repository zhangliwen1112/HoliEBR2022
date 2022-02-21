# -*- coding: utf-8 -*- 
# @Time : 2021/1/4 13:39 
# @Author : 张丽雯 
# @File : pageDeclaration.py 
# @中文描述 :  生产声明

from ElementApp.WoDeclarationPage import *
from src.pageobjectAPP.pagelogin import *


# 进入生产声明界面
def login_Declaration():
    new_click(workorder)
    new_click(Declaration)
    print('进入生产声明页面')


# 生产声明
def declaration(num,Cnumber):
    new_click(declaration_button)
    new_type(declara_num, num)
    new_click(palletType)
    new_click(palletType1)
    new_type(containerNumber, Cnumber)
    new_click(pallettitle)
    new_click(containertitle)
    new_click(labletitle)
    new_click(kuqu)
    new_click(kuqu1)
    sleep(1)
    new_click(kuqu_submit)
    new_click(kuwei)
    new_click(kuwei1)
    sleep(1)
    new_click(kuwei_submit)
    sleep(1)
    new_click(submit)
    sleep(1)
    if new_page_source('累计声明数量多于工单发布量,是否继续执行'):
        new_click(yes_button)
    sleep(5)
