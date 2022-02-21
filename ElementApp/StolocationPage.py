#coding=utf-8

"""
Created on 2020/10/14
@author: lianxiujuan
@desc: 库位页码元素
"""


# 登录页码元素
inventory = "//*[text()='库存管理']"
storageloction = "//*[text()='库位']"

# 库位上端按钮
add = "//*[text()='新增']"
edit = "//*[text()='编辑']"
delete = "//*[text()='删除']"

# 新增/编辑库位界面元素
allinput = '//div[@class="v-card v-sheet theme--light"]//input'
infinite = "//tr[3]//td[2]//div[@class='v-input--selection-controls__input']"
yes_button = "//div[@class='v-card v-sheet theme--light']//span[text()='确定']"

kuqu_1 = "//div[@class='v-data-table__wrapper']//div[@class='v-input--selection-controls__ripple']"

# 删除库位
delete_yes_button = "//button[@color='red']"
