'''
线程池
   concurrent.futures模块提供了高度封装的异步调用接口
   ThreadPoolExecutor 线程池 提供异步调用
   ProcessPoolExecutor 进程池，提供异步调用

   #2 基本方法
#submit(fn, *args, **kwargs)
异步提交任务

#map(func, *iterables, timeout=None, chunksize=1)
取代for循环submit的操作

#shutdown(wait=True)
相当于进程池的pool.close()+pool.join()操作
wait=True，等待池内所有任务执行完毕回收完资源后才继续
wait=False，立即返回，并不会等待池内的任务执行完毕
但不管wait参数为何值，整个程序都会等到所有任务执行完毕
submit和map必须在shutdown之前

#result(timeout=None)
取得结果

#add_done_callback(fn)
回调函数

# done()
判断某一个线程是否完成

# cancle()
取消某个任务
'''
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import time,random

def func(n):
    time.sleep(2)
    print(n)
    return n*n

def call_back(a):
    print('结果是%s'%a.result())
#多进程的一般不超过cpu个数*5
t=ThreadPoolExecutor(max_workers=5)
t_lst=[]
# for i in range(20):
#     t1=t.submit(func,i)   #类似于t.apply_ascny
#     t_lst.append(t1)
# t.shutdown(True)       #类似于 t.close()+t.join()  如果返回值过多的话可以不阻塞
# for a in t_lst:
#     a.result()
for i in range(20):
    t.submit(func,i).add_done_callback(call_back)

#t.map(func,range(10))#如果使用map的话就拿不到 结果


