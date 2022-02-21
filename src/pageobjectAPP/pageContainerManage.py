# -*- coding: utf-8 -*- 
# @Time : 2021/1/8 16:41 
# @Author : 张丽雯 
# @File : pageContainerManage.py 
# @中文描述 :  容器管理页面

from ElementApp.ContainerManagePage import *
from src.public.common.Login import *


# 进入容器管理界面
def login_container_manage():
    new_click(inventory)
    new_click(container)
    new_click(containermanage)
    print('进入容器管理页面！')


# 查看容器明细
def container_detail(isopen):
    new_click(first_container)
    new_click(detail)
    new_click(open)
    if isopen in 'Y':
        new_click(open_N)
    new_click(pallet_detail)
    new_click(entity)
    new_click(receive)
    new_click(storage)
    new_click(close)
    new_click(submit)
    sleep(2)


# 移动
def container_move():
    new_click(first_container)
    new_click(move)
    new_click(target_storage)
    sleep(2)
    new_click(submit)
    if new_page_source("物料位置不兼容"):
        new_click(submit1)
    sleep(5)


# 返回
def container_reback():
    new_click(first_container)
    new_click(reback)
    sleep(2)
    new_click(submit)
    sleep(2)


# 拆分
def container_split(type, num):
    new_click(first_container)
    new_click(split)
    if type in '新容器':
        new_click(split_type2)
    else:
        new_click(split_type1)
    new_type(split_num, num)
    new_click(submit)
    sleep(2)


# 重新打印标签
def container_label(num):
    new_click(first_container)
    new_click(label)
    new_type(print_num, num)
    new_click(submit)
    sleep(2)



# 状态
def container_status(text):
    new_click(first_container)
    new_click(status)
    new_click(select_status)
    if text in '驳回':
        new_click(status2)
    if text in '锁定':
        new_click(status1)
    new_click(submit)
