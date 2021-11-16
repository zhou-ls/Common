# -*- coding: utf-8 -*-
class Human:

    def __init__(self, name):
        self.name = name

    # def __str__(self):
    #     return 'Name1: %s' % self.name

    def __repr__(self):
        return 'Name:%s' % self.name

    # 方法
    def eat(self):
        print('eat method')

    def run(self):
        print('run method')


human = Human('Python')
# 该类没有实现__str__，但是打印对象的时候，会执行__repr__
print(human)
