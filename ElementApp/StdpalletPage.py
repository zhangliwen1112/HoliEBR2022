#coding=utf-8

"""
Created on 2020/10/14
@author: lianxiujuan
@desc: 标准托盘页码元素
"""


# 登录页码元素
inventory = "//*[text()='库存管理']"
pallet = "//*[text()='托盘']"
stdpallet = "//*[text()='标准托盘']"

# 标准托盘上端按钮
add = "//*[text()='新增']"
edit = "//*[text()='编辑']"
delete = "//*[text()='删除']"

# 新增/编辑标准托盘界面元素
allselect = '//div[@class="v-card v-sheet theme--light"]//i[text()="arrow_drop_down"]'
p6_type = '//div[text()="P6"]'
allinput = '//div[@class="v-card v-sheet theme--light"]//input[@type="text"]'
yes_button = '//div[@class="v-card v-sheet theme--light"]//span[text()="确定"]'

# 删除标准托盘
delete_yes_button = '//button[@color="red"]'
