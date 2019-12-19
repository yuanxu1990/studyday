'''
java  面向对象编程
设计模式  书-->设计模式
          --->接口类

接口类：
      python原生不支持

抽象类：
      python原生支持
      将类中的相同的部分抽象出来，更像是一种 类的规范

      raise 主动抛出异常
      抽象类无法被实例化


接口类
     默认多继承
     特点 ：
       1    接口类所有的方法 都必须不能实现（）------java
     假如定义了接口类，且用@abstractclassmethod 装饰了接口类中的函数
     则在子类中，必须要实现或定义和接口类中被@abstractclassmethod装饰的函数
     这样就实现了 类的一种规范
     原则：
        2  使用多个专门的几口，而不使用单一的总结口，即客户端（子类）不应该依赖那些不需要的接口
     接口类  刚好满足接口隔离原则，面向对象开发的思想 规范

抽象类：
     不支持多继承，抽象类中可以有一些代码的实现-----java



'''


# 抽象类和接口类  在py中可以将接口类理解成抽象类
# from abc import abstractclassmethod,ABCMeta
# class Payment(metaclass=ABCMeta):#   元类 默认的元类 type  这里指定元类为ABCmeta 规范一个类
#     @abstractclassmethod
#     def pay(self,money):
#         pass
# # class Payment1:
# #     def pay(self):
# #         raise NotImplemented #没有实现这个方法
# class Wechat(Payment):
#     def pay(self,money):
#         print('已经使用微信支出%s',money)
# class alichat(Payment):
#     def pay(self,money):
#         print('已经使用ali支出%s',money)
# class appchat(Payment):
#     def pay1(self,money):
#         print('已经使用app支出%s',money)
# def pay(pay_obj,money):    #统一支付接口
#     pay_obj.pay(money)
# we=Wechat()
# app=appchat()
# pay(we,199)
# pay(app,300)



'''

接口类的多继承

'''

# from abc import abstractclassmethod,ABCMeta
# class swim_animal(metaclass=ABCMeta):
#     @abstractclassmethod
#     def swim(self):
#         pass
#
# class walk_animal(metaclass=ABCMeta):
#     @abstractclassmethod
#     def walk(self):
#         pass
#
# class fly_animal(metaclass=ABCMeta):
#     @abstractclassmethod
#     def fly(self):
#         pass
#
# class tiger(swim_animal,walk_animal,fly_animal):
#     def swim(self):
#         print('tiger swim')
#     def walk(self):
#         print('tiger swim')
#     def fly(self):
#         print('tiger swim')


'''
抽象类  
     与java 一样，python也有抽象类的概念但是同样需要借助模块实现，
     抽象类是一个特殊的类，特殊之处在于只能被继承，可不能被实例化
     

为什么会有抽象类
  如果说类是从一堆对象中 抽取相同的内容而来，抽象类就是从一堆类中抽取相同的内容而来，内容包括数据属性和函数属性
  比如我们有鸡肉的类，猪肉的类，牛肉的类，从这些类抽取的内容就是肉这个抽象的类，你吃肉时，要么要吃一块具体的鸡肉
  牛肉，猪头，要么吃一个具体的鱼肉， 但是你无法迟到一个叫做肉的东西   
  
  从设计角度去看，如果类是从现实对象抽象而来的，那么抽象类就是基于类抽象而来的  
     
抽象类：规范
一般情况下 单继承 能实现的功能都是一样的，所以在父类中可以有一些简单的基础实现
多继承的情况下 由于功能比较复杂 所以不容易抽象除相同的功能的具体实现在父类中


无论是抽象类还是接口类： 
              都是面向对象的开发规范

python中没有接口类
               python中自带多继承，所以我们直接用class来实现了接口类
java中没有多继承的概念，所有类的继承都是单继承，所以抽象类完美的解决了单继承需求中的规范问题
                通过interface这个概念实现接口类
python中支持抽象类，一般都是单继承 不能实例化且可以实现python代码


'''
import abc #利用abc模块实现抽象类
class all_file(metaclass=abc.ABCMeta):
    all_type='file'
    @abc.abstractclassmethod
    def read(self):#定义抽象方法，无需实现功能，当然也可以实现部分功能
        '子类必须定义读功能'
        print('all_file read')
        pass
    @abc.abstractclassmethod
    def write(self):
        '子类必须定义写功能'
        pass

class txt(all_file):
    def read(self):
        print('txt read')
    def write(self):
        print('txt write')

t1=txt()
t1.read()
t1.write()
print(t1.all_type)
