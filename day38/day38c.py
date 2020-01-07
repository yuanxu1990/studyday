'''
数据共享Manager

基于消息传递的并发变成是大势所趋

即使是使用线程 推荐做法也是将程序设计为独立的线程集合，通过消息队列交换数据
这样极大地减少了对使用锁定和其他同步手段的需求 还可以扩展到分布式系统中

但是进程间应该尽量避免通信，即便通信，也应该选择进程安全的工具来避免加锁带来的问题

数据不安全的根本 多进程之间抢占资源

'''

from multiprocessing import Manager,Process,Lock

def man_dict(dic,locks):
    locks.acquire()
    dic['count']-=1
    locks.release()
    print('子进程---',dic)

if __name__ == '__main__':
    m=Manager()
    locks=Lock()
    p_list=[]
    dicts=m.dict({'count':100})
    for i in range(50):
        p=Process(target=man_dict,args=(dicts,locks))
        p.start()
        p_list.append(p)
    [a.join() for a in p_list]
    print('主进程---',dicts)


