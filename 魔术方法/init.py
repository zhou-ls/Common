# -*- coding: utf-8 -*-
class Human:

    def __init__(self, name):
        print('init method for {}'.format(name))

    # 方法
    def eat(self):
        print('eat method')

    def run(self):
        print('run method')


human = Human('chengjie')  # 执行这一步实例化对象human之后, 会触发 __init__, 打印出init method for chengjie
