'''
数据包里的所有数据都叫保温
报文里不知有你的数据 ip地址  mac地址 端口号
所有的报文都有报头
协议 报头 接受多少个自己
自己定义报头
  在复杂的应用上就会用到
  传输的文件的时候就够复杂
       文件的名字
       文件的大小
       文件的类型
       存储的路径
协议的解析过程我们不需要关心


'''

import socket
import json
import struct


sk=socket.socket()
sk.bind(('127.0.0.1',10080))
sk.listen()
cont,addr=sk.accept()
buffer=1024
head_len=cont.recv(4)
head_len=struct.unpack('i',head_len)[0]
json_head=cont.recv(head_len).decode('utf-8')
head=json.loads(json_head)

file_size=head['filesize']

with open(head['filename'],'wb')as f:
    while file_size:
        if file_size>=buffer:
            content=cont.recv(buffer)
            f.write(content)
            file_size-=buffer
        else:
            cont.recv(file_size)
            f.write(content)
            file_size=0
            break
cont.close()
sk.close()

