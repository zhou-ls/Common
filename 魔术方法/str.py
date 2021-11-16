# -*- coding: utf-8 -*-
class Human:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Name: %s' % self.name

    # 方法
    def eat(self):
        print('eat method')

    def run(self):
        print('run method')


human = Human('Python')
# 如果没有__str__魔术方法，则打印出来的是类似于<__main__.Human object at 0x000001BFE3F39828>，这是继承自object的__str__方法
print(human)

