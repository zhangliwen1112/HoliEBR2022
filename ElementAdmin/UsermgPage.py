#coding=utf-8
#
# """
# Created on 2020/9/3
# @author: lianxiujuan
# @desc: 用户管理页面元素
# """


# 登录后“用户管理”按钮
usermg = "//span[text()='用户管理']"

# 用户管理界面中表格上端按钮
add ='//span[text()="新增"]'
edit = '//span[text()="编辑"]'
refresh = '//span[text()="刷新"]'
delete = '//span[text()="删除"]'
active = '//span[text()="激活/重置"]'
lock = '//span[text()="锁定"]'
unlock = '//span[text()="解锁"]'

# 新增/编辑用户界面的元素
username_mail_rfid = '//input[@placeholder="请输入" and @class="ivu-input ivu-input-default"]'
people_group = '//i[@class="ivu-icon ivu-icon-ios-arrow-down ivu-select-arrow"]'
select_list = "//ul[@class='ivu-select-dropdown-list']/li"
people_select = "//span[text()='lian']"
role1 = "//label[@class='ivu-radio-wrapper ivu-radio-group-item ivu-radio-wrapper-" \
        "checked ivu-radio-default']//input[@type='radio']"  # 系统管理员
role2 = "//label[@class='ivu-radio-wrapper ivu-radio-group-item ivu-radio-default']//input[@type='radio']"   #普通用户
admingp = '//ul[@class="ivu-select-dropdown-list"]//span[text()="管理员组"]'
usergp = '//ul[@class="ivu-select-dropdown-list"]//span[text()="普通用户组"]'
usermg_select = "//i[@class='ivu-icon ivu-icon-ios-arrow-down ivu-select-arrow']"
expiretime = "//input[@class='ivu-input ivu-input-default ivu-input-with-suffix']"

# 激活界面
newpw = "//div[@class='ivu-modal-wrap']//input[@class='ivu-input ivu-input-large']"
confirmpw = "//div[@class='ivu-modal-wrap']//input[@class='ivu-input ivu-input-default']"
yes_button = "//div[@class='v-transfer-dom']//span[text()='确定']"
submit_button = "//div[@class='ivu-modal-footer']//span[contains(text(),'确定')]"
cancel_button = "//button[@class='ivu-btn ivu-btn-default']/span[contains(text(),'取消')]"
lock_delete_yes_button = "//div[@x-placement='bottom']//button[@class='ivu-btn ivu-btn-primary ivu-btn-small']"

password = "//div[@class='ivu-modal-wrap']//input[@class='ivu-input ivu-input-default']"
