# -*- coding: utf-8 -*- 
# @Time : 2020/11/18 11:22 
# @Author : 张丽雯 
# @File : AttributivelistData.py
# @中文描述 :  属性列表
import random
attributive_code1 = 's9002'+str(random.randint(0,199))
attributive_code2 = 'l9002'+str(random.randint(0,199))
attributive_code3 = 't9002'+str(random.randint(0,199))
attributive_code4 = 'n9002'+str(random.randint(0,199))
attributive_type1 = '状态'
attributive_type2 = '列表'
attributive_type3 = '文本'
attributive_type4 = '数字'
attributive_name1 = 'attributive_s'+str(random.randint(0,199))
attributive_name2 = 'attributive_l'+str(random.randint(0,199))
attributive_name3 = 'attributive_t'+str(random.randint(0,199))
attributive_name4 = 'attributive_n'+str(random.randint(0,199))
text_long = '15'
attributive_list = [
                    (attributive_code1,attributive_type1,attributive_name1),
                    (attributive_code2,attributive_type2,attributive_name2),
                    (attributive_code4,attributive_type4,attributive_name4)
                    ]
attributive_text = [(attributive_code3, attributive_type3, attributive_name3, text_long)]
code_value = '2'
code_name = '12'
select_rule = '超过有效期'
edit_name = 'xiugai_attributive'


# 复制属性数据
copy_code = 'fuzhi_109'
copy_name = "copy_name109"
