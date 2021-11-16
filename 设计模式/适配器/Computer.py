# -*- coding: utf-8 -*-
# Created by lensen on 2021/7/3 23:12.
class Computer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} computer'.format(self.name)

    def execute(self):
        return 'executes a program'
