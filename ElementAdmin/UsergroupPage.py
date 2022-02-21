#coding=utf-8

"""
Created on 2020/9/3
@author: lianxiujuan
@desc: 用户组页面元素
"""


# 登录后“用户管理”按钮
authmg = '//span[text()="权限管理"]'

# “权限管理”下”用户权限“按钮
userauth = '//span[text()="用户权限"]'

# 用户管理界面中表格上端按钮
add ='//i[@class="ivu-icon ivu-icon-md-add"]'
edit = '//i[@class="ivu-icon ivu-icon-md-create"]'
delete = '//i[@class="ivu-icon ivu-icon-md-remove"]'

# 新增/编辑用户组界面中编码框
input = '//div[@class="ivu-modal-body"]//input[@placeholder="请输入" and @class="ivu-input ivu-input-default"]'
submit_button = "//button/span[contains(text(),'确定')]"
yes_button = "//div[@class='ivu-modal-footer']//span[text()='确定']"
cancel_button = '//div[@class="ivu-modal-footer"]//span[contains(text(),"取消")]'

# 设置权限
authlist = '//input[@type="checkbox" and @class="ivu-checkbox-input"]'

# 删除用户组界面中的确定按钮
delete_yes_button = '//button[@class="ivu-btn ivu-btn-primary ivu-btn-small"]//span[text()="确定"]'
