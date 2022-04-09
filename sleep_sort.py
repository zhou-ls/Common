# -*- coding: utf-8 -*-
import threading
import time


# 睡觉排序,just a joke
def sleep_sort(n: int, arr: list):
    time.sleep(pow(1.1, float(n)))
    arr.append(n)


def run(old_arr: list, new_arr: list):
    thread_list = []
    for i in range(len(old_arr)):
        thread_list.append(threading.Thread(target=sleep_sort, args=(old_arr[i], new_arr,)))
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()


if __name__ == '__main__':
    old_arr = [-5, 3, 9, 11, -1, 5, -3, 8, 10, 13, 35, 22]
    new_arr = []
    run(old_arr, new_arr)
    print(new_arr)
