# -*- coding: utf-8 -*-
# Created by lensen on 2021/7/4 17:28.
"""
使用元类
"""


class SingleTonType(type):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        _instance = None  # 设置一个变量，用来存储是否创建实例
        print('cls:', cls)
        if _instance is None:
            obj = cls.__new__(cls, *args, **kwargs)  # 会一直找到能创建实例的父类，创建实例
            cls.__init__(obj, *args, **kwargs)  # 构造方法去丰富该实例
            cls._instance = obj  # 并将变量修改的创建的实例
        return _instance


class Foo(metaclass=SingleTonType):
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    obj1 = Foo('hello')  # 会调用type类（SingleTonType）中的call方法
    obj2 = Foo('world')
    print(id(obj1))
    print(id(obj2))
