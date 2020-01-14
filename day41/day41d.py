from gevent import monkey;monkey.patch_all()
import time
import gevent
import requests
from urllib.request import urlopen

# url='http://www.baidu.com'
# res1=urlopen(url)
# res2=requests.get(url)
# print(res1.read().decode('utf-8'))#有格式
# print(res2.content.decode('utf-8'))#无格式

def get_url(url):
    res1 = urlopen(url)
    cont=res1.read().decode('utf-8')
    return len(cont)

url_list=[ 'http://www.baidu.com',
           'http://www.sogou.com',
            'http://www.taobao.com',
            'http://www.hao123.com',
            'http://www.cnblogs.com'
          ]
# g_list=[]
# start_time=time.time()
# for a in url_list:
#     g=gevent.spawn(get_url,a)
#     g_list.append(g)
# gevent.joinall(g_list)
# v=[v.value for v in g_list]
# end_time=time.time()-start_time
# print(end_time)
# print(v)
start_time=time.time()
g1=gevent.spawn(get_url,'http://www.baidu.com')
g2=gevent.spawn(get_url,'http://www.sogou.com')
g3=gevent.spawn(get_url,'http://www.hao123.com')
g4=gevent.spawn(get_url,'http://www.taobao.com')
g5=gevent.spawn(get_url,'http://www.cnblogs.com')
gevent.joinall([g1,g2,g3,g4,g5])
end_time=time.time()-start_time
print(end_time)
print(g1.value)
print(g2.value)
print(g3.value)
print(g4.value)
print(g5.value)




