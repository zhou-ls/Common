# -*- coding: utf-8 -*-
import threading
import time


def target():
    print("threading %s is running" % threading.current_thread().name)  # Thread-1
    time.sleep(1)
    print("threading %s is ended" % threading.current_thread().name)  # Thread-1


print("the current threading %s is running" % threading.current_thread().name)  # 主线程
# 属于线程t的部分
t = threading.Thread(target=target)
t.start()
# 属于线程t的部分
t.join()  # join是阻塞当前线程(此处的当前线程是主线程) 主线程直到Thread-1结束之后才结束，即主线程是最后结束
print("the current threading %s is ended" % threading.current_thread().name)  # 主线程
