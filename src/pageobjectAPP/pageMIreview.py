# -*- coding: utf-8 -*- 
# @Time : 2021/1/22 14:24 
# @Author : 张丽雯 
# @File : pageMIreview.py 
# @中文描述 :  批记录复核

from ElementApp.MIreviewPage import *
from src.public.common.Login import *


# 进入批记录复核页面
def login_MI_review():
    new_click(manufacture)
    new_click(MIreview)
    sleep(2)
    print('进入批记录复核页面！')

# 进入打开页面
def MI_review_open():
    new_click(open)


# 批准
def MI_review_approve():
    new_click(approve)

# 驳回
def MI_review_reject():
    new_click(reject)

# 重新复核
def MI_review_re_review():
    new_click(re_review)

# 复核说明弹框
def MI_review_detail(text):
    new_type(detail,text)
    new_click(re_submit)

# 添加说明
def MI_review_add_detail():
    new_click(add_detail_button)

# 关闭工单
def MI_review_close_wo():
    new_click(close_wo)