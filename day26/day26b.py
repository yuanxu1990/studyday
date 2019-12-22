'''

遗留的内置函数
            property
            classmethod
            staticmethod
'''
#property   内置装饰器函数，只在面向对象中使用
#被property装饰的方法不能传任何参数
# 只是使类中的方法看起来更像是一个属性，
# 在类的外部调用该方法的时候，不用加()调用
from math import pi

# class circle:
#     def __init__(self,r):
#         self.r=r
#     @property
#     def perimeter(self):
#         return 2*pi*self.r
#     @property
#     def area(self):
#         return pow(self.r,2)*pi
#
# c1=circle(6)
# print(c1.perimeter)
# print(c1.area)

# class person:
#     def __init__(self,name,high,weight):
#         self.name=name
#         self.high=high
#         self.weight=weight
#     @property
#     def bmi(self):
#         return self.weight/self.high**2
#     @property
#     def fab_bmi(self):
#         return 22*pow(self.high,2)
#
# yuan=person('袁',1.74,91)
# print(yuan.bmi)
# print(yuan.fab_bmi)

#利用property 修改类的私有属性
#property 可以看成将方法置成了一个类的属性 在外部是不能被更改的
#需要配合 @被property装饰的函数同名.setter 在定义一个新的和被property装饰的方法同名的方法才能完成修改
#所以如果想使用    @被property装饰的函数同名.setter 更改则必须先使用@property
# class edit_name:
#     def __init__(self,name):
#         self.__name=name
#     @property
#     def name1(self):
#         return self.__name+'sb'
#
#     @name1.setter
#     def name1(self,new_name):
#         print('name1 edit')
#         self.__name=new_name
#
# cat=edit_name('dandan')
# print(cat.name1)
# cat.name1='wangyongmei'
# print(cat.name1)


# class goods:
#     discount=0.8
#     def __init__(self,name,price):
#         self.name=name
#         self.__price=price
#     @property
#     def price(self):
#         return self.__price*goods.discount
# app=goods('玉米',6)
# print(app.price)

#属性的删除 修改 查看
# class del_name:
#     def __init__(self,name):
#         self.__name=name
#     @property
#     def name1(self):
#         return self.__name
#     @name1.deleter
#     def name1(self):
#         print('执行了这个方法')
#         del self.__name
#     @name1.setter
#     def name1(self,newname):
#         self.__name=newname
#
# del_oldname=del_name('niu')
# print(del_oldname.name1)
# print(del_oldname.__dict__)
#
# #del 只是触发了类中 @被property装饰的函数同名.deleter 装饰的方法
# del del_oldname.name1
# print(del_oldname.__dict__)
# #print(del_oldname.name1)



'''

method 方法
       staticmethod 静态的方法
       classmethod  类方法 
                    把一个方法变成一个类中的方法，这个方法就直接可以被类调用，不需要依托任何对象
                    当这个方法的操作只设计静态属性的时候，就应该使用classmethod来装饰这个方法

'''
# class goods:
#     __discount=0.8
#     def __init__(self,name,price):
#         self.name=name
#         self.__price=price
#     @property
#     def price(self):
#         return self.__price*goods.__discount
#     @classmethod  #把一个方法变成一个类中的方法，这个方法就直接可以被类调用，不需要依托任何对象
#     def change_discont(cls,newdiscont):
#         cls.__discount=newdiscont
#
# app=goods('玉米',6)
# print(app.price)
# goods.change_discont(0.6)
# print(app.price)


#面向对象编程  staticmethod 方法
class Login:
    def __init__(self,name,password):
        self.name=name
        self.password=password
    def login(self):
        pass
    @staticmethod
    def get_user():
        user=input('usename')
        pwd=input('pwd')
        Login(user,pwd)

Login.get_user()

#在完全面向对象的程序中
#如果一个函数，既和对象没有关系，也和类没有关系，那么就用staticmethod将这个函数变成一个静态方法
#类方法，有一个默认参数cls，代表这个类cls
#静态方法 没有默认的参数，就像函数一样