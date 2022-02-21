# -*- coding: utf-8 -*- 
# @Time : 2021/1/22 14:59 
# @Author : 张丽雯 
# @File : Sign.py 
# @中文描述 :  签名--双签名&单签名

from src.public.FunctionSet import *
from src.public.common.elements import *

# 签名弹框 -- 双签名
def sign_double(name1, password1, name2,password2):
    new_type(user, name1)
    new_type(pwd, password1)
    new_click(sign_yes)
    sleep(2)
    new_type(user, name2)
    new_type(pwd, password2)
    new_click(sign_yes)
    sleep(2)

# 签名弹框 -- 单签名
def sign_single(name1, password1):
    new_type(user, name1)
    new_type(pwd, password1)
    new_click(sign_yes)
    sleep(2)
