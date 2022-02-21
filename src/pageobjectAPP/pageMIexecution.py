# -*- coding: utf-8 -*- 
# @Time : 2021/1/12 10:51 
# @Author : 张丽雯 
# @File : pageMIexecution.py 
# @中文描述 :  MI执行-gongxuMI执行

from ElementApp.MIexecutionPage import *
from src.public.common.Login import *


# 进入MI执行界面
def login_MI_execution():
    new_click(manufacture)
    new_click(MIexecution)
    sleep(2)
    print('进入MI执行页面！')


# 选择工单-执行MI
def MI_execution_wo():
    new_click(wo)
    new_click(wo1)
    new_click(woyes)
    sleep(2)

# 点击开始按钮
def MI_execution_start():
    new_click(start)


# 上传文件
def MI_execution_upfile(file):
    base_dir = os.getcwd()
    base = base_dir.split("\\HoliEBR-UI")[0]
    upload_path = base + "\\HoliEBR-UI\\src\\public\\upload\\"

    new_find_element(upload).send_keys(upload_path + file)


# 执行next下一步按钮,其中i=0,1,2....
def MI_execution_next(i):
    driver.find_elements_by_xpath(next1)[i].click()
    sleep(1)


# text组件，输入文本内容
def MI_execution_text(words):
    new_type(text, words)


# text组件，输入文本内容
def MI_execution_multitext(words):
    new_type(multi, words)


# text组件，输入文本内容
def MI_execution_number(number):
    new_type(num, number)


# 多选框组件
def MI_execution_multiselect(i):
    driver.find_elements_by_xpath(multiselect)[i].click()


# 签名 -- 签名按钮
def MI_execution_sign_button():
    new_click(sign)


# 强制执行组件，输入文本内容
def MI_execution_force(text):
    new_type(force, text)
    sleep(1)

# 警示组件
def MI_execution_alert(type,level,text):
    new_click(alert_type)
    if type in '偏差':
        new_click(errors)
    elif type in '备注':
        new_click(notes)
    else:
        pass
    new_click(alert_level)
    if level in '微小':
        new_click(small)
    elif level in '严重':
        new_click(serious)
    elif level in '重要':
        new_click(major)
    else:
        new_click(none)
    new_type(alert_text, text)
    sleep(2)

# 快速称量
def MI_execution_scale():
    new_click(scale)
    sleep(2)
    new_click(scale_yes)
    sleep(1)