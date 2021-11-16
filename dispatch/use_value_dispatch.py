# -*- coding: utf-8 -*-
from dispatch.value_dispatch import value_dispatch


@value_dispatch
def get_discount(level):
    return "等级错误"


@get_discount.register(1)
def parse_level_1(level):
    # 此处可有大量计算代码
    discount = 0.1
    return discount


# @get_discount.register(2)
# def parse_level_2(level):
#     # 此处可有大量计算代码
#     discount = 0.2
#     return discount
#
#
# @get_discount.register(3)
# def parse_level_3(level):
#     # 此处可有大量计算代码
#     discount = 0.3
#     return discount


# 当用户等级为2或者3时，折扣都是0.2
@get_discount.register(2)
@get_discount.register(3)
def parse_level_4(level):
    # 此处可有大量计算代码
    discount = 0.2
    return discount


discount = get_discount(1)
print(f'等级1的用户，获得的折扣是：{discount}')
discount = get_discount(3)
print(f'等级3的用户，获得的折扣是：{discount}')
