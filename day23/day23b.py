'''


面向对象的三大特性：  继承  多态 封装

类的组合：一个对象的属性值是另外一个类的对象
          w=weapon('粪叉子',100,3,200)
          yuanbao.get_weapon(w)    通过self  将武器对象绑定成自己的属性值
          yuanbao.weapon.hand18(jin)



'''
# class dog:
#     def __init__(self,name,aggr,hp,kind):
#         self.name=name
#         self.aggr=aggr
#         self.hp=hp
#         self.kind=kind
#     def bite(self,person):
#         person.hp-=self.aggr
#         print('%s被狗咬了，掉了%s滴血'%(person.name,self.aggr))
#
# class person:
#     def __init__(self,name,aggr,hp,sex):
#         self.name=name
#         self.aggr=aggr
#         self.hp=hp
#         self.sex=sex
#         self.money=0
#     def attack(self,dog):
#         dog.hp-=self.aggr
#         print('%s被人打了，掉了%s滴血'%(dog.name,self.aggr))
#     def get_weapon(self,weapon):
#         if self.money>weapon.price:
#             self.money-=weapon.price
#             self.aggr+=weapon.statck
#             self.weapon=weapon
#         else:
#             print('钱不够')
#
# class weapon:
#     def __init__(self,name,statck,lasting,price):
#         self.name=name
#         self.statck=statck
#         self.lasting=lasting
#         self.price=price
#     def hand18(self,person):
#         if self.lasting>0:
#             person.hp-=self.statck*2
#             self.lasting-=1
#
#
#
# yuanbao=person('蛋蛋',2,100,'未知')
#
# jin=dog('二哈',100,500,'teddy')
# w=weapon('粪叉子',100,3,200)
# #充钱
# yuanbao.money=1000
# print(yuanbao.__dict__)
# #装备打狗棒
# yuanbao.get_weapon(w)
# #打狗
# yuanbao.attack(jin)
# print(jin.hp)
#
# #使用打狗棒大招
# yuanbao.weapon.hand18(jin)
# print(jin.hp)


'''

类的组合  ：
           一个对象的属性是另一类的对象
           实际上在A类中将B类的实例化赋值给变量S，然后通过调用的方式使用B中的属性 AA=A.S.func
圆环是由两个圆组成的，圆环的面积是外面圆的面积减去内部圆的面积。圆环的周长是内部圆的周长加上外部圆的周长。
这个时候，我们就首先实现一个圆形类，计算一个圆的周长和面积。然后在"环形类"中组合圆形的实例作为自己的属性来用
'''


# from math import pi
#
# class roundness:
#     def __init__(self,r):
#         self.r=r
#     def permiter(self):
#         return pi*self.r*2
#     def areas(self):
#         return pi*pow(self.r,2)
#
#
# class annulus:
#     def __init__(self,outside_r,inside_r):
#         self.outs=roundness(outside_r)
#         self.inside=roundness(inside_r)
#
#
#     def annu_per(self):
#         return self.outs.permiter()+self.inside.permiter()
#     def annu_areas(self):
#         return abs(self.outs.areas()-self.inside.permiter())
#
# ring=annulus(30,20)
# print(ring.annu_areas())
# print(ring.annu_per())

class bir:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
class teacher:
    def __init__(self,name,age,sex,b):
        self.name=name
        self.age=age
        self.sex=sex
        self.b=b
birs=bir(2018,12,8)
t1=teacher('yu',18,'man',birs)
print(t1.name)
print(t1.b.year)