'''
通过一个信号 来控制多个进程同时执行或阻塞


事件
    一个信号可以使所有的进程都进出入到阻塞状态
    一个时间被创建后 默认是阻塞状态

    是否 和jmeter的定时器很像

set 和 clear
   分别用来修改一个事件的状态 True和False
   is_set 用来查看一个事件的状态
   wait  是依据事件的状态来决定自己是否阻塞
          False是阻塞   True是不阻塞
'''

# from multiprocessing import Event
#
#
# #创建一个事件
# e=Event()
# #查看一个事件的状态，默认被设置成阻塞
# print(e.is_set())
# #将这个时间状态改为True
# e.set()
# print(e.is_set())
# #依据 e.is_set() 的值来决定是否阻塞
# e.wait()
# print(123456)
# #将这个时间的状态改成False
# e.clear()
# print(e.is_set())
# e.wait()
# print(123456)


import time,random
from multiprocessing import Process,Event
def car(e,i):
    if not e.is_set():
        print('car%s在等待'%i)
        e.wait()
    print('car%s通过'%i)


def light(e):
    while True:
        if e.is_set():
            time.sleep(2)
            e.clear()
            print('\033[31m红灯亮了\033[0m')
        else:
            time.sleep(2)
            e.set()
            print('\033[32m绿灯亮了\033[0m')

if __name__ == '__main__':
    e=Event()
    traffic=Process(target=light,args=(e,))
    traffic.start()
    for i in range(10):
        ca=Process(target=car,args=(e,i,))
        ca.start()
        time.sleep(random.random())