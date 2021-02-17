# -*-encoding:utf-8 -*-

# @File     : start.py
# @Data     : 2021-02-17 16:53
# @Author   : Administrator

# 定义一个start.py ，启动文件展示最终存款金额

import select_money

# 未发工资的存款
print(f"未发工资时存款：{select_money.select_money(0)}")
print(f"发1000工资后存款：{select_money.select_money(1, 1000)}")

