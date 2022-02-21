# -*- coding: utf-8 -*- 
# @Time : 2021/1/6 14:50 
# @Author : 张丽雯 
# @File : pagewopack.py 
# @中文描述 :  工单包装

from ElementApp.WoPackPage import *
from src.public.FunctionSet import *
from src.public.common.elements import *

# 进入工单包装界面
def login_wopack():
    new_click(workorder)
    new_click(wopack)
    print('工单包装界面进入成功！')


# 包装界面-耗用容器
def wopack_consumed(num, isFinishedContainer='是'):
    new_click(pack)
    new_click(consumed)
    new_click(ContainerID)
    new_click(ID1)
    new_click(ID_submit)
    new_type_double(consumed_number, num)

    if isFinishedContainer in '否':
        new_click(FinishedContainer_no)
        new_click(add)
    else:
        new_click(FinishedContainer_yes)
        new_click(add)
        sleep(2)

        # 异常判断
    if new_page_source('请输入精度为3位的非0小数') or new_page_source('请输入小于'):
        sleep(2)
        new_get_text(error_message)
        new_click(cancel)
        new_click(closed)
        return


    # 容器已结束
    if new_page_source('该容器已结束,是否继续？'):
        new_click(yes_button)
        sleep(2)
    if new_page_source('已使用过该容器,是否继续？'):
        new_click(yes_button)
        sleep(1)
    if new_page_source('容器已超过批次限制使用期，你确定要使用吗？'):
        new_click(yes_button)
        sleep(1)
    new_click(submit)
    new_click(closed)


# 包装界面-退回
def wopack_returned(num):
    new_click(pack)
    new_click(returned)
    new_click(select_container1)
    new_type(returned_num, num)
    sleep(1)
    new_click(select_container1)
    new_click(submit1)
       # 异常判断
    if new_page_source('请输入精度为3位的非0小数') or new_page_source('请输入小于'):
        sleep(2)
        new_get_text(error_message2)
        new_click(returned_close)
        new_click(closed)
        return
    if new_page_source('确认继续执行该操作？'):
        new_click(yes_button)
    sleep(2)
    new_click(closed)
    sleep(2)


# 包装界面-调整（工单已生产终止，才可调整）
def wopack_changed(num, isFinishedContainer):
    new_click(pack)
    sleep(2)
    new_click(changed)
    new_click(ContainerID)
    new_click(ID1)
    new_click(ID_submit)
    new_type_double(consumed_number, num)
    if isFinishedContainer in '否':
        new_click(FinishedContainer_no)
        new_click(add)
    else:
        new_click(FinishedContainer_yes)
        new_click(add)
    # 容器已结束
    new_click(yes_button)
    new_click(submit)
    new_click(closed)


# 转移
def woparking_transfer():
    new_click(transfer)
    new_click(select_work)
    new_click(up)
    new_click(submit1)