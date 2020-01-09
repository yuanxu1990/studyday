from multiprocessing import Pool
import time
import os
'''
进程池的异步调用 下边的子进程中的代码是异步执行的
apply_async  真正的异步  如果主进程执行完毕 不会等待子进程结束

'''

def func(n):
    print('start func%s'%n,os.getpid())
    time.sleep(0.5)
    print('end func%s'%n,os.getpid())


if __name__ == '__main__':
    p=Pool(5)
    for i in range(10):
        p.apply_async(func,args=(i,))

    p.close() #结束进程池接受任务
    p.join()  #感知进程池中的任务执行结束
    # apply_async
    # 真正的异步
    # 如果主进程执行完毕
    # 不会等待子进程结束
    #time.sleep(2)