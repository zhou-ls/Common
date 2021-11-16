# -*- coding: utf-8 -*-
class Human:

    def __init__(self, name):
        self.name = name

    def __len__(self):
        # 必须有返回值，而且必须是整型
        return len(self.name)

    # 方法
    def eat(self):
        print('eat method')

    def run(self):
        print('run method')


human = Human('chengjie')
# 如果没有实现__len__, 则无法直接使用len(human), 否则报TypeError: object of type 'Human' has no len(), 实现了__len__后，可以根据需要
print(len(human))
