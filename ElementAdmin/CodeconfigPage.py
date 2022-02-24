#coding=utf-8

"""
Created on 2020/9/15
@author: lianxiujuan
@desc: 编码配置
"""


# 登录进入编码配置界面
syset = '//span[text()="系统设置"]'
codeconfig = '//span[text()="编码配置"]'

# 编码配置中新增/编辑/删除/重置按钮
add ='//span[text()="新增"]'
edit = '//span[text()="编辑"]'
delete = '//span[text()="删除"]'
reset = '//span[text()="重置"]'

# 新增/编辑编码配置
code = "//input[@placeholder='请输入编码']"
name = "//input[@placeholder='请输入名称']"
desc = "//input[@placeholder='请输入描述']"
insertitem = '//span[text()="4位长度的年"]'
insert = '//span[text()="插入"]'
circleway = '//div[@class="ivu-select-selection"]'
circlevalue1 = '//li[text()="年"]'
circlevalue2 = '//li[text()="月"]'
circlevalue3 = '//li[text()="日"]'
circlevalue4 = '//li[text()="最大值"]'
yes_button = '//button[@class="ivu-btn ivu-btn-primary"]//span[contains(text(),"确定")]'
cancel_button = '//span[contains(text(),"取消")]'

# 删除界面
delete_yes_button = '//button[@class="ivu-btn ivu-btn-primary ivu-btn-small"]//span[text()="确定"]'

# 重置界面
reset_yes_button = '//button[@class="ivu-btn ivu-btn-primary ivu-btn-large"]//span[text()="确定"]'
