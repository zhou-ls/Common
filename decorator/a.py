# -*- coding: utf-8 -*-
def f1(func):
    def inner(*args, **kwargs):
        print(1)
        d = abs(func(*args, **kwargs))
        print("取绝对值")
        return d
    return inner


def f2(value):
    def out(func):
        def inner(*args, **kwargs):
            print(2)
            f = value * func(*args, **kwargs)
            print("执行乘法")
            return f
        return inner
    return out


@f2(value=10)
@f1
def add(a, b):
    c = a - b
    return c


t = add(3, 5)
print(t)
