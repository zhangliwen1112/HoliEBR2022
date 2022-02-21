# -*- coding: utf-8 -*- 
# @Time : 2020/10/14 10:54 
# @Author : 张丽雯 
# @File : cleanPage.py
# @描述 : 清洁配置

# 登录页码元素
cleanmanage = "//*[contains(text(),'称量管理')]"
clean = "//*[contains(text(),'清洁配置')]"


# 砝码配置上端按钮
add = "//span[contains(.,'新增')]"
edit = "//span[contains(.,'编辑')]"
delete = "//span[contains(.,'删除')]"
refresh = "//span[contains(.,'刷新')]"

#新增\编辑页面元素
rulecode = "//div[@class='layout row wrap']//input"
rule_name = "//div[@class='layout row wrap']//input[1]"
select_area = "//div[@class='v-select__selections']"
area1 = "//div[@class='v-list-item__content']"
select_ruletype = "//form/div/div/div[4]/div/div/div/div/div"
rule_type1 = "//body//div[@role='listbox']//div[text()='按工单清洁']"
rule_type2 = "//body//div[@role='listbox']//div[text()='按物料清洁']"
submit = "//span[text()='确定']"
cancle = "//span[contains(.,'取消')]"

#删除确定、取消
yes_button = "//div[@class='DialogActions']//span[contains(.,'确定')]"
cancle_button = "//div[@class='DialogActions']//span[contains(.,'取消')]"

# 筛选,按name过滤条件
select = "//span[contains(.,'筛选')]"
select_name = "//div[2]/div[2]/div/div/span[3]"
name_text = "//div[2]/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/input"