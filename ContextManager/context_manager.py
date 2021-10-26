# -*- coding: utf-8 -*-
"""
上下文管理器的使用：
    一个类只要实现了__enter__()和 __exit__() 这两个方法，通过该类创建的对象我们就称之为上下文管理器
    上下文管理器可以使用 with 语句， with 语句之所以这么强大，背后是由上下文管理器做支撑，open() 函数创建的文件对象就是就是一个上下文管理器对象。
"""


# 上下文管理器 类 的实现方式
class File:
    def __init__(self, file_name, file_mode):
        self.file_name = file_name
        self.file_mode = file_mode

    def __enter__(self):
        # 上下文方法， 负责返回操作对象资源，比如：文件对象，数据库连接对象
        self.file = open(self.file_name, self.file_mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.file.close()
        print("over")


with File("1.txt", 'r') as f:
    # content = f.read()
    # print(content)
    f.write("qqq")  # 虽然报错， 但仍然执行了 关闭连接操作 __exit__()

# 上下文管理器装饰器方式实现
from contextlib import contextmanager


# 加上装饰器， 下面的函数创建的对象就是一个上下文管理器
@contextmanager
def my_open(file_name, file_mode):
    global file
    try:
        file = open(file_name, file_mode)
        # yield 关键字之前的代码可以认为是上文方法， 负责返回操作对象资源
        yield file
    except Exception as e:
        print(e)
    finally:
        # yield 关键字后面的代码可以认为是下文方法，负责释放操作对象的资源
        file.close()
        print("over")


with my_open("1.txt", "r") as f:
    # content = f.read()
    # print(content)
    f.write("qqq")  # 虽然报错， 但仍然执行了 关闭连接操作 __exit__()
