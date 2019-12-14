'''

os 模块
    和操作系统打交道


'''


import os

# #getcwd 返回当前工作目录 即当前python脚本工作的目录路径
# print(os.getcwd())
#chdir 切换目录 和shell中的cd类似
# os.chdir(r'C:\Users\Administrator\PycharmProjects')
# print(os.getcwd())


#返回当前目录(.)
# print(os.curdir)
#获取当前目录的父目录字符串名(..)
# print(os.pardir)
#也可以使用chdir 相当于cd ..  返回父目录
# os.chdir('..')
# print(os.getcwd())

#创建  makedirs 生成多层递归目录 即dirname1是dirname2的父目录
# os.makedirs('dirname1/dirname2')
#删除  removedirs   若目录为空 则删除   并递归到上一级目录 如若也为空 则删除  以此类推
# os.removedirs('dirname1')

# 创建  mkdir  生成单级目录  mkdir dirname
# os.mkdir('dirname3')

# 删除 rmdir    删除单级空目录 若目录不为空则无法删除 报错 rmdir dirname
# os.rmdir('dirname3')

# #列出指定目录下的所有文件和子目录，包括隐藏文件，并且以列表的形式打印出来
# print(os.listdir(r'C:\Users\Administrator\PycharmProjects\day'))
#
# #删除一个文件 remove
# os.remove('dirname3\方法')


#重命名一个文件/目录  该当前目录下的文件或则子目录
# os.rename('oldname','newname')

#获取文件/目录信息
# print(os.getcwd())
# print(os.stat('day19d.py'))
'''
stat 结构:

st_mode: inode 保护模式
st_ino: inode 节点号。
st_dev: inode 驻留的设备。
st_nlink: inode 的链接数。
st_uid: 所有者的用户ID。
st_gid: 所有者的组ID。
st_size: 普通文件以字节为单位的大小；包含等待某些特殊文件的数据。
st_atime: 上次访问的时间。
st_mtime: 最后一次修改的时间。
st_ctime: 由操作系统报告的"ctime"。在某些系统上（如Unix）是最新的元数据更改的时间，在其它系统上（如Windows）是创建时间（详细信息参见平台的文档）。
'''

#获取当前操作系统的目录分隔符 Win \   linux /  python代码跨平台用的
# print(os.sep)
#
# #获取输出当前平台使用的行终止符   Win下位'\t\n'   linux下为‘\n’
# print(123)
# print(os.linesep)
# print(456)


# #输出用于分割文件路径字符串   win---> ;   linux--->:
# print(os.pathsep)
#
# #输出字符串只是当前使用平台 win--->'nt';   linux----->'posix'
# print(os.name)

#运行shell命令 直接显示  linux 是对应shell命令    win是对应dos命令
#system 和 popen区别   前者没有返回值 而后者有
# # print(os.system('dir'))
# ret=os.popen('dir').read()
# print(ret)
#
# #获取环境变量
# print(os.environ)


#os.path
#返回path规范化的绝对路径
# print(os.path.abspath(os.getcwd()))
# #将path分割成目录和文件名元组返回
# print(os.path.split(os.getcwd()))
#
# #返回path的目录,其实就是os.path.split(path)的第一个元素
# print(os.path.dirname(os.getcwd()))
#
# #返回path最后的文件名，如果path以/或\结尾，那么就会返回空值
# #其实就是os.path.split(path)中的第二个值
# print(os.path.basename(os.getcwd()))
#
# #判断路径是否存在  如果path存在则返回True  否则False
# print(os.path.exists(os.getcwd()))

#如果path是绝对路径 返回True
# print(os.path.isabs(os.getcwd()))
#
# #如果path是一个存在的文件，返回True 否则False
# print(os.path.isfile(r'C:/Users/Administrator/PycharmProjects/day/day19/day19d.py'))
#
# #如果path是一个存在的目录 则返回True 否则False
# print(os.path.isdir('C:/Users/Administrator/PycharmProjects/day/day19'))
#
# #将多个路径组合返回  第一个绝对路径之前的参数将被忽略
# print(os.path.join('C:/Users/','Administrator/PycharmProjects/','day'))

#返回path所指向的文件或目录的最后访问时间  返回时间戳
# print(os.path.getatime(os.getcwd()))
# #返回path所指向的文件或目录的最后修改时间   返回时间戳
# print(os.path.getmtime(os.getcwd()))
#
# #返回path的大小  文件夹最大4096
# print(os.path.getsize(os.getcwd()))



import sys

'''
和python解释器交互的一个接口
'''
#命令行参数list  第一个元素是程序本身路径  执行一个脚本需要先传一些参数

# 1 需要在终端 运行文件时 把参数传入  格式  python 文件名 参数1 参数2
#  2 传入的参数1 参数2需要在文件中已经做了判断 才能用
# 验证权限使用 在命令行执行文件需要权限
ret01=sys.argv
print(ret01)
name=ret01[1]
pwd=ret01[2]
if name=='alex' and pwd=='yuan':
    print('login pass')
else:
    print('login faile')
    sys.exit()
print('可以使用')
#返回操作系统平台名称
# print(sys.platform)
# #退出程序exit(n)    正常退出时exit(0) 错误退出sys.exit(1)
# #整个程序退出  等于退出python解释器，如果exit（1） 则为错误退出发送给系统处理
#
# #获取python的解释器版本
# print(sys.version)
#
#
# #搜索模块的搜索路径 初始化时使用python
# # 顺序 本身所处的目录找----->到上一级搜-------->python解释器中搜索
# print(sys.path)
