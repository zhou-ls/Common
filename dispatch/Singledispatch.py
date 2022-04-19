# -*- coding: utf-8 -*-
# 重载
from functools import singledispatch


@singledispatch
def show(obj):
    print(obj, type(obj), "obj")


@show.register(str)
def test(text):
    print(text, type(text), "str")


@show.register(int)
def test(n):
    print(n, type(n), "int")


show([1])
show(1)
show("xx")
