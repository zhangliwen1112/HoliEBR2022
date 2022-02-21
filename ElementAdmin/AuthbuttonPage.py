#coding=utf-8

"""
Created on 2020/9/8
@author: lianxiujuan
@desc: 权限按钮
"""


# 登录后“权限管理”按钮
authmg = '//span[text()="权限管理"]'

# “系统设置”下”权限按钮“按钮
authbu = "//span[text()='权限按钮']"

# 权限按钮中新增/编辑/删除按钮
add ='//span[text()="新增"]'
edit = '//div[@class="app-content ivu-layout-content"]//span[text()="编辑"]'
delete = '//span[text()="删除"]'

# 新增/编辑权限按钮名称/备注
code = '//input[@placeholder="请输入编码"]'
name = '//input[@placeholder="请输入名称"]'
ramark = '//input[@placeholder="请输入备注"]'
i18n = '//input[@placeholder="请输入国际化键"]'
submit = "//span[contains(text(),'确定')]"
yes_button = '//div[@class="ivu-modal-footer"]//span[text()="确定"]'
cancel_button = '//span[contains(text(),"取消")]'
tabel_code = '//div[@role="presentation"]//span[text()="编码"]'  # 表头的编码列

# 删除权限按钮中的删除按钮
delete_yes_button = '//div[@class="ivu-poptip-footer"]//span[text()="确定"]'
