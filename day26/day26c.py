'''

反射

hasattr getattr deattr
'''

class teacher:
    dic={'查看学生信息':'show_student','查看讲师信息':'show_teacher'}
    @classmethod
    def show_student(cls):
        print('show_student')
    @classmethod
    def show_teacher(self):
        print('show_teacher')

    @classmethod
    def func(cls):
        print('sdf')

# ret=getattr(teacher,'dic')    #teacher.dic  类也是对象
# print(ret)
# ret01=getattr(teacher,'func')  #teacher.func()
# ret01()
# if hasattr(teacher,'show_student'):
#     ret02=getattr(teacher,'show_student')
#     print(ret02)
#     ret02()
#
#
# yuan=teacher()
# ret03=getattr(yuan,'show_teacher')
# ret03()
for k in teacher.dic:
    print(k)
key_info=input("pelase select info")
if hasattr(teacher,key_info):
    ret7=getattr(teacher,teacher.dic[key_info])
    ret7()

'''
通过反射
对象名 获取对象属性和普通方法
类名 获取静态属性和类方法和静态方法


普通方法 self
静态犯法 @staticmethod
类方法   @classmethod
属性方法 @property

继承
封装的


'''




# class studen:
#     @classmethod
#     def func00(cls):
#         print('od')
#     def func001(self):
#         print('low')
# studen.func00()
# studen.func001(studen)