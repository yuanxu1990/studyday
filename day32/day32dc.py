#实现一个大文件的上传和下载

import socket
import json
import os
import struct



ck=socket.socket()
ck.connect(('127.0.0.1',10080))
buffer=1024 #这里不能写的过大 如果超过4096容易报错 猜测和读写速度有关


#发送文件
head={'filename':r'02 包的使用.mp4','filesize':None,'filepath':r'E:\toolss'}
file_path=os.path.join(head['filepath'],head['filename'])
file_size=os.path.getsize(os.path.join(file_path))


head['filesize']=file_size
json_head=json.dumps(head)
bytes_head=bytes(json_head,encoding='utf-8')

len_head=len(bytes_head)      #报头的长度
pack_len=struct.pack('i',len_head)  #转成bytes

ck.send(pack_len)
ck.send(bytes_head)
sum=0
with open(file_path,'rb')as f:
    while file_size:
        sum+=1
        if file_size>=buffer:
            file_content=f.read(buffer)
            print(sum)
            ck.send(file_content)
            file_size-=buffer
        else:
            file_content=f.read(file_size)
            ck.send(file_content)
            file_size=0
            break
ck.close()



