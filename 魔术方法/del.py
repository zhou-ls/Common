# -*- coding: utf-8 -*-
class Human:

    def __init__(self, name):
        print('init method for {}'.format(name))

    def __new__(cls, name):
        print(name)
        if name == 'chengjie':
            r = super(Human, cls).__new__(cls)
            return r
        else:
            pass

    def __del__(self):
        print('del method')


    # 方法
    def eat(self):
        print('eat method')

    def run(self):
        print('run method')


human = Human('chengjie')  # 执行这一步实例化对象human之后, 会先触发__new__打印出chengjie,返回实例化对象,再触发 __init__,打印出init method for chengjie
human2 = human
del human  # 此时不会触发__del__，在程序最后才会触发，如果没有human2 = human，则在此处调用del会触发__del__，程序最后则不会触发
print('running') # 在执行完这一句之后，会触发__del__，打印出del method，__del__总是会在程序最后被触发
