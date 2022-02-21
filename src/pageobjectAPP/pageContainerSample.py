# -*- coding: utf-8 -*- 
# @Time : 2021/1/11 14:20 
# @Author : 张丽雯 
# @File : pageContainerSample.py 
# @中文描述 :  容器取样页面

from ElementApp.ContainerSamplePage import *
from src.public.common.Login import *


# 进入容器取样界面
def login_container_manage():
    new_click(inventory)
    new_click(container)
    new_click(containersample)
    sleep(2)
    print('进入容器取样页面！')


# 容器取样
def container_sample(num, state):
    new_click(second_container)
    new_click(sample)
    new_type(sample_num, num)
    if new_page_source('取样说明'):
        new_type(sample_state, state)
    new_click(submit)
    sleep(3)


# 锁定容器
def container_lock():
    new_click(second_container)
    new_click(lock)
    new_click(yes_button)
    sleep(2)


# 驳回容器
def container_reject():
    new_click(second_container)
    new_click(reject)
    new_click(yes_button)
    sleep(2)
