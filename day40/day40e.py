'''
事件
事件创建的时候
    默认为False状态
    wait（）阻塞

    True
    wait（）非阻塞


clear  设置状态为False

set  设置状态为True
'''
from threading import Thread,Event
import time
import random

def light(e):
    while True:
        if e.is_set():
            print('绿灯亮')
            e.clear()
            time.sleep(3)
        else:
            print('红灯亮')
            time.sleep(3)
            e.set()
def car(i,e):
    # if not e.is_set():
    #     print('car%s 等红灯'%i)
    #     e.wait()
    # print('car%s 通过' % i)
    if e.is_set():
        print('car %s 通过'%i)
    print('car %s 等待'%i)
    e.wait()
    print('car %s 通过'%i)


if __name__ == '__main__':
    e=Event()
    Thread(target=light,args=(e,)).start()
    for i in range(10):
        t1=Thread(target=car,args=(i,e))
        t1.start()
        time.sleep(random.random())
