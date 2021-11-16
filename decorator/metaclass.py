# -*- coding: utf-8 -*-
# 定义一个元类


class FirstMetaClass(type):
    # cls代表动态修改的类
    # name代表动态修改的类名
    # bases代表被动态修改的类的所有父类
    # class_dic代表被动态修改的类的所有属性、方法组成的字典
    def __new__(cls, name, bases, class_dic):
        # 动态为该类添加一个name属性
        print("cls     :", cls)  # <class '__main__.FirstMetaClass'>
        # class_dic['name'] = "C语言中文网"
        # class_dic['say'] = lambda self: print("调用 say() 实例方法")
        return super().__new__(cls, name, bases, class_dic)  # 返回实例对象

    def __init__(cls, name, bases, class_dic):
        super().__init__(cls)
        print("实例对象成功")
        print("self    ：", cls)  # <class '__main__.CLanguage'>
        print(name)  # CLanguage
        print(bases)  # (<class 'object'>,)
        print(class_dic)  # {'__module__': '__main__', '__qualname__': 'CLanguage', 'name': 'C语言中文网', 'say': <function FirstMetaClass.__new__.<locals>.<lambda> at 0x0000028717EE87B8>}


# 定义类时，指定元类
class CLanguage(object, metaclass=FirstMetaClass):
    pass


clangs = CLanguage()
print('------------------------------------')
# print(clangs.name)
# clangs.say()
