# -*- coding: utf-8 -*- 
# @Time : 2021/1/11 13:39 
# @Author : 张丽雯 
# @File : ContainerSamplePage.py
# @中文描述 :  容器取样

# 登录页码元素
inventory = "//*[contains(text(),'库存管理')]"
container = "//*[contains(text(),'容器')]"
containersample = "//*[contains(text(),'容器取样')]"

# 标准容器上端按钮
sample = "//span[contains(.,'取样')]"
lock = "//span[contains(.,'锁定')]"
reject = "//span[contains(.,'驳回')]"
refresh = "//span[contains(.,'刷新')]"
# 第er个容器
first_container = "//div/div[24]/div[1]/div/div/div/div/input"
second_container = "//div[3]/div[2]/div/div/div[1]/div[1]/div/div/div/div/input"
# -------------------------------取样界面元素--------------------------------
sample_num = "//form/div/div/div[2]/div/div/div[1]/div/input"
# sample_num = "//label[text()='每个容器的取样量']"
sample_state = "//textarea"
submit = "//span[text()='确定']"
cancel = "//span[text()='取消']"


# ----------------------弹框确定、取消按钮元素-----------------------------------
yes_button = "//div[@class='DialogActions']//span[contains(.,'确定')]"
cancle_button = "//div[@class='DialogActions']//span[contains(.,'取消')]"

