#coding=utf-8

"""
Created on 2020/10/14
@author: lianxiujuan
@desc: 供应商页码元素
"""


# 登录页码元素
inventory = "//*[text()='库存管理']"
supplier = "//*[text()='供应商信息']"

# 供应商信息上端按钮
add = "//*[text()='新增']"
edit = "//*[text()='编辑']"
delete = "//*[text()='删除']"

# 新增/编辑供应商界面元素
allinput = '//div[@class="v-card v-sheet theme--light"]//input'
email = '//textarea'
yes_button = '//div[@class="v-card v-sheet theme--light"]//span[text()="确定"]'
cancle = '//span[text()="取消"]'
# 删除供应商
delete_yes_button = '//button[@color="red"]'
