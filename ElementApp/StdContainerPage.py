# -*- coding: utf-8 -*- 
# @Time : 2020/11/16 14:21 
# @Author : 张丽雯 
# @File : standardcontainerPage.py 
# @中文描述 :  标准容器页面

# 登录页码元素
inventory= "//*[contains(text(),'库存管理')]"
container = "//*[contains(text(),'容器')]"
standardcontainer = "//*[contains(text(),'标准容器')]"

# 标准容器上端按钮
add = "//span[contains(.,'新增')]"
edit = "//span[contains(.,'编辑')]"
delete = "//span[contains(.,'删除')]"
refresh = "//span[contains(.,'刷新')]"

#新增页面
type = '//form/div/div/div/div/div/div/div/div'
type1 = '//body/div/div[3]/div/div/div[1]'
name = '//form/div/div/div[2]/div/div/div/div/input'
quality = '//form/div/div/div[3]/div/div/div/div/input'
hight = '//form/div/div/div[4]/div/div/div/div/input'
length = '//form/div/div/div[5]/div/div/div/div/input'
width = '//form/div/div/div[6]/div/div/div/div/input'
ratio = '//form/div/div/div[7]/div/div/div/div/input'
tare = '//form/div/div/div[8]/div/div/div/div/input'
slectunit = '//form/div/div/div[9]/div/div/div/div/div'
unit1 = "//div[@role='listbox']//div[text()='g']"
unit2 = "//div[@role='listbox']//div[text()='kg']"
edit_unit1 = '//body/div/div[3]/div/div/div[1]'
edit_unit2 = '//body/div/div[3]/div/div/div[2]'
submit = "//button[contains(.,'确定')]"
cancle = "//button[contains(.,'取消')]"

#选中第一条
first = "//div[@role='row' and @row-index='0']//div[@col-id='code']"

#删除
yes_button = "//div[@class='DialogActions']//span[contains(.,'确定')]"
cancle_button = "//div[@class='DialogActions']//span[contains(.,'取消')]"




