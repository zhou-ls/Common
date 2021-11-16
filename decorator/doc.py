# -*- coding: utf-8 -*-
def makeBold(fun):
    print('----a----')

    def inner():
        print('----1----')
        return '<b>' + fun() + '</b>'

    return inner


def makeItalic(fun):
    print('----b----')

    def inner():
        print('----2----')
        return '<i>' + fun() + '</i>'

    return inner


@makeBold
@makeItalic
def func():
    print('----c----')
    print('----3----')
    return 'hello python decorator'


ret = func()
print(ret)
