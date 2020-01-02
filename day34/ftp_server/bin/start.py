'''


1多用户同时登录
2用户登录 加密认证
3上传下载/保证文件一致性
4不同用户家目录不同，且只能访问自己的家目录
5对用户进行磁盘配额 不同用户配额 可以不同
    用户信息
    用户名
    当前用户所在目录
    文件总大小
    硬盘的配额 总配额
6用户登录server后 可在家目录权限下 切换子目录
7查看当前目录下文件 新建文件夹
8删除文件和空文件夹
9充分使用面对对象
10传输过程中实现进度条
11支持断点续传


'''

import os
import sys
import socketserver

sys.path.insert(0,os.path.dirname(os.getcwd()))

from core.sever import ftpserver




if __name__ == '__main__':
    server=socketserver.ThreadingTCPServer(('127.0.0.1',10111),ftpserver)
    server.serve_forever()