# -*- coding: utf-8 -*- 
# @Time : 2020/11/19 9:10 
# @Author : 张丽雯 
# @File : EqpcategoryPage.py 
# @中文描述 :  设备类别接口

# 登录页码元素
device = "//*[contains(text(),'设备管理')]"
eqp = "//*[contains(text(),'接口管理')]"
eqpcategory = "//*[contains(text(),'设备类别接口')]"

# 属性列表上端按钮
edit = "//span[contains(.,'编辑')]"
equipment = "//span[contains(.,'设备')]"
refresh = "//span[contains(.,'刷新')]"
check = "//span[contains(.,'查看')]"

# 筛选,按类别编码过滤条件
select = "//span[contains(.,'筛选')]"
select_code = "//body//div[@class='ag-tool-panel-wrapper']//span[contains(.,'类别编码')]"
code_text = "//div[2]/div[1]/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/input"

# 弹框确定、取消按钮
yes_button = "//div[@class='DialogActions']//span[contains(.,'确定')]"
cancle_button = "//div[@class='DialogActions']//span[contains(.,'取消')]"

# 新增接口
add = "//span[contains(.,'新增')]"
eqp_code = '//div[3]/div/div/div[2]/form/div/div/div/div/div/div/div/input'
eqp_name = '//form/div/div[2]/div/div/div/div/div/input'
submit = "//span[contains(.,'确定')]"
# 切到输出tab
eqp_out = "//div[@role='tab'][text()='输出']"

# 输出新增按钮
out_add = "//div[@class='row']//span[text()='新增']"

# 新增输出参数
out_code = '//div[4]/div/div/div[2]/form/div/div/div/div/div/div/div/input'
out_name = '//div[4]/div/div/div[2]/form/div/div/div[2]/div/div/div/div/input'
out_type = '//form/div/div/div[3]/div/div/div/div/div'
out_type1 = "//div[@role='listbox']//div[text()='文本']"
out_type2 = "//div[@role='listbox']//div[text()='数字']"
out_submit = '//div[4]/div/div/div[3]/button'

# 输出编辑按钮
out_edit = "//div[@class='row']//span[text()='编辑']"

# 输出删除按钮
out_delete = "//div[@class='row']//span[text()='删除']"

# 关闭类别界面
close = "//button[contains(.,'关闭')]"

