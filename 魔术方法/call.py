# -*- coding: utf-8 -*-
class MakeCake:
    def __init__(self, name):
        self.name = name

    def buy_yuan_liao(self):
        print('购买原料')

    def huo_mian(self):
        print('和面')

    def fa_jiao(self):
        print('发酵')

    def hong_bei(self):
        print('烘焙')

    def __call__(self, *args, **kwargs):
        if self.name == 'test':
            self.buy_yuan_liao()
            self.huo_mian()
            self.fa_jiao()
            self.hong_bei()
            print('蛋糕制作完成')

    def __repr__(self):
        return "MakeCake[buy_yuan_liao=" + '购买原料' + ",huo_mian=" + '和面' + "]"


maek_cake = MakeCake('test')  # 实例化一个类MakeCake的对象make_cake
maek_cake()  # 把对象make_cake当做一个函数调用
print(maek_cake)
