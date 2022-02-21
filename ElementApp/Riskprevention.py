#coding=utf-8
#
# """
# Created on 2020/9/14
# @author: lianxiujuan
# @desc: 危险防范
# """


# 登录页码元素
material = '//div[@class="v-list-item theme--light"]//div[text()="物料管理"]'
riskpre = '//div[text()="危险防范信息"]'

# 危险防范上端按钮
add = "//span[text()='新增']"
edit = "//span[text()='编辑']"
delete = "//span[text()='删除']"

# 新增/编辑危险防范界面元素
allinput = "//div[@class='v-dialog v-dialog--active v-dialog--persistent v-dialog--scrollable']//input[@type='text']"
yes_button = "//div[@class='v-dialog v-dialog--active v-dialog--persistent v-dialog--scrollable']//span[text()='确定']"

# 删除危险防范
delete_yes_button = '//button[@color="red"]//span[contains(text(),"确定")]'
