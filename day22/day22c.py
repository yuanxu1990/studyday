'''

非常明显的处理一类事物，这些事物都具有相似的属性和功能
当有几个函数，需要反反复复传入相同的参数的时候，就可以考虑面向对象
这些参数都是对象的属性
'''




# class dog:
#     def __init__(self,name,blood,aggr,kind):
#         self.name=name
#         self.blood=blood
#         self.aggr=aggr
#         self.kind=kind
#     def bite(self,perison):
#         perison.blood-=self.aggr
#         print('%s被咬了，掉了%s的血'%(perison.name,self.aggr))
#
# class perison:
#     def __init__(self,name,blood,attack,kind):
#         self.name=name
#         self.blood=blood
#         self.attack=attack
#         self.kind=kind
#     def attack01(self,dog):
#         print(dog.__dict__)
#         dog.blood-=self.attack
#         print('%s被打了了，掉了%s的血' % (dog.name,self.attack))
#
# dog1=dog('二哈',1000,20,'犯傻')
# p1=perison('元宝',998,100,'du')
# dog1.bite(p1)
# p1.attack01(dog1)
# from math import pi
# class circle:
#     def __init__(self,r):
#         self.r=r
#     def girth(self):
#         return 2*pi*self.r
#     def areas(self):
#         return pi*pow(self.r,2)
#
#
# girth01=circle(4)
# girths=girth01.girth()
# print(girths)
# area01=circle(3)
# areass=area01.areas()
# print(areass)


class rectangle:
    '''
    矩形面积和周长
    '''
    def __init__(self,n):
        self.n=n
    def areas(self):
        return self.n*self.n
    def girth(self):
        return 4*self.n


s=rectangle(3)
print(s.areas())
print(s.girth())

