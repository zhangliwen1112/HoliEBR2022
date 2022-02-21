#coding=utf-8
#
# """
# Created on 2020/9/14
# @author: lianxiujuan
# @desc: 取样规则页码元素
# """


# 登录页码元素
material = '//div[@class="v-list-item theme--light"]//div[text()="物料管理"]'
samplerule = '//div[text()="取样规则"]'

# 取样规则上端按钮
add ='//div[@class="flex shrink"]//span[text()="新增"]'
edit = '//div[@class="flex shrink"]//span[text()="编辑"]'
delete = '//div[@class="flex shrink"]//span[text()="删除"]'

# 新增/编辑取样规则界面元素
allinput = '//div[@class="v-card v-sheet theme--light"]//input[@type="text"]'
desc = '//textarea'
addscope = '//div[@class="v-card v-sheet theme--light"]//span[text()="新增"]'
deletescope = '//div[@class="v-card v-sheet theme--light"]//span[text()="删除"]'
yes_button = '//div[@class="v-dialog v-dialog--active v-dialog--persistent v-dialog--scrollable"]//span[text()="确定"]'

cancel_button = '//div[@class="v-dialog v-dialog--active v-dialog--persistent v-dialog--scrollable"]//span[text()="取消"]'

# 删除取样规则
delete_yes_button = '//button[@color="red"]//span[contains(text(),"确定")]'
