'''

进程锁

火车票

'''

from multiprocessing import Process
import json
import time


def show(i):
    with open('ticket',encoding='utf-8')as f:
        tick_num=json.load(f)
    print('%s余票:%s'%(i,tick_num['ticket']))

def buy_tick(i):
    with open('ticket', encoding='utf-8')as f:
        tick_num = json.load(f)
        time.sleep(0.1)
    if tick_num['ticket']>0:
        tick_num['ticket']-=1
        print('买到票了%s'%i)
    else:
        print('没有买到票')
    time.sleep(0.1)
    with open('ticket','w')as f1:
        json.dump(tick_num,f1)


if __name__ == '__main__':
    '''
    两个子进程都是异步的
    每个子进程不一定是先后执行的就会造成火车票数据错乱
    
    
    '''
    for i in range(10):
        p=Process(target=show,args=(i,))
        p.start()
    for a in range(10):
        p1=Process(target=buy_tick,args=(a,))
        p1.start()