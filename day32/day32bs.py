'''
黏包 出现的问题
  1 连续send两个小数据     tcp的算法 当两个数据比较小且时间间隔很小 那么就回一块发过去
  2 两个recv 第一个recv特别小    接受端缓存区 recv接受长度小
根本问题
   接受端不知道到底要知道接受多大的数据


解决方案
   首先发送一下这个数据有多大
   在按照数据的长度接受数据

# 好处
         确定了我到底要接受多大的数据
         要在文件中配置一个配置项，就是每次recv的大小  一般不超过4096  buffer=4096
         当我们要发送大数据的时候，要明确的告诉接收方要发送多大的数据，以便接收方能准确的接受到所有数据
         多用在文件传输的过程当中
             大文件的传输 一定是按照字节读  每一次读固定的字节
             传输的过程中，一边读一边传，接受端一边收一边写
             send这个大文件前先计算长度例如35672字节，  send（4096） 35672-4096-4096---》0
            recv这个大文件  recv 35672 recv（2048）  35672-2048-2048---》0
# 坏处
         多了一次交互 网络延迟

send sendto 在超过一定范围的时候 都会报错
程序的内存管理
'''
import socket
sk=socket.socket()
sk.bind(('127.0.0.1',10070))
sk.listen()
content,addr=sk.accept()
while True:
    cmd=input('>>>')
    if cmd=='q':
        content.send(b'q')
        break
    content.send(cmd.encode('utf-8'))
    num=content.recv(1024)
    print(type(num), num)
    content.send(b'ok')

    res=content.recv(int(num))
    print(res.decode('gbk'))
content.close()
sk.close()