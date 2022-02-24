# coding=utf-8
# """
# Created on 2020/9/16
# @author: zhangliwen
# @desc: 处方管理
# """

# 登录页码元素
formula = "//*[contains(text(),'配方管理')]"

# 处方管理上端按钮
add = "//span[contains(.,'新增')]"
edit = "//span[contains(.,'编辑')]"
copy = "//span[contains(.,'复制')]"
refresh = "//span[contains(.,'刷新')]"
revise = "//span[contains(.,'修订')]"
revoke = "//span[contains(.,'撤回')]"
submit = "//span[contains(.,'提交')]"
approve = "//span[contains(.,'批准')]"
verify = "//span[contains(.,'验证')]"
effect = "//span[contains(.,'生效')]"
noeffect = "//span[contains(.,'失效')]"
check = "//span[contains(.,'查看')]"
print1 = "//span[contains(.,'打印')]"
# 新增/编辑处方界面元素
name = "//div[@class='v-dialog v-dialog--active v-dialog--persistent v-dialog--scrollable']//div[@class='v-text-field__slot']//input"

# 点击下拉框按钮
select_selections = "//div[@class='v-select__selections']"

# 类型

type1 = "//div[@role='listbox']//div[text()='测试/研发']"
type2 = "//div[@role='listbox']//div[text()='生产/临床']"
# 产品编码

product ="//div[@class='v-text-field__slot']//input[@readonly='readonly']"

product_search = "//div[@class='v-input theme--light v-text-field v-text-field--single-line v-text-field--is-booted']//input"
product_search1 = "//div[@class='v-data-table__wrapper']//tr[1]/td[1]"  # 选择搜索结果的第一个

unit1 = "//div[@role='listbox']//div[text()='mg']"
unit2 = "//div[@role='listbox']//div[text()='g']"
unit3 = "//div[@role='listbox']//div[text()='kg']"
unit4 = "//div[@role='listbox']//div[text()='lb']"
weight = "//input[@name='weightEquivalent']"
add_submit = "//button[contains(.,'确定')]"
add_cancle = "//button[contains(.,'取消')]"

# 筛选,第一个过滤条件
select = "//span[contains(.,'筛选')]"

# 选中第一条
first = "//div[@role=\"row\" and @row-index=\"0\"]"

# 处方物料 按钮
material_add = "//div[@class='tab-table']//span[text()='新增']"
material_edit = "//div[@class='tab-table']//span[text()='编辑']"
material_delete = "//div[@class='tab-table']//span[text()='删除']"
material_refresh = "//div[@class='tab-table']//span[text()='刷新']"

# 处方物料新增/编辑页面元素

material_main = "//label[text()='主料']"
material_tail = "//label[text()='尾料半成品']"
compensator = "//div[@class='flex sm12']//div[@role='button']/div/div/div"
no_compensator = '//div[contains(text(),"非补偿物料:该物料不是补偿物料")]'
potency_compensator = '//div[contains(text(),"效价补偿")]'
# 输入框
input_text = "//div[@class='v-dialog v-dialog--active v-dialog--persistent v-dialog--scrollable']//div[@class='v-text-field__slot']//input"

material_yes = "//div[@class='v-dialog v-dialog--active v-dialog--persistent v-dialog--scrollable']//button[contains(.,'确定')]"

# 提交、批准处方
yes_button = "//div[@class='DialogActions']//span[contains(.,'确定')]"
cancle_button = "//div[@class='DialogActions']//span[contains(.,'取消')]"
