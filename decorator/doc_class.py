# -*- coding: utf-8 -*-
#
# class Test(object):
#     def __init__(self, name, year):
#         self.name, self.year = name, year
#
#     def __call__(self, *args, **kwargs):
#         print("__call__使用测试")
#         print(*args)
#         print([i for i in args])
#
#
# t = Test("zla", "22")
# t(1, 2, 3, 4)
# print(t.name, t.year)


class Test1(object):
    """
    类装饰器的使用
    """

    def __init__(self, func):
        print('test init')
        print('func name is %s ' % func.__name__)
        self.func = func

    def __call__(self, *args, **kwargs):
        print('装饰器中的功能')
        self.func()

    def pr(self, a, b):
        print("测试输出")
        return a + b

@Test1
def func():
    print('this is test func')


func()

# print(Test1(test).pr(3, 4))
# print(t.pr(3, 4))
