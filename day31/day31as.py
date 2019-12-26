'''


udp
      udp 的server 不需要进行监听也不需要建立建链接
      在启动服务之后只能被动的等待客户端发送消息过来
      客户端发送消息的同事还会自带地址信息
      消息回复的时候，不仅需要发送消息 还需要把对方的地址填写上
'''

import socket
sh=socket.socket(type=socket.SOCK_DGRAM)    #DGRAM datagram
sh.bind(('127.0.0.1',10010))
msg,addr=sh.recvfrom(1024)
print(msg.decode('utf-8'))
sh.sendto(b'hello',addr)


sh.close()