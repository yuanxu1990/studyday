'''
封装   代码的保护 面向对象的思想本身就是一种封装
       只让自己的对象调用自己类中的方法


狭义上的封装-----面向对象的三大特性之一
属性和方法都藏起来


类的私有：
       所有的私有，都是在变量的左边加上双下划线
       1 对象的私有属性
       2 类中的私有方法
       3 类中的静态私有属性
       所有的私有，都不能在类的外部使用


'''

#类的私有属性  只是在代码层面不允许用 对象.属性的方式调用
# class userinfo:
#     __key=123  #私有的静态属性
#     def __init__(self,name,pwd):
#         self.name=name
#         self.__pwd=pwd   #私有属性
#     def get_pwd(self):
#         # 只要在类的内部使用私有属性，就会自动带上  _类名
#         # 注意如果此时在类的外部调用pwd 需要用 _userinfo__pwd
#         # 这一点可以通过在外部定义一个 带下划线的方法来实验例如  yuan._pwd1
#         # 这样在外部依然可以用 yuan._pwd1来调用该方法
#         print('get_pwd--》',self.__dict__)
#         return self.__pwd
#
#     def __user_name(self):
#         #私有的方法  只在内部使用 外部没办法感知
#         print(self.__dict__)
#         print('__user_name')
#     def use(self):
#         print('use',self.__dict__)
#         self.__user_name()
# yuan=userinfo('dandan',123456)
# print(yuan.name)
#
# #print(yuan.__pwd)
# print(yuan.__dict__)
# print(yuan._userinfo__pwd)    #_类名__属性
# yuan._weight=100
# print(yuan._weight)
# print(yuan.use())


#假设父类的私有属性，能被子类调用？？
class foo:
    __y='212'
class son(foo):
    #print(foo.__key)
     pass
#弱项调用必须在外部调用需要以下列方式
# print(son._foo__y)


'''
私有应用场景
         1 隐藏起一个属性，不想让类的外部调用
         2 保护这个属性，不想属性随意被改变
         3 不想被子类继承
'''

