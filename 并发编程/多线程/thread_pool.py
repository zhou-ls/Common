# -*- coding: utf-8 -*-
import queue
import threading
import time


# 声明线程池管理类
class WorkManager(object):
    def __init__(self, work_num=1000, thread_num=2):
        self.work_queue = queue.Queue()  # 任务队列
        self.threads = []  # 线程池
        self.__init_work_queue(work_num)  # 初始化任务队列，添加任务
        self.__init_thread_pool(thread_num)  # 初始化线程池，创建线程

    def __init_thread_pool(self, thread_num):
        """
           初始化线程池
        """
        for i in range(thread_num):
            # 创建工作线程(线程池中的对象)
            self.threads.append(Work(self.work_queue))

    def __init_work_queue(self, jobs_num):
        """
           初始化工作队列
        """
        for i in range(jobs_num):
            self.add_job(do_job, i)

    def add_job(self, func, *args):
        """
           添加一项工作入队
        """
        self.work_queue.put((func, list(args)))  # 任务入队，Queue内部实现了同步机制

    def wait_allcomplete(self):
        """
           等待所有线程运行完毕
        """
        for item in self.threads:
            if item.isAlive():
                item.join()


class Work(threading.Thread):
    def __init__(self, work_queue):
        threading.Thread.__init__(self)
        self.work_queue = work_queue
        self.start()

    def run(self):
        # 死循环，从而让创建的线程在一定条件下关闭退出
        while True:
            try:
                do, args = self.work_queue.get(block=False)  # 任务异步出队，Queue内部实现了同步机制
                do(args)
                self.work_queue.task_done()  # 通知系统任务完成
            except:
                break


# 具体要做的任务
def do_job(args):
    time.sleep(0.1)  # 模拟处理时间
    print(threading.current_thread())
    print(list(args))


if __name__ == '__main__':
    start = time.time()
    work_manager = WorkManager(100, 10)  # 或者work_manager =  WorkManager(10000, 20)
    work_manager.wait_allcomplete()
    end = time.time()
    print("cost all time: %s" % (end - start))
