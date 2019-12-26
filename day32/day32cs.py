
'''


struct模块

什么是固定长度的bytes以及原因


'''

import struct

ret=struct.pack('i',4096)# i 代表int 就是即将要把一个数字转换成固定长度的bytes类型 后跟参数长度不能超过6位
print(ret)

num=struct.unpack('i',ret)
print(num[0])

#如果发送数据的时候
#先发送长度 先接受长度