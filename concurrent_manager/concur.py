from multiprocessing import Pool
from threading import Thread,Event
import gevent
import requests
import time
def get_res(url):
    res=requests.get(url)
    print(res.content.decode('utf-8'))

def gevent_res(url):
    global g_lista
    for i in range(500):
        g=gevent.spawn(get_res,url)
        g_lista.append(g)
    if len(g_lista)==500:
        [g1.join() for g1 in g_lista]

def thread_res(url,i,e):
    print(i)
    global thread_lista
    for i in range(20):
        t=Thread(target=gevent_res,args=(url,))
        thread_lista.append(t)
    if len(thread_lista)==100:
       e.set()
       [a.start() for a in thread_lista]




if __name__ == '__main__':
    #thread_lista = []
    g_lista = []
    # p=Pool(5)
    # e=Event()
    # print(e)
    # for i in range(5):
    #     p.apply_async(thread_res,args=('http://www.baidu.com',))
    # time.sleep(2)
    # p.close()
    # p.join()
    # print(len(g_lista))
    start_time=time.time()
    for i in range(50):
        g=gevent.spawn(get_res,'http://www.baidu.com')
        g_lista.append(g)
        print(i,flush=True)
    print(len(g_lista))
    [a.join() for a in g_lista]
    end_time=time.time()-start_time
    print(end_time)