# -*- coding: utf-8 -*-
# Created by lensen on 2021/7/3 23:13.
class Adapter:
    def __init__(self, adapted_methods):
        # <适配器.adapter.Adapter object at 0x00000215070F6978>
        print(self)
        self.adapted_methods = adapted_methods
        print(self.__dict__)
        self.__dict__.update(dict(execute=self.adapted_methods))
        print(self.__dict__)

    def __call__(self):
        return self.adapted_methods


def Adapter2(func):
    print(func)

    def wrapper(self, *args, **kwargs):
        print('self: ', self)
        try:
            # print(self.__dict__)
            self.__dict__.update(dict(execute=self.func))
            print(self.__dict__)
        except:
            print('出错了')
        return func(self, *args, **kwargs)

    return wrapper


class Adapter1:
    def __init__(self, cls):
        # <适配器.adapter.Adapter1 object at 0x000001EFC9C86940>
        # print(self)
        self.cls = cls
        self.__dict__.update(dict(execute=self.cls().speak))
        # {'cls': <class '__main__.Human'>,
        # 'execute': <bound method Human.speak of <__main__.Human object at 0x000002192B1B6940>>}
        # print(self.__dict__)

    def __call__(self):
        # def wrapped(*args, **kwargs):
        #     return func(*args, **kwargs)
        return self.cls
