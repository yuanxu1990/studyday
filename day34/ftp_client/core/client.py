import socket
from core.auth import auths

def main():
    auth_obj=None
    start_l=[('登录','login'),('注册','register',),('退出','logout',)]
    for index,item in enumerate(start_l):
        print(index,item[0])
    while True:
        try:
            num=int(input('>>>'))
            str_func=start_l[num][1]

        except:
            print('输入的序号有误')
        print(1)
        if hasattr(auths,str_func):   #登录和退出
            auth_obj=auths()
            func=getattr(auth_obj,str_func)
            print(func)
            ret=func()
            if ret:
                return ret
            elif auth_obj:
                auth_obj.sockck.ck.close()
                exit()
            else:
                exit()

