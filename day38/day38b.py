'''
管道  在进程之间传递消息

要特别注意管道端点的正确管理问题，如果是生产者或消费者中都没有
使用管道的某个端点，就应该将它关闭。这也说明了为何在生产者中
关闭了管道的输出端，在消费者中关闭管道的输入端，如果忘记执行这些步骤，
程序可能在消费者中的recv（）操作上挂起，管道是由操作系统进行引用计数的，
必须在所有进程中关闭管道后才能生成EOFERROR异常
因此在生产者中关闭管道不会有任何效果，除非消费者也关闭了相同的管道端点

Pipe数据不安全 本质是通过ipc通讯



数据共享Manager

进程池和回调函数

'''

#管道
# from multiprocessing import Pipe,Process
#
# def func(conn1,conn2):
#     conn2.close()
#     while True:
#         try:
#             msg=conn1.recv()
#             print(msg)
#         except EOFError:
#             conn1.close()
#             break
# if __name__ == '__main__':
#     pipe1,pipe2=Pipe()
#     Process(target=func,args=(pipe1,pipe2,)).start()
#     pipe1.close()
#     for i in range(20):
#         pipe2.send('cdsaf')
#     pipe2.close()


#管道  锁  加锁来控制操作管道的行为，来避免进程之间抢数据
#造成的数据不安全现象

#队列 进程之间数据安全的
#队列= 管道+锁
#管道走的底层实际上文件类型的socket

from multiprocessing import Process,Pipe,Lock
import time
import random

def consumer(produce,consume,name,lock):
    produce.close()
    while True:
        lock.acquire()
        baozi=consume.recv()
        lock.release()
        if baozi:
            print('%s收到包子:%s'%(name,baozi))
        else:
            consume.close()
            break
def producer(produce,consume,n):
    consume.close()
    for i in range(n):
        print(i)
        produce.send(n)
    produce.send(None)
    produce.close()

if __name__ == '__main__':
    produce,consume=Pipe()
    lock=Lock()

    c1=Process(target=consumer,args=(produce,consume,'c1',lock))
    c2 = Process(target=consumer,args=(produce, consume, 'c2', lock))
    p1 = Process(target=producer,args=(produce, consume,5))
    c1.start()
    c2.start()
    p1.start()
    # c1.join()
    # c2.join()
    produce.close()
    consume.close()