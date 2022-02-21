# -*- coding: utf-8 -*- 
# @Time : 2021/1/11 17:40 
# @Author : 张丽雯 
# @File : ContainerOverPage.py 
# @中文描述 :  结束容器界面

# 登录页码元素
inventory = "//*[contains(text(),'库存管理')]"
container = "//*[contains(text(),'容器')]"
containerover = "//*[contains(text(),'结束容器')]"

# 标准容器上端按钮
over = "//span[contains(.,'结束')]"
cancel_over = "//span[contains(.,'取消结束')]"
delete = "//span[contains(.,'删除')]"
zero = "//span[contains(.,'归零')]"
label = "//span[contains(.,'标签重打')]"
refresh = "//span[contains(.,'刷新')]"
#选择第二个
second_container = "//div[3]/div[2]/div/div/div[1]/div[1]/div/div/div/div/input"
# ----------------------弹框确定、取消按钮元素-----------------------------------
yes_button = "//div[@class='DialogActions']//span[contains(.,'确定')]"
cancle_button = "//div[@class='DialogActions']//span[contains(.,'取消')]"

# ------------------------------------标签打印页面元素---------------------------
print_num = '//div/div[2]/div[2]/div/div/div[2]/form/div/div/div[3]/div/div/div[1]/div/input'
submit = "//button[contains(.,'确定')]"
cancel = "//button[contains(.,'取消')]"


