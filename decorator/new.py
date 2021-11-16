# -*- coding: utf-8 -*-
class CapStr(str):
    def __new__(cls, string):
        print(cls)
        self_in_init = super().__new__(cls, string)
        print(id(self_in_init))  # 打印返回值的id(内存地址)
        print(self_in_init)
        return self_in_init

    def __init__(self, string):
        print(self)
        print(id(self))
        self.string = string
        print(self.string)


a = CapStr("I love China!")
print(id(a))
