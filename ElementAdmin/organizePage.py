#coding=utf-8
#
# """
# Created on 2020/9/3
# @author: zhangliwen
# @desc:组织结构页面
# """
# from .base import Page
from selenium.webdriver.common.by import By

# 登录后“组织机构”按钮 xpath
organize = "//span[contains(.,\'组织机构\')]"

# 组织机构 右侧表格上方按钮
add ="//button[contains(.,'新增')]"
edit = '//*[contains(text(),"编辑")]'
refresh ='//*[contains(text(),"刷新")]'
delete = '//*[contains(text(),"删除")]'

# -----------------------------组织机构树表 增删改刷新按钮-----------------------
o_add ="//i[@class='ivu-icon ivu-icon-md-add']"
o_delete ="//i[@class='ivu-icon ivu-icon-md-remove']"
o_edit ="//i[@class='ivu-icon ivu-icon-md-create']"
o_refresh ="//i[@class='ivu-icon ivu-icon-md-refresh']"
# ----------------------------组织机构树表 新增组织机构--------------------------
input_text = "//div[@class='ivu-modal-wrap']//input[@class='ivu-input ivu-input-default']"

#选择类型
OrganType2 = "//label[contains(text(),'公司')]"  #选择公司
OrganType3 = "//label[contains(text(),'部门')]"  #选择部门
#所属父级
OrganUpper = "//div[@class='ivu-cascader-label']" #选择框
Upper1 = "//span/ul/li" #第一级
Upper2 = "//span/span/ul/li" #第二级
Upper3 = "//span/span/span/ul/li" #第三级
#新增组织机构--确定 、取消按钮
add_submit = "//span[contains(text(),'确定')]"
add_cancel = "//span[contains(text(),'取消')]"

#展开树表结构
group = "//div[1]/div/div[3]/div/ul/li/div/div" #集团
company1 = "//div[1]/div/div[3]/div/ul/li/ul/li[1]" #集团下第一个公司
company1_1 = '//div[1]/div/div[3]/div/ul/li/ul/li[1]/ul/li'
company2 = "//li/ul/li[2]/div/div/span" #集团下第二个公司
company2_1 = "//div[1]/div/div[3]/div/ul/li/ul/li[2]/ul/li[1]/span" #第二个公司下第一个部门

#删除树表结构
delete_submit = "//div[@class='ivu-poptip-inner']//span[text()='确定']"
delete_cancel = "//div[@class='ivu-poptip-inner']//span[text()='取消']"

# ------------------------------------新增用户弹框页面--------------------------------------------

add_UserSta = "//span[@class='ivu-select-placeholder']"
edit_UserSta = "//span[@class='ivu-select-selected-value']"
UserSta_online = "//li[contains(.,'在职')]"
UserSta_off = "//li[contains(.,'离职')]"
UserMale1 = "//label[contains(.,'男')]"
UserMale2 = "//label[contains(.,'女')]"
UserDate = "//i[@class='ivu-icon ivu-icon-ios-calendar-outline']"
UserDate_first = "//em[1]"  #出生日期选择第一天
UserOrg = "//li/label/span/input"  #选择集团
UserOrg1 = "//li/ul[1]/li/label/span/input" #集团下第1个公司
UserOrg2 = "//li/ul[2]/li/label/span/input" #集团下第2个公司
UserOrg2_1 = "//li/ul[2]/li/ul[1]/li/label/span/input" #集团下第2个公司下第一个部门


User_cancel = "//div[15]/div[2]/div/div/div[3]/div/button[1]/span"
#删除用户 确定、取消按钮
DetUser_cancel = "//button[@class='ivu-btn ivu-btn-text ivu-btn-small']"
DetUser_submit = "//div[@x-placement='bottom']//button[@class='ivu-btn ivu-btn-primary ivu-btn-small']"