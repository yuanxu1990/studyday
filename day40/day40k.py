'''
定时器
 Timer

'''

from threading import Timer
import time
def func():
    print('时间同步')

while True:
    t=Timer(2,func).start()
    time.sleep(2)