# -*- coding: utf-8 -*-
# Created by lensen on 2021/7/3 23:13.
from 设计模式.适配器.adapter import Adapter1

@Adapter1
class Human:
    # @Adapter
    def speak(self):
        print('says hello')
        return 'says hello'

if __name__ == '__main__':
    Human.execute()

    human = Human
    # human.speak()
    human.execute()
