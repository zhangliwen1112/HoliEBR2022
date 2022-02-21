# -*- coding: utf-8 -*- 
# @Time : 2021/1/22 15:11 
# @Author : lianxiujuan 
# @File : elements.py 
# @中文描述 : 系统内公用元素



# ----------------------------- 每个页面右侧的搜索框 --------------------------
# 筛选按钮
search = "//span[contains(.,'筛选')]"
# 筛选条件
def searchitem(string):
    return "//span[@ref='eTitle'][text()='%s']"%string
# 筛选内容 --输入筛选内容
search_text = "//input[@ref='eInput' and @placeholder='过滤条件...']"
# 通过选择组件，筛选条件
search_select = "//select[@id='filterText']"
# 选项内容
def searchoption(string):
    return "//option[text()='%s']"%string
# 表单第一行第一列的值
firstdata_admin = '//div[@row-index="0"]//span[@aria-colindex="2"]'
firstdata_app = '//div[@row-index="0"]//div[@aria-colindex="2"]'
# ----------------------------------------------------------------------------

# ------------------------------签名弹框元素----------------------------------
sign = "//span[contains(.,'签名')]"
user = "//input[@autocomplete='new-password' and @type='text']"
pwd = "//input[@autocomplete='new-password' and @type='password']"
sign_yes = "//div[@class='v-dialog v-dialog--active v-dialog--" \
           "persistent v-dialog--scrollable']//span[text()='确定']"
# ----------------------------------------------------------------------------

# ------------------------------xpath相同元素---------------------------------
# 类型为li的xpath元素
def xpath_litype(string):
    return '//li[text()="%s"]'%string
# ----------------------------------------------------------------------------

# --------------------------不同颜色的button----------------------------------
primary_button = '//button[@color="primary"]'
red_button = '//button[@color="red"]'
# ----------------------------------------------------------------------------

# ------------------------------界面提示语元素--------------------------------
alert_txt = "//div[@class='v-alert__content']//div[@class='mr-2']"
# -----------------------------------------------------------------------------

# ------------------------------多页签相关-------------------------------------
# 正在打开的页签 的关闭按钮
close_tab = "//div[@aria-selected='true']//i[@title='删除']"
# -----------------------------------------------------------------------------

# ------------------------------app页面错误元素--------------------------------
error_message = "//div[@class='v-messages__message']"
error_message2 = "//div[@class='v-messages__message message-transition-enter-to']"
# -----------------------------------------------------------------------------

# ------------------------------admin页面错误元素--------------------------------
error_tips = "//div[@class='ivu-form-item-error-tip']"
# -----------------------------------------------------------------------------
