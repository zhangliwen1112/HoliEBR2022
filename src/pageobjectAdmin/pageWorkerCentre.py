# -*- coding: utf-8 -*- 
# @Time : 2021/1/20 11:26 
# @Author : 张丽雯 
# @File : pageWorkerCentre.py 
# @中文描述 :  工作中心-工作中心

from src.public.common.Login import *
from ElementAdmin.workercentrePage import *


# 进入工作中心-工作中心页面
def login_worker_centre():
    new_click(Work_Centre)
    new_click(Worker_Centre)
    print('进入工作中心页面！')

# 新增工作中心
def worker_center_add(worker_code,worker_name):
    new_click(add)
    new_type(code, worker_code)
    sleep(1)
    new_type(name, worker_name)
    sleep(1)
    new_click(factory)
    new_click(factory1)
    # new_click(factory_submit)
    new_click(area)
    new_click(area1)
    new_click(location)
    new_click(location1)
    new_click(submit)

# 编辑新增工作中心
def worker_center_edit(*args):
    new_click(First)
    new_click(edit)
    new_type(name,args[0])
    if args[1] != '':
        new_click(factory)
        new_click(factory1)
        new_click(area)
        new_click(area1)
        new_click(location)
        new_click(location1)
    else:
        pass
    new_click(submit)

# 删除工作中心
def worker_center_delete():
    new_click(First)
    new_click(delete)
    new_click(delete_submit)