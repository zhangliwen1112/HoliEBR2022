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

# 新增属性页面元素
input_text = "//div[@class='v-dialog v-dialog--active v-dialog--persistent v-dialog--scrollable']//div[@class='v-text-field__slot']//input"
type = "//div[@class='v-select__selection v-select__selection--comma']"
text_type = "//div[@role='listbox']//div[text()='文本']"
num_type = "//div[@role='listbox']//div[text()='数字']"
list_type = "//div[@role='listbox']//div[text()='列表']"
status_type = "//div[@role='listbox']//div[text()='状态']"
# 数字类型\列表类型需要定义选项
selection = "//div[@class='row justify-space-around']//div[@class='v-input--selection-controls__input']"



# 新增状态值页面元素
status_button = "//div[@class='row no-gutters']//span[text()='新增']"
status_select1 = "//label[text()='计数管理']"
status_select2 = "//label[text()='影响链接的设备']"
status_select3 = "//label[text()='有效期']"

# 新增转换规则页面元素
rule_add = "//div[@class='row no-gutters']//span[contains(text(),' 新增')]"
# 点击下拉选项
select = "//div[@class='container grid-list-md']//div[@class='v-select__selections']"
select_option = "//div[@class='v-menu__content theme--light v-menu__content--fixed menuable__content__active']//div[@role='listbox']//div[@class='v-list-item__title']"

rule_type1 = "//div[@role='listbox']//div[text()='超过有效期']"
rule_type2 = "//div[@role='listbox']//div[text()='生产步骤']"
rule_type3 = "//div[@role='listbox']//div[text()='超过最大循环数']"
submit = "//span[text()='确定']"
cancle = "//button[contains(.,'取消')]"

# 状态信息第一行
status_first = "//div[@class='row no-gutters']//div[@class='ag-pinned-left-cols-container']"

# 状态信息编辑按钮
status_edit = "//div[@class='row no-gutters']//span[text()='编辑']"

# 状态信息删除按钮
status_delete = "//div[@class='row no-gutters']//span[text()='删除']"

# 弹框确定、取消按钮
yes_button = "//div[@class='DialogActions']//span[contains(.,'确定')]"
cancle_button = "//div[@class='DialogActions']//span[contains(.,'取消')]"


