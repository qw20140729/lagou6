# -*-encoding:utf-8 -*-

# @File     : send_money.py
# @Data     : 2021-02-17 16:54
# @Author   : Administrator
import money

# 定义发工资模块 send_money，用来增加收入计算
def send_money(salary):
    # 当前现有存款
    print(f"现有存款：{money.saved_money}")

    # 发工资salary
    nowed_money = money.saved_money + salary

    print(f"发工资后存款：{nowed_money}")

    return nowed_money

if __name__ == '__main__':
    send_money(1000)


