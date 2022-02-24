#coding=utf-8

"""
Created on 2020/9/15
@author: lianxiujuan
@desc: MI管理
"""


# 登录进入MI管理界面
promg = "//*[contains(text(),'生产管理')]"
mimg = "//*[contains(text(),'MI管理')]"

# MI管理中新增/编辑/删除按钮
add = "//button[contains(.,'新增')]"
edit = "//button[contains(.,'编辑')]"
delete = "//button[contains(.,'删除')]"
design = "//button[contains(.,'设计')]"
approve = "//button[contains(.,'批准')]"
publish = "//button[contains(.,'发布')]"

# 新增/编辑MI
code = "//input[@placeholder='请按照格式要求填写数据']"
desc = "//input[@class='ivu-input ivu-input-default' and @maxlength='50']"
yes_button = "//button[@class='ivu-btn ivu-btn-primary']//span[contains(text(),'确定')]"
cancel_button = '//div[@class="ivu-modal-footer"]//span[contains(text(),"取消")]'

# 删除界面
delete_cancel_button = "//button[@class='ivu-btn ivu-btn-primary ivu-btn-small']//span[text()='确定']"

# 删除、批准、发布 确定按钮
submit = "//div[@class='ivu-modal-confirm-footer']//span[text()='确定']"

# ######################################################### 设计页面 #####################################################
# 流程控制
start = "//div[text()='start']"
end = "//div[text()='end']"
save = "//span[text()='保存']"
close = "//i[@class='ivu-icon ivu-icon-md-close']"
# 工艺实例
weighting = "//div[text()='weighing']"
reconcilliation = "//div[text()='reconcilliation']"
combination = "//div[text()='combination']"
statement= "//div[text()='statement']"

# 左侧标题
control = "//span[text()='流程控制']"
process = "//span[text()='工艺实例']"
subflows = "//span[text()='工序流程']"

# 流程元素
port_out = "//*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g'][4]/*[name()='g'][1]/*[name()='g'][3]"
port_in = "//*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g'][4]/*[name()='g'][6]/*[name()='g'][3]"

# 称量
weight_in = "//*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g'][4]/*[name()='g'][2]/*[name()='g'][3]"
weight_out = "//*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g'][4]/*[name()='g'][2]/*[name()='g'][4]"

# 集中
reconcilliation_in = "//*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g'][4]/*[name()='g'][3]/*[name()='g'][3]"
reconcilliation_out = "//*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g'][4]/*[name()='g'][3]/*[name()='g'][4]"

# 混合
combination_in = "//*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g'][4]/*[name()='g'][4]/*[name()='g'][3]"
combination_out = "//*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g'][4]/*[name()='g'][4]/*[name()='g'][4]"

# 声明
statement_in = "//*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g'][4]/*[name()='g'][5]/*[name()='g'][3]"
statement_out = "//*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g'][4]/*[name()='g'][5]/*[name()='g'][4]"

#设计页面
start1 = "//*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g'][4]/*[name()='g'][1]"
start_text = "//input[@placeholder='Name']"
weight1 = "//*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g'][4]/*[name()='g'][2]"
weight_text = "//input[@placeholder='请输入组件名称']"
reconcilliation1 = "//*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g'][4]/*[name()='g'][3]"
reconcilliation_text = "//input[@placeholder='请输入集中组件标题']"
combination1 = "//*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g'][4]/*[name()='g'][4]"
combination_text = "//input[@placeholder='请输入混合组件标题']"
statement1 = "//*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g'][4]/*[name()='g'][5]"
statement_text = "//input[@id='node-input-name']"
end1 = "//*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g'][4]/*[name()='g'][6]"
end_text = "//input[@id='node-input-name']"
# subflow
subflow_in = "//*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g'][4]/*[name()='g'][7]/*[name()='g'][3]"
subflow_out = "//*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g'][4]/*[name()='g'][7]/*[name()='g'][4]"
tab1 = "//a[@title='流程1']"
# ----------------------------------------------------------子流程-------------------------------------------------------
add_subflow = "//div[@class='red-ui-tab-button red-ui-tabs-add']"
input_add = "//a[@id='workspace-subflow-input-add']"
output_add = "//a[@id='workspace-subflow-output-add']"
finish = "//button[@id='node-dialog-ok']"
# 工序组件
subflow = "//div[text()='Subflow 1']"
workcenter = "//div[text()='workcenter']"
datachange = "//div[text()='datachange']"
datachange_text = "//input[@placeholder='请输入数据变化组件的标题']"
title = "//div[text()='title']"
title_text = "//textarea[@placeholder='请输入标题文本']"
files = "//div[text()='files']"
files_text = "//input[@placeholder='请输入文件组件的标题']"
upload = "//div[text()='upload']"
upload_text = "//input[@placeholder='请输入上传组件的标题']"
workcenter1 = "//*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g'][4]/*[name()='g'][3]"
datachange1 = "//*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g'][4]/*[name()='g'][4]"
title1 = "//*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g'][4]/*[name()='g'][5]"
files1 = "//*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g'][4]/*[name()='g'][6]"
upload1 = "//*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g'][4]/*[name()='g'][7]"

input_out = "//*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g'][4]/*[name()='g'][1]/*[name()='g']"
output_in = "//*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g'][4]/*[name()='g'][2]/*[name()='g']"
upload_in = "//*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g'][4]/*[name()='g'][7]/*[name()='g'][3]"
upload_out = "//*[name()='svg']/*[name()='g']/*[name()='g']/*[name()='g'][4]/*[name()='g'][7]/*[name()='g'][4]"
# ----------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------导入MI流程元素--------------------------------------------------------
options_btn = "//a[@id='btn-deploy-options']"
import_btn = "//a[@id='flow-import']"
upload_btn = "//a[@id='import-file-upload-btn']"
upload_submit = "//button[@id='mi-dialog-ok']//span[text()='导入']"
current = "//a[@id ='import-tab-current']"
new = "//a[@id ='import-tab-new']"
flow_tab1 = "//a[@class='red-ui-tab-label']"
delete_node = "//button[@id='node-dialog-delete']"
upload_file1 = "//input[@type='file']"
# ----------------------------------------------------------------------------------------------------------------------

