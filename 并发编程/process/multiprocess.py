# -*- coding: utf-8 -*-
# 参考： https://www.cnblogs.com/jiangfan95/p/11439207.html
import urllib
from multiprocessing.dummy import Pool as ThreadPool

urls = [
    'https://www.baidu.com',
    'https://www.sina.com.cn',
    'https://www.163.com',
    'https://www.qq.com'
]

# make the Pool of workers
pool = ThreadPool(4)
# open the urls in their own threads and return the results
results = pool.map(urllib.request.urlopen, urls)
# close the pool and wait for the work to finish
pool.close()
pool.join()
