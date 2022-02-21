# -*- coding: utf-8 -*- 
# @Time : 2020/10/14 10:06 
# @Author : 张丽雯 
# @File : weightPage.py
# @中文描述 :  砝码配置

# 登录页码元素
weightmanage = "//*[contains(text(),'称量管理')]"
weight = "//*[contains(text(),'砝码配置')]"


# 砝码配置上端按钮
add = "//span[contains(.,'新增')]"
edit = "//span[contains(.,'编辑')]"
delete = "//span[contains(.,'删除')]"
refresh = "//span[contains(.,'刷新')]"

#新增\编辑页面元素
name = "//form/div/div/div/div/div/div/div/input"
weight_value = "//form/div/div/div[2]/div/div/div/div/input"
weight_unit = "//form/div/div/div[3]/div/div/div/div/div"
unit_mg = "//div[@role='listbox']//div[text()='mg']"
unit_g = "//div[@role='listbox']//div[text()='g']"
unit_kg = "//div[@role='listbox']//div[text()='kg']"
unit_lb = "//div[@role='listbox']//div[text()='lb']"
submit = "//span[contains(.,'确定')]"
cancel = "//span[contains(.,'取消')]"

#删除确定、取消
yes_button = "//div[@class='DialogActions']//span[contains(.,'确定')]"
cancel_button = "//div[@class='DialogActions']//span[contains(.,'取消')]"

# 筛选,按name过滤条件
select = "//span[contains(.,'筛选')]"
select_name = '//div[3]/div[3]/div[2]/div[2]/div/div/div/span[3]'
name_text = "//div[2]/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/input"