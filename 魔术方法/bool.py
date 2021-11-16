# -*- coding: utf-8 -*-
# @Time : 2020/8/24 18:24
# @Author : zls
# @File : bool.py
# @Software: PyCharm
class Human:

    def __init__(self, name):
        self.name = name

    def __bool__(self):
        if self.name == 'cheng':
            return True
        else:
            return False

    # 方法
    def eat(self):
        print('eat method')

    def run(self):
        print('run method')


human = Human('cheng')
human2 = Human('Python')
print(bool(human))
print(bool(human2))
