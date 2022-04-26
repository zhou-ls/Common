# -*- coding: utf-8 -*-
import threading
import time

"""
通过继承threading.Thread定义子类创建多线程
"""


class MyThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print("Starting " + self.name)
        print_time(self.name, self.counter, 5)
        print("Exiting " + self.name)


def print_time(thread_name, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s process at: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1


# 创建新线程
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

# 开启线程
thread1.start()
thread2.start()

# 等待线程结束
thread1.join()
thread2.join()

print("Exiting Main Thread")
