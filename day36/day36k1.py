'''
进程锁

牺牲了效率 但是保证了数据的安全



'''

from multiprocessing import Process
from multiprocessing import Lock
import json
import time

def show(i):
    with open('ticket') as f:
        json_msg=json.load(f)
        print('%s余票:%s' % (i,json_msg['ticket']))

def buy_ticket(i,locks):
    locks.acquire()  #拿钥匙
    with open('ticket') as f:
        json_msg=json.load(f)
    if json_msg['ticket']>0:
        json_msg['ticket']-=1
        print('%s买到票了'%i)
    else:
        print('没有买到')
    time.sleep(0.1)
    with open('ticket','w')as f1:
        json.dump(json_msg,f1)
    locks.release()  #还钥匙
if __name__ == '__main__':
    for i in range(10):
        p1=Process(target=show,args=(i,))
        p1.start()
    locks=Lock()  #生成锁对象
    for a in range(10):
        p2=Process(target=buy_ticket,args=(a,locks))
        p2.start()

'''
首先生成锁的对象
locks=Lock()
当成参数传入所有执行的函数内 
p2=Process(target=buy_ticket,args=(a,locks))
拿钥匙
locks.acquire()
还钥匙
locks.release()

'''
