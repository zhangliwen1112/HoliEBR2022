# -*- coding: utf-8 -*- 
# @Time : 2021/1/13 16:22
# @Author : lianxiujuan 
# @File : SignpathapplyPage.py 
# @中文描述 : 签名路径应用

# 登录签名路径应用页面
mimg = "//span[text()='生产管理']"
signpathapply = "//span[text()='签名路径应用']"

# 页面上端按钮
config = "//span[text()='新增']"
delete = "//span[text()='删除']"

# 配置页面
config_select = '//span[contains(text(),"选择")]'
miresult_select = '//div[@row-index="0"]//input[@ref="eInput" and@aria-label="Toggle Row Selection"]'
selectbutton = '//i[@class="ivu-icon ivu-icon-ios-arrow-down ivu-select-arrow"]'
yes_button = "//div[@class='ivu-modal-wrap']//span[contains(text(),'确定')]"

# 选择签名路径页面
select_code = "//i[@class='ivu-icon ivu-icon-ios-more']"
input_select = "//div[@class='ivu-row']//input[@placeholder='搜索...']"
select = "//input[@type='radio']"

# 页面第一行
first_row = '//div[@row-index="0"]//div[@col-id="miCode"]'

# 删除确定按钮
submit = "//button[@class='ivu-btn ivu-btn-primary ivu-btn-small']"