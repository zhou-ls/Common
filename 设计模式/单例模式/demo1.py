# -*- coding: utf-8 -*-
# Created by lensen on 2021/7/4 17:16.
"""使用 __new__ 方法"""


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class Foo(Singleton):
    pass


if __name__ == '__main__':
    f1 = Foo()
    f2 = Foo()
    print(id(f1))
    print(id(f2))
