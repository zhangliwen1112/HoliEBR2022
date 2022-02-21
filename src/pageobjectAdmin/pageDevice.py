# -*- coding: utf-8 -*- 
# @Time : 2021/1/19 14:35 
# @Author : 张丽雯 
# @File : pageDevice.py 
# @中文描述 :  工作中心-外部设备页面

from src.public.common.Login import *
from ElementAdmin.devicePage import *


# 进入外部设备页面
def login_device_manage():
    sleep(2)
    new_click(Work_Centre)
    new_click(Device_Page)
    print('进入外部设备页面！')


# 新增设备
def device_manage_add(device_code,device_name,device_type,device_status,device_address,device_des=''):
    new_click(add)
    new_type(code,device_code)
    sleep(1)
    new_type(name,device_name)
    sleep(1)
    new_click(type)
    if device_type == '打印机':
        new_click(type1)
    elif device_type == '电子秤':
        new_click(type2)
    else:
        new_click(type3)
    new_click(status)
    if device_status == '注册':
        new_click(status1)
    elif device_status == '注销':
        new_click(status2)
    elif device_status == '离线':
        new_click(status4)
    else:
        new_click(status3)
    new_type(adr,device_address)
    new_click(worker)
    new_click(worker_all)
    new_click(worker_submit)
    new_type(des,device_des)
    new_click(submit)
    sleep(1)

# 编辑设备
def device_manage_edit(*args):
    new_click(First)
    sleep(1)
    new_click(edit)
    new_type(name,args[0])
    sleep(2)
    new_click(type)
    if args[1] == '打印机':
        new_click(type1)
    elif args[1] == '电子秤':
        new_click(type2)
        sleep(1)
    else:
        new_click(type3)
    new_click(status)
    if args[2] == '注册':
        new_click(status1)
    elif args[2] == '注销':
        new_click(status2)
    elif args[2] == '离线':
        new_click(status4)
    else:
        new_click(status3)
    new_type(adr, args[3])
    new_click(submit)
    sleep(1)

# 删除新增设备
def device_manage_delete():
    new_click(First)
    new_click(delete)
    new_click(delete_submit)
    sleep(1)

