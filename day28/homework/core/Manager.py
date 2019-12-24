'''

首先


'''

from conf.config import *
from core.Teacher import Teatcher
from core.my_pickle import MyPickle
class Manager:
    menu=[
        ('创建讲师账号','createTeacher'),('创建学生账号','createTeacher'),
        ('创建课程', 'createCourse'),('查看课程','createTeacher'),
        ('创建班级', 'createClass'),('查看班级','showClasses'),
        ('创建讲师账号', 'boundClass'),('退出','')

    ]
    def __init__(self,name):
        self.name=name
        self.teacher_pickle_obj=MyPickle(teacher_obj)
    @staticmethod
    def userinfo_handle(content):
        with open(userinfo,'a')as f:
            f.write('\n%s'%content)
