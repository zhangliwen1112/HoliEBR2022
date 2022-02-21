# -*- coding: utf-8 -*- 
# @Time : 2021/2/1 11:29 
# @Author : 张丽雯 
# @File : CancelWeightPage.py
# @中文描述 :  取消称量 -- 退料

# 登陆元素
inventory = "//*[contains(text(),'库存管理')]"
cancelweight = "//*[contains(text(),'取消称量')]"
returned_mater = "//*[contains(text(),'退料')]"
cancel_weight = "//a/div[text()='取消称量']"
# -----------------------------------退料、取消称量公共元素------------------------------------
# 执行按钮
execute = "//span[text()='执行']"
# 称量标签
weight_label = "//div[@class='col col-8']//input[@type='text']"
# 厂区、区域、区段、库区、库位选择
select1 = "//div[@class='v-card v-sheet theme--light']//tbody/tr[1]"
select_submit = "//div[@class='v-card v-sheet theme--light']//span[contains(text(),' 确定')]"
area1 = "//body/div/div[4]/div/div/div/div/div"
section1 = "//body/div/div[5]/div/div/div/div/div"
reservoir1 = "//body/div/div[6]/div/div/div/div/div"
stolocation1 = "//body/div/div[7]/div/div/div/div/div"

# 弹框确定按钮
yes_button = "//div[@class='DialogActions']//span[contains(.,'确定')]"
# ----------------------------------------------退料页面元素---------------------------------
delete_wo = "//*[contains(text(),'已删除工单')]"
isselect = "//div[@class='v-input--selection-controls__input']//input"

# 新容器
new_container = "//label[text()='存储在新容器中']"
container_type = "//form/div[4]/div[3]/div/div/div[1]/div[1]/div[1]/div"
type_C1 = "//div[@role='listbox']//div[text()='C1']"
type_C2 = "//div[@role='listbox']//div[text()='C2']"
tare = "//form/div[4]/div[5]/div/div/div[1]/div/input"
tare_unit = "//form/div[4]/div[6]/div/div/div[1]/div[1]/div[1]/div"
tare_g = "//div[@role='listbox']//div[text()='g']"
tare_kg = "//div[@role='listbox']//div[text()='kg']"
factory = "//form//div[5]/div[1]/div[1]/div/div[1]/div[1]/input"
area = "//form/div[5]/div[2]/div/div/div[1]/div[1]/div[1]"
section = "//form/div[5]/div[3]/div/div/div[1]/div[1]/div[1]"
reservoir = "//form/div[5]/div[4]/div/div/div[1]/div[1]/div[1]"
stolocation = "//form/div[5]/div[5]/div/div/div[1]/div[1]/div[1]"
# 已有容器
exist_container = "//label[text()='存储在已有容器']"
first_container = "//div[@role='row' and @row-index='0']"

# ---------------------------------------------------------------------------------------------

# ----------------------------------------------取消称量页面元素----------------------------------
c_factory = "//form/div[1]/div[1]/div[1]/div/div[1]/div[1]/input"
c_area = "//form/div[1]/div[2]/div/div/div[1]/div[1]/div[1]"
c_section = "//form/div[1]/div[3]/div/div/div[1]/div[1]/div[1]"
c_reservoir = "//form/div[1]/div[4]/div/div/div[1]/div[1]/div[1]"
c_stolocation = "//form/div[1]/div[5]/div/div/div[1]/div[1]/div[1]"
add = "//span[text()='新增']"
any_ele = "//div[@class='col col-2']"

