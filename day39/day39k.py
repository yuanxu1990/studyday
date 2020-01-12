import threading,time

def yuan(n):
    print(n,threading.current_thread())
    print(threading.get_ident())#线程的id
    time.sleep(0.5)

for i in range(10):
    threading.Thread(target=yuan,args=(i,)).start()
print(threading.active_count()) #加上主线程   11个
print(threading.current_thread())  #线程的名字

print(threading.enumerate())#线程对象