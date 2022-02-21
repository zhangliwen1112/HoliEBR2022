# -*- coding: utf-8 -*- 
# @Time : 2021/1/11 17:47 
# @Author : 张丽雯 
# @File : pageContainerOver.py 
# @中文描述 :  结束容器界面
from ElementApp.ContainerOverPage import *
from src.public.common.Login import *


# 进入结束容器界面
def login_container_over():
    new_click(inventory)
    new_click(container)
    new_click(containerover)
    sleep(2)
    print('进入结束容器页面！')

# 取消结束
def container_over_cancel():
    new_click(second_container)
    new_click(cancel_over)
    new_click(yes_button)
    sleep(2)

# 删除容器
def container_over_delete():
    new_click(second_container)
    new_click(delete)
    new_click(yes_button)
    sleep(2)

# 归零容器
def container_over_zero():
    new_click(second_container)
    new_click(zero)
    new_click(yes_button)
    sleep(2)

# 重新打印标签
def container_over_label(num):
    new_click(second_container)
    new_click(label)
    sleep(2)
    new_type(print_num, num)
    new_click(submit)
    sleep(2)

# 刷新
def container_over_refresh():
    new_click(refresh)
    sleep(2)


# 结束容器
def container_over():
    new_click(second_container)
    new_click(over)
    new_click(yes_button)
    sleep(2)
