'''
进程是最小的内存分配单位
线程是操作系统调度的最小单位
线程被cpu执行了
进程内至少含有一个线程
进程中可以开启多个线程
    开启一个线程所需要的时间要远远小于开启一个进程
    多个线程内部有自己的数据线，数据不共享
    全局变量在多个线程之间是共享的


cpython的解释器  有gil的限制
全局解释器所   gil
         同一时刻只能有一个线程访问cpu
         锁的是什么？
           线程
         是python语言的问题？
           是cpython的问题，也是cpython的特性
编译型语言 在编译过程中就可以感知到需要启多少线程 所有不会产生解释性语言多线程的问题
全局解释器锁是解释性语言的软肋  php也是解释性语言

在cpython解释器下的python程序，在同一时刻 多个线程中，只能有一个线程被cpu执行

高cpu  计算类  ----高cpu利用率
高io   input time.sleep
       爬去网页
      qq聊天
      处理web请求
      读写数据库

高cpu 多进程
高io  多线程
'''

from threading import Thread
from multiprocessing import Process
import time

def func(n):
    n+1

if __name__ == '__main__':
    start_time=time.time()
    t_lst=[]
    for i in range(100):
        t=Thread(target=func,args=(i,))
        t.start()
        t_lst.append(t)
    [s.join() for s in t_lst]
    end_time=time.time()-start_time

    start_time1=time.time()
    p_lst=[]
    for j in range(100):
        p=Process(target=func,args=(j,))
        p.start()
        p_lst.append(p)
    [b.join() for b in p_lst]
    end_time1=time.time()-start_time1
    print(end_time,end_time1)

