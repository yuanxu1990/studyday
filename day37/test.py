'''
解决生产者和消费者的问题
    消费者无法感知生产者是否已经真正的结束
    假如 在已经被取空的时候，恰好这时生产者
    正要往队列中加数据
JoinableQueue
      q.task_done()
      q.join()

在消费者这一端
   每次获得一个数据
   处理一个数据
   发送一个记号 标志一个数据被处理成功 q.task_done()
在生产者这一端：
   每次生产一个数据
   且每一次生产的数据都放在队列中
   在队列中刻上一个记号
   当生产者全部生产完毕后
   join信号 已经停止生产数据了
            切要等待之前被刻上记号都消费完了结束阻塞

'''
import time
import random
from multiprocessing import Process,JoinableQueue,Queue

def conmmu(q,name):
    # while True:
    #     food=q.get()
    #     if food=='None':
    #         print('%s取到一个空')
    #         break
    #     print('%s吃到了%s'%(name,food))
    #     time.sleep(random.randint(3,6))
    #     q.task_done()  #count-1
    food1=q.get()
    print('%s吃到了%s' % (name, food1))
    q.task_done()
    food2 = q.get()
    print('%s吃到了%s' % (name, food2))
    q.task_done()
    food3= q.get()
    print('%s吃到了%s' % (name, food3))
    q.task_done()


def prodect(q,name,food):
    for i in range(3):
        time.sleep(random.randint(1,3))
        foods='%s做的第%s个%s'%(name,i,food)
        q.put(foods)
    q.join()  #阻塞 知道一个队列中的所有数据被执行完毕



if __name__ == '__main__':
    q=JoinableQueue()
    p1=Process(target=prodect,args=(q,'yuan','baozi',))

    '''
    其实这里也可以将消费者者设定为守护进程
    '''

    c1=Process(target=conmmu,args=(q,'wang',))
    p1.start()
    c1.start()


