# -*- coding: utf-8 -*-

# @Time : 2021/1/13
# @Author : lianxiujuan
# @File : pageMImanage.py
# @中文描述 :  MI管理

from ElementAdmin.MIPage import *
from src.public.FunctionSet import *


# import win32gui
# import win32con


# 进入MI管理界面
def login_mimanage():
    new_click(promg)
    new_click(mimg)


# 新增MI
def mimanage_add(addcode):
    new_click(add)
    new_send_keys(code, addcode)
    ele = new_find_elements(yes_button)
    new_click_ele(ele[1])


# 编辑MI
def mimanage_edit(editdesc):
    new_click(edit)
    new_send_keys(desc, editdesc)
    ele = new_find_elements(yes_button)
    new_click_ele(ele[1])


# 删除MI
def mimanage_delete():
    new_click(delete)
    sleep(2)
    new_click(delete_cancel_button)


# 批准MI
def mimanage_approve():
    new_click(approve)
    sleep(2)
    new_click(submit)


# 发布 MI
def mimanage_publish():
    new_click(publish)
    sleep(2)
    new_click(submit)


# 进入MI设计页面
def mimanage_design_into():
    new_click(design)
    sleep(3)


# 设计MI
def mimanage_design():
    driver.switch_to_frame(0)
    new_drag_and_drop_by_offset(start, 150, 150)
    sleep(1)
    new_drag_and_drop_by_offset(weighting, 300, 150)
    sleep(1)
    new_drag_and_drop_by_offset(reconcilliation, 500, 150)
    sleep(1)
    new_drag_and_drop_by_offset(combination, 300, 200)
    sleep(1)
    new_drag_and_drop_by_offset(statement, 500, 200)
    sleep(1)
    new_drag_and_drop_by_offset(end, 550, 250)
    sleep(1)
    new_drag_and_drop(port_out, weight_in)
    sleep(1)
    new_drag_and_drop(weight_out, reconcilliation_in)
    sleep(1)
    new_drag_and_drop(reconcilliation_out, combination_in)
    sleep(1)
    new_drag_and_drop(combination_out, statement_in)
    sleep(1)
    new_click(add_subflow)
    sleep(2)
    new_click(input_add)
    sleep(1)
    new_click(output_add)
    sleep(2)
    new_click(control)
    sleep(1)
    new_click(process)
    sleep(2)
    new_drag_and_drop_by_offset(workcenter, 300, 20)
    sleep(2)
    new_drag_and_drop_by_offset(datachange, 350, 40)
    sleep(1)
    new_drag_and_drop_by_offset(title, 400, 50)
    sleep(1)
    new_drag_and_drop_by_offset(files, 450, 55)
    sleep(1)
    new_drag_and_drop_by_offset(upload, 500, 60)
    sleep(2)
    new_double_click(workcenter1)
    new_click(finish)
    sleep(2)
    new_double_click(datachange1)
    new_type(datachange_text, '数据修改组件')
    new_click(finish)
    sleep(2)
    new_double_click(title1)
    new_type(title_text, '标题组件测试')
    new_click(finish)
    sleep(2)
    new_double_click(files1)
    new_type(files_text, '文件组件测试')
    new_click(finish)
    sleep(2)
    new_double_click(upload1)
    new_type(upload_text, '上传组件测试')
    new_click(finish)
    sleep(2)
    new_drag_and_drop(input_out, upload_in)
    sleep(1)
    new_drag_and_drop(upload_out, output_in)
    sleep(1)
    new_click(tab1)
    sleep(2)
    new_drag_and_drop_by_offset(subflow, 450, 150)
    sleep(1)
    new_drag_and_drop(statement_out, subflow_in)
    sleep(1)
    new_drag_and_drop(subflow_out, port_in)
    sleep(1)
    new_double_click(start1)
    new_type(start_text, '开始组件')
    new_click(finish)
    sleep(2)
    new_double_click(weight1)
    new_type(weight_text, '称量组件')
    new_click(finish)
    sleep(2)
    new_double_click(reconcilliation1)
    new_type(reconcilliation_text, '集中组件')
    new_click(finish)
    sleep(2)
    new_double_click(combination1)
    new_type(combination_text, '混合组件')
    new_click(finish)
    sleep(2)
    new_double_click(statement1)
    new_type(statement_text, '声明组件')
    new_click(finish)
    sleep(2)
    new_double_click(end1)
    new_type(end_text, '结束组件')
    new_click(finish)
    sleep(2)
    new_click(save)
    sleep(2)
    driver.switch_to.default_content()
    sleep(2)


# 导入MI脚本
def mimanage_design_import(file):
    driver.switch_to_frame(0)
    sleep(1)
    new_click(options_btn)
    new_click(import_btn)
    base_dir = os.getcwd()
    base = base_dir.split("\\HoliEBR-UI\\")[0]
    upload_path = base + "\\HoliEBR-UI\\src\\public\\upload\\"
    new_find_element(upload_file1).send_keys(upload_path + file)
    sleep(2)
    new_click(upload_submit)
    sleep(1)
    driver.switch_to.default_content()


# 删除主流程
def mimanage_design_delete_tab():
    driver.switch_to_frame(0)
    sleep(1)
    new_double_click(flow_tab1)
    sleep(1)
    new_click(delete_node)
    new_click(save)
    sleep(3)
    driver.switch_to.default_content()


# 关闭设计页面
def mimanage_design_close():
    new_click(close)
