# -*- coding: utf-8 -*-
# Created by lensen on 2021/7/4 17:21.
"""使用闭包方式
通过判断该类是否已经创建了实例，
若没有进行过实例化，则我们让其进行实例化，
反之，返回原有对象即可。
"""


def singleton(cls):
    instances = None
    def get_instance(*args, **kwargs):
        nonlocal instances
        if instances is None:
            instances = cls(*args, **kwargs)
        return instances
    return get_instance


@singleton
class Bar(object):
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    b1 = Bar('alex')
    b2 = Bar('hello')
    print(b1.name)
    print(b2.name)
