#coding=utf-8

"""
Created on 2020/9/10
@author: lianxiujuan
@desc: 签名路径页面元素
"""


# 登录签名路径界面
sysset = '//span[text()="系统设置"]'
signpath = '//span[text()="签名路径"]'

# 签名路径界面中表格上端按钮
add ='//span[text()="新增"]'
edit = '//span[text()="编辑"]'
delete = '//span[text()="删除"]'
verify = '//span[text()="验证"]'
cancelverify = '//span[text()="取消验证"]'

# 新增/编辑签名路径界面的元素
code_name_level = '//input[@placeholder="请输入" and @class="ivu-input ivu-input-default"]'
addsignlevel ='//div[@class="content-center ivu-col ivu-col-span-3"]//span[text()="新增"]'

# 新增签名级别界面
group = '//i[@class="ivu-icon ivu-icon-ios-arrow-down ivu-select-arrow"]'
admingp = '//span[text()="管理员组"]'
usergp = '//span[text()="普通用户组"]'

yes_button = '//span[text()="确定"]'
cancel_button = '//div[@class="ivu-modal-content"]//span[contains(text(),"取消")]'
