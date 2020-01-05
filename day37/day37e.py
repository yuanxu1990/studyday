'''

生产者和消费则模型


买包子               包子笼          买包子
生产数据快-----------容器-----------处理数据慢
'''

from multiprocessing import Process,Queue
import time,random
def product(name,food,q):
    for i in range(10):
        foods='%s生产了%s%s'%(name,food,i)
        print(foods)
        q.put(foods)
        time.sleep(2)

def commu(q,name):
    '''
    注意 队列的进程安全 即一个队列的数据同时只能被一个进程取走
    主进程有2个消费者的子进程，所以如果只在主进程put一个None
    只有一个消费者进程能去到None，所以只能结束一个
    消费者子进程 而另外一个消费者子进程取不到值
    就进入阻塞状态

    :param q:
    :param name:
    :return:
    '''
    while True:
        food=q.get()
        if food==None:
            print('已经取空')
            break
        print('\033[31m{}吃了{}\033[0m'.format(name,food))
        time.sleep(1.3)
if __name__ == '__main__':
    q=  Queue()
    p1=Process(target=product,args=('yuan','baozi',q,))
    p1.start()
    p2 = Process(target=product, args=('xu', 'hulatang', q,))
    p2.start()
    c1=Process(target=commu,args=(q,'dandan',))
    c1.start()
    c2= Process(target=commu, args=(q, 'wangyongmei',))
    c2.start()
    p1.join()
    p2.join()
    # #注意 队列的进程安全 即一个队列的数据同时只能被一个进程取走
    # 主进程有2个消费者的子进程，所以如果只在主进程put一个None
    # 只有一个消费者进程能去到None，所以只能结束一个
    # 消费者子进程 而另外一个消费者子进程取不到值
    # 就进入阻塞状态
    q.put(None)
    q.put(None)