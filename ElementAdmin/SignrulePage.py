#coding=utf-8

"""
Created on 2020/9/7
@author: lianxiujuan
@desc: 签名规则
"""


# 登录后“系统设置”按钮
authmg = "//span[text()='系统设置']"

# “系统设置”下”签名设置“按钮
signset = "//span[text()='签名设置']"

# 签名规则中新增/编辑/删除按钮
add = "//div[@class='right']//i[@class='ivu-icon ivu-icon-md-add']"
edit = "//div[@class='right']//i[@class='ivu-icon ivu-icon-md-create']"
delete = "//div[@class='right']//i[@class='ivu-icon ivu-icon-md-remove']"
submit = "//div[@x-placement='top']//span[text()='确定']"
# 新增/编辑签名规则
name = '//input[@placeholder="请输入" and @class="ivu-input ivu-input-default"]'

yes_button = '//div[@class="ivu-modal-wrap"]//span[contains(text(),"确定")]'
cancel_button = '//div[@class="ivu-modal-footer"]//span[contains(text(),"取消")]'
