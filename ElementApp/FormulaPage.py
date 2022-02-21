# coding=utf-8
# """
# Created on 2020/9/16
# @author: zhangliwen
# @desc: 处方管理
# """

# 登录页码元素
formula = "//*[contains(text(),'处方管理')]"

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
name = '//div[2]/div/div/div[2]/form/div/div/div[2]/div/div/div[1]/div/input'
type = '//form/div/div/div[4]/div/div/div/div/div'
type1 = "//div[@role='listbox']//div[text()='测试/研发']"
type2 = "//div[@role='listbox']//div[text()='生产/临床']"
product_code = '//form/div/div/div[7]/div/div/div/div/input'
product_search = '//div[7]/div/div/div/div/div/input'
product_search1 = "//td/div/div"  # 选择搜索结果的第一个
product_search2 = "//tr[2]/td[1]/div/div"  # 选择搜索结果的第一个
product_submit = '//div[4]/div/div[3]/button/span'
product_cancle = '//div[3]/div/div[3]/button[2]'
r_num = '//div[12]/div/div/div/div/input'
r_unit = '//div[13]/div/div/div/div/div'
unit1 = "//div[@role='listbox']//div[text()='mg']"
unit2 = "//div[@role='listbox']//div[text()='g']"
unit3 = "//div[@role='listbox']//div[text()='kg']"
unit4 = "//div[@role='listbox']//div[text()='lb']"
weight = "//div[14]/div/div/div/div/input"
# equivalent_weight = '//div[14]/div/div/div/div/input'
w_unit = "//div[15]/div/div/div/div/div"
w_unit1 = "//body/div[2]/div[6]/div/div/div/div/div"
w_unit2 = "//div[2]/div[6]/div/div/div[2]/div/div"
w_unit3 = "//div[6]/div/div/div[3]/div/div"
dose = "//div[16]/div/div/div/div/input"
dose_form = "//div[17]/div/div/div/div/input"
catalog = "//div[18]/div/div/div/div/input"
item = "//div[19]/div/div/div/div/input"
add_submit = "//button[contains(.,'确定')]"
add_cancle = "//button[contains(.,'取消')]"

# 筛选,第一个过滤条件
select = "//span[contains(.,'筛选')]"
select_name = "//div[3]/div[3]/div[2]/div[2]/div[2]/div/div[1]/span[3]"
name_text = "//body/div/div[1]/main/div/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div/" \
            "div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/input"
# 选中第一条
first = "//div[@role=\"row\" and @row-index=\"0\"]"

# 处方物料 按钮
material_add = "//div[2]/div/div/div/div/div/div/header/div/div/div/button"
material_edit = "//div[2]/div/div/div/div/div/div/header/div/div/div[2]/button"
material_delete = "//div[2]/div/div/div/div/div/div/header/div/div/div[3]/button"
material_refresh = "//div[2]/div/div/div/div/div/div/header/div/div/div[4]/button"

# 处方物料新增/编辑页面元素
material_name = "//div[3]/div/div/div[2]/form/div/div/div/div/div/div/div/input"
material_search = "//body/div/div[6]/div/div[1]/div/div[1]/div[1]/input"
material_search1 = "//tbody/tr[1]"
# material_search1 = "//body/div/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/div"
material_submit = "//div[@class='text-sm-right pt-2']//span[contains(.,'确定')]"
material_main = "//div[3]/div/div/div[2]/form/div/div/div[3]/div/div/div/div/div"
material_tail = "//div[3]/div/div/div[2]/form/div/div/div[4]/div/div/div/div/div"
compensator = '//div[3]/div/div/div[2]/form/div/div/div[5]/div/div/div/div/div'
no_compensator = '//body//div[@class="v-list-item__content"]//div[text()="非补偿物料:该物料不是补偿物料"]'
potency_compensator = ""
material_period = "//div[3]/div/div/div[2]/form/div/div/div[6]/div/div/div/div/input"
material_num = "//div[3]/div/div/div[2]/form/div/div/div[8]/div/div/div/div/input"
material_unit = "//div[3]/div/div/div[2]/form/div/div/div[9]/div/div/div/div/div"
material_unit1 = "//body/div/div[5]/div/div/div[1]"
material_unit2 = "//body/div/div[5]/div/div/div[2]"
material_unit3 = "//body/div/div[5]/div/div/div[3]"
material_yes = "//div[3]/div/div/div[3]/button[2]/span"

# 提交、批准处方
yes_button = "//div[@class='DialogActions']//span[contains(.,'确定')]"
cancle_button = "//div[@class='DialogActions']//span[contains(.,'取消')]"
