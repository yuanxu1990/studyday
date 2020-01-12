'''

信号量  Semaphore

'''

import time
from threading import Semaphore,Thread

def func(sema,a,b):
    sema.acquire()
    time.sleep(1)
    print(a,b,a+b)
    sema.release()

sem=Semaphore(4)
for i in range(10):
    t=Thread(target=func,args=(sem,i,i+5))
    t.start()