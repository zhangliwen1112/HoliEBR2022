# -*- coding: utf-8 -*- 
# @Time : 2021/1/29 16:58 
# @Author : 张丽雯 
# @File : StolocationmovePage.py 
# @中文描述 :  库位移动

# 登陆元素
inventory = "//*[contains(text(),'库存管理')]"
stolocationmove = "//*[contains(text(),'库位移动')]"

# 页面上方按钮元素
move = "//span[text()='移动']"
detail = "//span[text()='明细']"

# 移动页面元素
target_location = "//input[@readonly='readonly']"
type_text = "//input[@type='text']"
select_input = "//div[@class='v-card v-sheet theme--light']//label[text()='搜索...']"
select1 = "//div[@class='v-card v-sheet theme--light']//tbody/tr[1]"
select_submit = "//div[@class='v-card v-sheet theme--light']//span[contains(text(),' 确定')]"
title = "//div[@class='flex shrink']"
location_submit = "//span[text()='确定']"
