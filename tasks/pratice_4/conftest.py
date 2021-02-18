# -*-encoding:utf-8 -*-

# @File     : conftest.py.py
# @Data     : 2021-02-17 17:51
# @Author   : qyanls

import pytest

# 创建 fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
# 将 fixture 方法存放在 conftest.py ，设置 scope=module
@pytest.fixture(scope = "module")
def my_fixture():
    print("开始计算...")
    yield
    print("计算结束...")







