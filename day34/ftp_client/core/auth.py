import socket
import json
from core.sock_client import mysocketclient

class auths:
    __instance=None
    def __new__(cls, *args, **kwargs):
        '''
        单例模式  放置在client文件中 循环登录的时候 重复创建链接
        节省内存
        :param args:
        :param kwargs:
        :return:
        '''
        if cls.__instance:
            return cls.__instance
        else:
            obj=object.__new__(cls)
            cls.__instance=obj
            return cls.__instance
    def __init__(self):
        self.username=None
        self.sockck=mysocketclient()
    def login(self):
        username=input('username:')
        pwd=input('pwd')
        if username.strip() and pwd.strip():
            user_data={'username':username,'pwd':pwd,'opertion':'login'}
            print(user_data,type(user_data))
            self.sockck.mysend(user_data)
        login_ret=self.sockck.ck.recv(1024)
        #return login_ret
    def register(self):
        username = input('username:')
        pwd1= input('pwd1')
        pwd2= input('pwd2')
        if username.strip() and pwd1.strip() and pwd1==pwd2:
            user_data = {'username': username, 'pwd': pwd1,'opertion':'register'}
            self.sockck.mysend(user_data)
        register_ret=self.sockck.ck.recv(1024)
        return register_ret


    def logout(self):
        pass