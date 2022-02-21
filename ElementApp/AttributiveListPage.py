# -*- coding: utf-8 -*- 
# @Time : 2020/11/18 11:23 
# @Author : 张丽雯 
# @File : attributivelistPage.py 
# @中文描述 :  属性列表
# 登录页码元素
device = "//*[contains(text(),'设备管理')]"
attributive = "//*[contains(text(),'属性列表')]"

# 属性列表上端按钮
add = "//span[contains(.,'新增')]"
edit = "//span[contains(.,'编辑')]"
copy = "//span[contains(.,'复制')]"
effect = "//span[contains(.,'生效')]"
noeffect = "//span[contains(.,'失效')]"
refresh = "//span[contains(.,'刷新')]"
check = "//span[contains(.,'查看')]"

# 新增页面元素
code = '//form/div/div/div/div/div/div/div/input'
type = '//form/div/div/div[2]/div/div/div/div/div'
text_type = "//body//div[@role='listbox']//div[text()='文本']"
num_type = "//body//div[@role='listbox']//div[text()='数字']"
list_type = "//body//div[@role='listbox']//div[text()='列表']"
status_type = "//body//div[@role='listbox']//div[text()='状态']"
name = '//form/div/div[2]/div/div/div/div/div/input'
text = '//form/div/div[3]/div/div/div/div/div/input'
# 数字类型\列表类型需要定义选项
select1 = '//form/div/div[3]/div/div/div/div/div/div/div'
select2 = '//form/div/div[3]/div/div/div[2]/div/div/div/div'
select3 = '//form/div/div[3]/div/div/div[3]/div/div/div/div'
select4 = '//form/div/div[3]/div/div/div[4]/div/div/div/div'
# 新增状态值页面元素
status_button = '//div[2]/div[2]/button'
status_code = '//div[3]/div/div/div[2]/form/div/div/div/div/div/div/div/input'
status_name = '//div[3]/div/div/div[2]/form/div/div/div[2]/div/div/div/div/input'
status_select1 = "//label[text()='计数管理']"
status_select2 = "//label[text()='影响链接的设备']"
status_select3 = "//label[text()='有效期']"
status_submit = '//div[3]/div/div/div[3]/button[2]/span'
# 新增转换规则页面元素
rule_button = '//div[4]/div[2]/div[2]/button/span'
start_code = '//div[3]/div/div/div[2]/form/div/div/div/div/div/div/div/div'
start_code1 = '//body/div/div[4]/div/div/div'
rule_type = '//div[3]/div/div/div[2]/form/div/div[2]/div/div/div/div/div/div'
rule_type1 = "//body//div[@role='listbox']//div[text()='超过有效期']"
rule_type2 = "//body//div[@role='listbox']//div[text()='生产步骤']"
rule_type3 = "//body//div[@role='listbox']//div[text()='超过最大循环数']"
end_code = '//div[3]/div/div/div[2]/form/div/div[3]/div/div/div/div/div/div'
end_code1 = '//body/div/div[6]/div/div/div'
rule_submit = '//div[3]/div/div/div[3]/button[2]/span'
submit = "//button[contains(.,'确定')]"
cancle = "//button[contains(.,'取消')]"

# 状态信息第一行
status_first = "//div[2]/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[2]"

# 状态信息编辑按钮
status_edit = '//div[2]/button[2]'

# 状态信息删除按钮
status_delete = '//button[3]'

# 状态转换信息编辑按钮
rule_edit = '//div[4]/div[2]/div[2]/button[2]'

#状态转换第一行
rule_first = '//div[4]/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div'

# 状态转换信息删除按钮
rule_delete = '//div[4]/div[2]/div[2]/button[3]'

# 弹框确定、取消按钮
yes_button = "//div[@class='DialogActions']//span[contains(.,'确定')]"
cancle_button = "//div[@class='DialogActions']//span[contains(.,'取消')]"

# 筛选,按name过滤条件
select = "//span[contains(.,'筛选')]"
select_name = '//div[3]/div[2]/div[2]/div[2]/div/div'
name_text = "//div[2]/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/input"
