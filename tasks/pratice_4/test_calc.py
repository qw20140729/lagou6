# -*-encoding:utf-8 -*-

# @File     : test_calc.py
# @Data     : 2021-02-17 17:59
# @Author   : qyanls

import sys
sys.path.append(r'd:\lagou6')
from tasks.pratice_4.pythonCode.calc import Calculator
import pytest

class TestCalc(object):

    def setup(self):
        self.mycalc = Calculator()

    # 测试加法
    @pytest.mark.parametrize('a,b,result',[(1, 2, 4)])
    @pytest.mark.run(order=1)
    def test_add(self, a, b, result):
        assert self.mycalc.add(a, b) == result

    # 测试除法
    @pytest.mark.parametrize('a,b,result', [(1, 2, 4)])
    @pytest.mark.run(order=4)
    def test_div(self, a, b, result):
        assert self.mycalc.div(a, b) == result

    # 测试减法
    @pytest.mark.parametrize('a,b,result', [(1, 2, 4)])
    @pytest.mark.run(order=2)
    def test_sub(self, a, b, result):
        assert self.mycalc.sub(a, b) == result

    # 测试乘法
    @pytest.mark.parametrize('a,b,result', [(1, 2, 2)])
    @pytest.mark.run(order=3)
    def test_mul(self, a, b, result):
        assert self.mycalc.mul(a, b) == result

if __name__ == '__main__':
    pytest.main(['test_calc.py', '-v'])