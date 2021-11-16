# -*- coding: utf-8 -*-
class Test(object):
    def __init__(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def s(cls, string):
        s = string.split(',')
        return cls(b=s[0], c=s[1], a=s[2])

    def get(self):
        return self.a


a = Test().s('a,b,c')
print(a.get())
