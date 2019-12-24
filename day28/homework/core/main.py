'''

主程序   入口程序


'''
import sys
from conf.config import *
from core.Manager import Manager

def login():
    '''
    先到conf.config文件中读取userinfo的文件路径
    登录函数，读取userinfo中的信息对用户名进行判断
    登录成功后，查看这个人的神父，来确定进入那个视图
    :return:
    '''
    user=input('username-->')
    pwd=input('pwd--->')
    with open(userinfo)as f:
        for line in f:
            username,passwd,role=line.strip().split('|')
            if username==user and passwd==pwd:
                print('\033[1;32m登录成功!\033[0m')
                return {'username':user,'role':role}
            else:
                print('\033[1;31m登录失败!/033[0m')


def main():
    '''
    打印欢迎信息
    login：得到返回值  用户名和身份
    打印用户身份对应的功能菜单
    如果用户想要调用任何方法应该通过角色对象调用，跳转到对应对象的方法里
    :return:
    '''
    print('\033[1;42m欢迎你登录选课系统\033[0m')
    ret=login()
    if ret:
        print('sys---modeules',sys.modules[__name__])
        role_class=getattr(sys.modules[__name__],ret['role'])#根据userinfo文件中的最后意向内容反射对应的角色
        obj=role_class(ret['username'])
        for i,j in enumerate(role_class.menu,1):
            print(i,j[0])
        try:
            ret=int(input('请输入操作序号'))
            getattr(obj,role_class.menu[ret-1][1])()
        except:
            print('对不起你输入的内容有误')