# -*- coding: utf-8 -*- 
# @Time : 2021/1/20 9:10 
# @Author : 张丽雯 
# @File : OrganizeData.py 
# @中文描述 :  组织机构
# --------------------------------正常场景--------------------------------------------
add_name = "addcomp001"
code = '0004'
add_type = '公司'
edit_name = '公司002-修改'
edit_type = '部门'

add_name2 = "addcomp002"
code2 = '0006'
add_type2 = '部门'

users = "adduser001"
user_code = "xinzeng001"
tel = '18600000000'
status = "在职"
male = "女"

edit_users = "新增用户-修改"
edit_tel = "18600000002"
edit_status = "离职"
# ------------------------------------------------------------------------------------

# --------------------------异常场景------新增组织机构名称异常场景--------------------------
org_name1 = " "  # 为空
org_name2 = "_1234"  # 特殊字符开头，比如下划线字符开头
org_name3 = "name&org"  # 含有特殊字符
org_name4 = "机构"
add_orgname_abnormal_list = [(org_name1, code, add_type),
                             (org_name2, code, add_type),
                             (org_name3, code, add_type)
                             ]
add_orgname_abnormal1 = [(org_name1, code, add_type)]  # 名称为空
add_orgname_abnormal2 = [(org_name2, code, add_type)]  # 以特殊字符开头
add_orgname_abnormal3 = [(org_name3, code, add_type)]  #  中间含有特殊字符

# --------------------------异常场景------编辑组织机构名称异常场景--------------------------
org_name1 = " "  # 为空
org_name2 = "_1234"  # 特殊字符开头，比如下划线字符开头
org_name3 = "name&org"  # 含有特殊字符
edit_orgname_abnormal_list = [(org_name1, add_type),(org_name2, add_type),(org_name3, add_type)]

# --------------------------异常场景------新增组织机构编码异常场景--------------------------
org_code1 = " "  # 为空
org_code2 = "_1234"  # 特殊字符开头，比如下划线字符开头
org_code3 = "code&org"  # 含有特殊字符
add_orgcode_abnormal_list = [(add_name, org_code1, add_type),
                             (add_name, org_code2, add_type),
                             (add_name, org_code3, add_type)]

# ----------------------------异常场景------新增用户姓名异常场景---------------------------
username1 = " "  # 姓名为空
username2 = "#wang"  # 特殊字符开头
username3 = "张三&shdsdhh"  # 姓名中含有特殊字符
add_user_abnormal_list = [(username1, user_code, tel, status, male),
                          (username2, user_code, tel, status, male),
                          (username3, user_code, tel, status, male)]
# ----------------------------异常场景------新增用户编码异常场景---------------------------
code1 = " "  # 编码为空
code2 = "123"  # 编码字符不够
code3 = "12345678901"  # 编码超过11个字符
code4 = "urllib3介绍&"  # 编码含有特殊字符
code5 = "12编码"  # 编码含有中文字符
add_code_abnormal_list = [(users, code1, tel, status, male),
                          (users, code2, tel, status, male),
                          (users, code3, tel, status, male),
                          (users, code4, tel, status, male),
                          (users, code5, tel, status, male)]
# ----------------------------异常场景------新增用户手机号码异常场景---------------------------
tel1 = " "  # 号码为空
tel2 = "1"  # 号码位数不够
tel3 = "186000000001"  # 号码超过11个字符
tel4 = "1860000000a"  # 号码含有特殊字符
add_tel_abnormal_list = [(users, code, tel1, status, male),
                         (users, code, tel2, status, male),
                         (users, code, tel3, status, male),
                         (users, code, tel4, status, male)]
# ----------------------------异常场景------修改用户姓名异常场景---------------------------
name1 = " "  # 姓名为空
name2 = "#wang"  # 特殊字符开头
name3 = "张三&shdsdhh"  # 姓名中含有特殊字符
edit_user_abnormal_list = [(name1, tel, status),
                           (name2, tel, status),
                           (name3, tel, status)]
# ----------------------------异常场景------修改用户手机号码异常场景---------------------------
tel1 = " "  # 号码为空
tel2 = "1"  # 号码位数不够
tel3 = "186000000001"  # 号码超过11个字符
tel4 = "1860000000a"  # 号码含有特殊字符
edit_tel_abnormal_list = [(users, tel1, status),(users, tel2, status),(users, tel3, status),(users, tel4, status)]
# -----------------------------------------------------------------------------------------
