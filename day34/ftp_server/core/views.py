from core.userregister import user
from conf.settings import userinfo,pickle_path
import os
import pickle

def login(msg):
    print(msg)
    print('server login')

def register(msg):
    #username pwd
    #创建这个用户的家目录，记录
    #把用户名和密码写进文件，记录用户名
    #记录用户的初始磁盘配额
    #文件大小
    #记录用户当今的目录
    user_obj=user(msg['username'])
    print('$$$$$$')
    print('pickle_path------>', os.path.join(pickle_path, msg['username']))
    with open(os.path.join(pickle_path,msg['username']),'wb')as f:
        pickle.dump(user_obj,f)
    os.mkdir(user_obj.home)
    with open(r'C:\Users\Administrator\PycharmProjects\day\day34\ftp_server\db\userinfo','a',encoding='utf-8')as f1:
        f1.write('%s|%s|%s\n'%(msg['username'],msg['pwd'],pickle_path))
    return True






def upload(filename):
    pass


def download(filename):
    pass
