'''
进程间的通信   队列和管道(multiprocess.Queue multiprocess.pipe)
IPC(inter-Process Communication)

队列   先进先出
'''

#队列 put 和 get 可能会阻塞
# from multiprocessing import Queue
# import time
#
# q=Queue(3)
# q.put(1) #往队列里加东西
# q.put(2)
# q.put(3)
# print(q.full()) #判断队列是否为空
# print(q.get())  #从队列里去东西
# print(q.get())
# print(q.get())
# print(q.empty()) #判断队列是否为空
# while True:
#     try:
#         q.get_nowait()
#     except:
#         print('队列已经空了')
#         time.sleep(0.5)
# for i in range(6):
#     q.put(i)

from multiprocessing import Queue,Process
def product(q):
    q.put('yuan')

def consume(q):
    print(q.get())


if __name__ == '__main__':
    q=Queue()
    p1=Process(target=product,args=(q,))
    p1.start()
    p2=Process(target=consume,args=(q,))
    p2.start()
