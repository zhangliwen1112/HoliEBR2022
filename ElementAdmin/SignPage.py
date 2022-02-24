#coding=utf-8

"""
Created on 2020/9/7
@author: lianxiujuan
@desc: 签名策略
"""


# 登录后“系统设置”按钮
authmg = "//span[text()='系统设置']"

# “系统设置”下”签名设置“按钮
signset = "//span[text()='签名设置']"

# 签名策略中新增/编辑/删除按钮
add ='//div[@class="left"]//i[@class="ivu-icon ivu-icon-md-add"]'
edit = '//div[@class="left"]//i[@class="ivu-icon ivu-icon-md-create"]'
delete = '//div[@class="left"]//i[@class="ivu-icon ivu-icon-md-remove"]'

# 新增/编辑签名策略名称/备注
name_remark = '//input[@placeholder="请输入" and @class="ivu-input ivu-input-default"]'
yes_button = "//div[@class='ivu-modal-wrap']//span[contains(text(),'确定')]"
cancel_button = '//div[@class="ivu-modal"]//span[contains(text(),"取消")]'

#删除界面
delete_yes_button = '//div[@class="ivu-poptip-footer"]//span[text()="确定"]'
