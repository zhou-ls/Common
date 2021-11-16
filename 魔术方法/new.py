# -*- coding: utf-8 -*-
class Human:

    def __init__(self, name):
        print('init method for {}'.format(name))

    def __new__(cls, name):
        print(name)
        if name == 'chengjie':
            r = super(Human, cls).__new__(cls)
            print(r)  # <__main__.Human object at 0x000001A887D81C50>
            return r
        else:
            pass

    # 方法
    def eat(self):
        print('eat method')

    def run(self):
        print('run method')


human = Human('chengjie')  # 执行这一步实例化对象human之后, 会先触发__new__打印出chengjie,返回实例化对象,再触发 __init__,打印出init method for chengjie
