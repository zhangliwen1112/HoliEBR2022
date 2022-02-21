# -*- coding: utf-8 -*- 
# @Time : 2020/11/16 17:18 
# @Author : 张丽雯 
# @File : palletpackPaga.py 
# @中文描述 :  托盘包装方式

# 登录页码元素
inventory= "//*[contains(text(),'库存管理')]"
pallet = "//*[contains(text(),'托盘')]"
palletpack = "//*[contains(text(),'托盘包装方式')]"

# 托盘包装方式上端按钮
add = "//span[contains(.,'新增')]"
edit = "//span[contains(.,'编辑')]"
delete = "//span[contains(.,'删除')]"
refresh = "//span[contains(.,'刷新')]"

#新增页面
material = '//form/div/div/div/div/div/div/div/div/div/div/div/div/div/input'
material_select = "//div[@role='menu']//input"
material1 = '//td/div/div'
material_submit = '//div[3]/div/div[3]/button/span'
supplier = '//form/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/input'
supplier1 = '//div[4]/div/div[2]/div/table/tbody/tr/td/div/div'
supplier_submit = '//div[4]/div/div[3]/button/span'
pallet_tare = '//div[3]/div/div/div/div/div/div/div/div/div/div/div/div[4]/div/div/div/div/input'
container_tare = '//div[2]/div/div/div/div/div/div[4]/div/div/div/div/input'
pallet_num = '//div[2]/div/div/div/div/div[2]/div/div/div/div/div/input'
container = '//div[2]/div/div/div/div/div[2]/div[2]/div/div/div/div/input'
submit = "//button[contains(.,'确定')]"
cancle = "//button[contains(.,'取消')]"
material_title = '//button/div/i'
# 筛选,按name过滤条件
select = "//span[contains(.,'筛选')]"
select_name = '//div[3]/div[2]/div[2]/div[2]/div/div'
name_text = "//div[2]/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/input"
#选中第一条
# first = "//*[@id='app']/div[1]/main/div/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]"
first = '//div[@role="row" and @row-index="0"]'
#删除
yes_button = "//div[@class='DialogActions']//span[contains(.,'确定')]"
cancle_button = "//div[@class='DialogActions']//span[contains(.,'取消')]"
