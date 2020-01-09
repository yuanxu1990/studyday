from multiprocessing import Pool
import os
import time

'''
进程池的同步调用 下边的子进程中的代码是同步执行的
'''
def func(n):
    print('start func%s'%n,os.getpid())
    time.sleep(1)
    print('end func%s'%n,os.getpid())

if __name__ == '__main__':
    p=Pool(5)
    # for i in range(10):
    #     p.apply(func,args=(i,))
    for a in range(10):
        p.map(func,(a,))