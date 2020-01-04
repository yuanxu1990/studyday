'''
多进程中的组件
1 锁
2 信号量
   一套资源 同一时间 只能被n个人访问
   某一段代码 同一时间 只能被n个进程执行(类似于锁 )

3 队列

'''

from multiprocessing import Semaphore
from multiprocessing import Process
import time
import random

def ktv(i,sem):
    sem.acquire()
    print('%s走进ktv'%i)
    time.sleep(random.randint(1,5))
    print('%s走出ktv'%i)
    sem.release()


if __name__ == '__main__':
    sem=Semaphore(4)
    for i in range(20):
        p=Process(target=ktv,args=(i,sem))
        p.start()