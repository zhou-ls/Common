# -*- coding: utf-8 -*-
# @Time : 2020/8/24 17:55
# @Author : zls
# @File : shunxu.py
# @Software: PyCharm

"""
装饰顺序 : 就近原则
    被装饰的函数，组装装饰器时，是从下往上装饰

执行顺序 : 就远原则
    装饰器调用时是从上往下调用
"""


def f1(func):
    print("开始装饰f1")

    def inner(*args, **kwargs):
        print("进入f1")
        result = func(*args, **kwargs)
        print("进入f1里面")
        return result
    return inner


def f2(func):
    print("开始装饰f2")

    def inner(*args, **kwargs):
        print("进入f2")
        result = func(*args, **kwargs)
        print("进入f2里面")
        return result
    return inner


@f1
@f2
def fn():
    print("进入fn")
    return "结束"


test = fn()
print(test)
