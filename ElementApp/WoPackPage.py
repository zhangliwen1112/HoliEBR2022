# -*- coding: utf-8 -*- 
# @Time : 2021/1/6 13:41 
# @Author : 张丽雯 
# @File : workpacking.py 
# @中文描述 :  工单包装

# 登录页码元素
workorder = "//*[contains(text(),'工单管理')]"
wopack = "//*[contains(text(),'工单包装')]"

# 按钮元素
pack = "//span[contains(.,'包装')]"
transfer = "//span[contains(.,'转移')]"
refresh = "//span[contains(.,'刷新')]"

# -------------------包装界面元素-----------------
# 选中第一条
first = "//div[@role='row' and @row-index='0']"
consumed = "//span[contains(.,'耗用')]"
returned = "//button//span[contains(.,'退回')]"
changed = "//span[contains(.,'调整')]"
closed = "//span[contains(.,'关闭')]"
# 耗用界面
ContainerID = "//div[@class='row row--dense']//input[@readonly='readonly']"
ID1 = "//tr/td[1]/div/div"
ID_submit = "//button[@class='mr-4 my-1 v-btn v-btn--contained theme--light v-size--default primary']"
consumed_number = "//form/div/div[7]/div[2]/div/div/div[1]/div[1]/input"
# 是否结束容器
FinishedContainer_no = "//label[@class='v-label theme--light'][contains(.,'否')]"
FinishedContainer_yes = "//label[@class='v-label theme--light'][contains(.,'是')]"
add = "//span[contains(.,'新增')]"
delete = "//span[contains(.,'删除')]"
# 弹框确定、取消按钮
yes_button = "//div[@class='DialogActions']//span[contains(.,'确定')]"
cancle_button = "//div[@class='DialogActions']//span[contains(.,'取消')]"

# ---------------------退出耗用页面--------------------
cancel = "//div[@class='v-dialog v-dialog--active v-dialog--persistent v-dialog--scrollable']//span[contains(.,'取消')]"
submit = "//div[@class='v-dialog v-dialog--active v-dialog--persistent v-dialog--scrollable']//span[contains(.,'确定')]"

# ---------------------退回页面元素--------------------
# 选择第一行容器
select_container1 = '//form/div/div[9]/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div'
returned_num = "//form/div/div[7]/div[2]/div/div/div[1]/div[1]/input"
submit1 = "//span[contains(.,'确定')]"

# -----------------------筛选-------------------------
select = "//span[contains(.,'筛选')]"
code = "//span[@ref='eTitle' and contains(.,'编码')]"
code_text = "//div[2]/div[2]/div[1]/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/input"

# -----------------------转移-------------------------
select_work = "//form/div/div[7]/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div"
up = "//div[@class='row justify-space-around row--dense']//button[@class='v-btn v-btn--contained theme--light v-size--default']"