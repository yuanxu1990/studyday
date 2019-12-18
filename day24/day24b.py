'''
继承
     继承是一种创建新类的方式，在python中，新建的类可以继承一个或多个父类，
     父类又可称为基类或超类，新建的类称为派生类或子类
     父类必须在子类之前
     单继承和多继承
     一个父类可以被多个子类继承 子类之间没有关系
     一个子类可以继承多个父类，只在python有
     .
     在python3中任何一个没有父类的类，都是继承object类，都是object的子类
     这种类称为新式类

     象即抽取类似或者说比较像的部分。

            抽象分成两个层次：
            1.将奥巴马和梅西这俩对象比较像的部分抽取成类；
            2.将人，猪，狗这三个类比较像的部分抽取成父类。
            抽象最主要的作用是划分类别（可以隔离关注点，降低复杂度）


    通过继承的方式新建类B，让B继承A，B会‘遗传’A的所有属性(数据属性和函数属性)，实现代码重用


'''

# class A(object):pass
# class B:pass
# class A_son(A,B):pass
# class AB_son(A):pass
#
# print(A_son.__bases__)
# print(AB_son.__bases__)
# print(A.__bases__)


# class animal:
#     def __init__(self,name,aggr,hp):
#         self.name=name
#         self.aggr=aggr
#         self.hp=hp
#
# class dog(animal):
#     def bite(self,person):
#         person.hp-=self.aggr
#         print(person.name,self.aggr)
#
# class person(animal):
#     def attack(self,dog):
#         dog.hp-=self.aggr
#         print(dog.name,self.aggr)
#
# jin=dog('二哈',10,100)
# dan=person('蛋蛋',5,100)
# print(jin.name,dan.name)
# print(jin.bite(dan))



#狗类   吃 喝 游泳
#鸟     吃 喝 飞


# 派生属性

'''
父类中没有的属性，在子类中出现 叫做派生属性
父类中没有的方法，在子类中出现 叫做派生方法
只要是子类的对象调用，子类中有的名字一定用子类的，子类中没有才找父类，如果父类（包含object）中没有报错
如果父类和子类都有 用子类的
如果还想用父类的，单独调用父类的
       父类名.方法名  需要自己传self参数
       super().方法名  不需要自己传self
平时的代码中使用单继承     较少了代码的重复
继承  表达的是一种子类是父类的关系
组合  表达是一种类和类之间有的关系

'''

# 派生
# class animal:
#     def __init__(self,name,aggr,hp):
#         self.name=name
#         self.aggr=aggr
#         self.hp=hp
#
#     def eat(self):
#         self.hp+=100
# class dog(animal):
#     def __init__(self,name,aggr,hp,kind):
#         animal.__init__(self,name,aggr,hp)# 这里的self 是dog的self
#         self.kind=kind                         #派生属性  在父类的基础之上又派生了新的属性
#     def bite(self,person):                     #派生方法  在父类的基础上有派生了新的方法
#         person.hp-=self.aggr
#
#     def eat(self):
#         """
#         如果迹象实现新的功能也想使用父类原本的功能，还需要在子类中在掉用父类
#         :return:
#         """
#         animal.eat(self)# 这里的self是dog  作为参数传给了animal.eat
#         self.teeth = 2
# class person(animal):
#     def __init__(self,name,aggr,hp,sex):
#         animal.__init__(self,name,aggr,hp)
#         self.money=0
#         self.sex=sex
#
#     def attack(self,dog):
#         dog.hp-=self.aggr
#
#     def get_weson(self,weson):
#         pass
#
# jin=dog('二哈',100,500,'哈士奇')
# jin.eat()
# print(jin.hp)
# dan=person('dandan',20,100,'baobao')
# dan.eat()
# print(dan.hp)
# jin.bite(dan)
# print(dan.hp)

'''
super()  只在新式类中才有  python3中所有的类都是新式类
'''
class animal:
    def __init__(self,name,aggr,hp):
        self.name=name
        self.aggr=aggr
        self.hp=hp

    def eat(self):
        self.hp+=100
        print('吃药回血')

class dog(animal):
    def __init__(self,name,aggr,hp,kind):
        #super(dog,self).__init__(name,aggr,hp)  supper内参数可以不传
        super().__init__(name, aggr, hp)
        self.kind=kind
    def eat(self):
        print('dog eating')


jin=dog('二哈',200,100,'哈士奇')
print(jin.name)
jin.eat()
super(dog,jin).eat()   #如果是在类外 使用supper(类名，实例化名).方法()   就会执行类中的方法