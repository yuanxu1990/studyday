import socket
import time
from jinja2 import Template
'''
web框架总结：
    1 web框架的本质：
          socket服务端与浏览器的通信
    2 socket服务端功能划分
          a 负责与浏览器收发消息（socket）
          b 根据用户访问不同的路径执行不同函数
          c 从html读取出内容 并且完成字符串替换
    3 python中web框架的分类
          1 框架自带abc的   tornado
          2 框架自带bc的 使用第三方模块的a django
          3 自带b  使用第三方的a和c    flask
        另外一种：
          Django和其他
          django  大而全  
          flask  轻量级

'''
def f_404(url):
    ret = '<p>not found-->{}</p>'.format(url)
    return bytes(ret, encoding='utf-8')
def nihao(url):
    ret='<p>hello-->{}</p>'.format(url)
    return bytes(ret,encoding='utf-8')

def nimei(url):
    print(url)
    with open('nimei.html','r',encoding='utf-8')as f:
        ret=f.read()
        ret2=ret.replace('oo@zz',str(time.time()))
    return bytes(ret2,encoding='utf-8')

def html01(url):
    print(url)
    with open('html01.html','rb')as f:
        html_msg=f.read()
    return html_msg

def jinja2_01(url):
    print(url)
    with open('jinja2_temp.html','r',encoding='utf-8')as f:
        data=f.read()
    temp_data=Template(data)
    ret=temp_data.render({'name':'hello yuan','hobby_list':['喝茶','抽烟'],'url':url})
    return bytes(ret,encoding='utf-8')

base_url=[('/nihao',nihao),('/nimei',nimei),('/html01',html01),('/jinja2',jinja2_01)]

sk = socket.socket()
sk.bind(('127.0.0.1', 10055))
sk.listen()

while 1:
    conn, addr = sk.accept()
    data = conn.recv(1024)
    # 前后端 使用http格式交互数据，在浏览器直接访问
    print(data)
    data_str=str(data,encoding="utf-8")

    lista=data_str.split('\r\n')
    print('lista',lista[0])
    url=lista[0].split(' ')[1]
    # with open('data','wb')as f:
    #     f.write(data)

    for i in base_url:
        print(i)
        if i[0]==url:
            func=i[1]
            break
        else:
            func=f_404
    conn.send(b'HTTP/1.1 200 OK\r\ncontent-type:text/html; charset=utf-8\r\n\r\n')
    respondata=func(url)
    conn.send(respondata)
    # if url=='/nihao':
    #     responsedata=nihao(url)
    #     conn.send(responsedata)
    # elif url=='/nimei':
    #     responsedata = nimei(url)
    #     conn.send(responsedata)
    # else:
    #     conn.send(b'<p>url 404</p>')
conn.close()

sk.close()
