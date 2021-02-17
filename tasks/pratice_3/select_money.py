# -*-encoding:utf-8 -*-

# @File     : select_money.py
# @Data     : 2021-02-17 17:00
# @Author   : Administrator

import money
import send_money

def select_money(bSendSalary, salary = 0):
    # 直接查询当前存款，不考虑是否发工资
    if bSendSalary:
        return send_money.send_money(salary)
    else:
        return money.saved_money

