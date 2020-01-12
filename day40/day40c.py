'''

死锁
科学家吃面 死锁问题 三个人吃面，一碗面一个叉子，a拿走了面，b拿走了叉子
，造成僵持

互斥锁 和 递归锁
互斥锁 Lock 用来决绝数据安全问题
递归锁 用来解决死锁问题  原理 通俗的将 是将所有钥匙放入钥匙串，在拿的时候，会将所有钥匙都拿走，但是还的时候要都换回来
'''

from threading import Lock,Thread,RLock
import time


# noodle_lock=Lock()
# fork_lock=Lock()
# def eat1(name):
#     noodle_lock.acquire()
#     print('%s拿到面条'%name)
#     fork_lock.acquire()
#     print('%s拿到叉子' % name)
#     print('%s吃面'%name)
#     fork_lock.release()
#     noodle_lock.release()
#
# def eat2(name):
#     fork_lock.acquire()
#     print('%s拿到叉子' % name)
#     time.sleep(1)
#     noodle_lock.acquire()
#     print('%s拿到面条' % name)
#     print('%s吃面'%name)
#     noodle_lock.release()
#     fork_lock.release()
#
# Thread(target=eat1,args=('yuan0',)).start()
# Thread(target=eat2, args=('yuan1' ,)).start()
# Thread(target=eat1,args=('yuan2',)).start()
# Thread(target=eat2, args=('yuan3' ,)).start()

'''
递归锁  一串钥匙  同时拿到2把钥匙，因为这2把钥匙都在一个钥匙串上  用来解决死锁问题
'''
# fork_lock=noodle_lock=RLock()
#
# def eat1(name):
#     noodle_lock.acquire()
#     print('%s拿到面条'%name)
#     fork_lock.acquire()
#     print('%s拿到叉子' % name)
#     print('%s吃面'%name)
#     fork_lock.release()
#     noodle_lock.release()
#
# def eat2(name):
#     fork_lock.acquire()
#     print('%s拿到叉子' % name)
#     time.sleep(1)
#     noodle_lock.acquire()
#     print('%s拿到面条' % name)
#     print('%s吃面'%name)
#     noodle_lock.release()
#     fork_lock.release()
#
# Thread(target=eat1,args=('yuan0',)).start()
# Thread(target=eat2, args=('yuan1' ,)).start()
# Thread(target=eat1,args=('yuan2',)).start()
# Thread(target=eat2, args=('yuan3' ,)).start()


fork_lock=RLock()
#
def eat1(name):
    fork_lock.acquire()
    print('%s拿到面条'%name)
    fork_lock.acquire()
    print('%s拿到叉子' % name)
    print('%s吃面'%name)
    fork_lock.release()
    fork_lock.release()

def eat2(name):
    fork_lock.acquire()
    print('%s拿到叉子' % name)
    time.sleep(1)
    fork_lock.acquire()
    print('%s拿到面条' % name)
    print('%s吃面'%name)
    fork_lock.release()
    fork_lock.release()

Thread(target=eat1,args=('yuan0',)).start()
Thread(target=eat2, args=('yuan1' ,)).start()
Thread(target=eat1,args=('yuan2',)).start()
Thread(target=eat2, args=('yuan3' ,)).start()

