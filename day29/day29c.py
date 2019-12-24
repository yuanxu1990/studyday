# s='**hello,world!**'
# ss=s.strip('*')
# print(ss)


# s1='hskakhlkshfkskjakf'
# # l=[]
# # for i in s1:
# #     if i not in l:
# #         l.append(i)
# l2=set([i for i in s1 ])
#
# print(l2)

# s5='123.33sdhf3421.34sdf323.324'
# import re
# ret=re.findall('(\d+.\d+)',s5)
# ret=[float(i) for i in ret]
#
# print(sum(ret))

# d={'k1':'v2','k2':[1,2,3],('k','3'):[1,2,3]}
# #输出字典中value是列表的key
# for a,b in d.items():
#     if type(b)==list:
#         print(a)
#
# #如果字典中的key是一个元组，输入对应value
# for n,m in d.items():
#     if type(n)==tuple:
#         print(m)
# #d[('k','3')]对应的是一个什么数据类型
# print(type(d[('k','3')]))

#四个数字 1,2,3,4 能主城多少个互补相同且不重复的数字的三位数
# count=0
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i==j or i==k or j==k:
#                 continue
#             count+=1
#             print(str(i),str(j),str(k))

# def func():
#     count=0
#     for i in range(1,5):
#         for j in range(1,5):
#             for k in range(1,5):
#                 if i==j or i==k or j==k:
#                     continue
#                 count+=1
#                 yield count,(str(i),str(j),str(k))
#
# for s in func():
#     print(s)


# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# import random
# # 初始化10个不同的对象
# #求最高age的对象的name
# lista=[Person('yuan'+str(i),i) for i in range(1,11)]
# ret=max(lista,key=lambda a:a.age)
# print(ret.name,ret.age)

class pandb:
    def __init__(self,name,hp,gun,sex):
        self.name=name
        self.hp=hp
        self.gun=gun
        self.sex=sex
class police(pandb):
    def pstarck(self,obj):
        if isinstance(obj,police):
            print('police 不能攻击 police')
            return 'obj error'
        else:
            obj.hp-=self.gun-25
            print('匪徒%s被警察%s打掉了%s滴血'%(obj.name,self.name,self.gun-25))

class bad(pandb):
    def bstarck(self,obj):
        if isinstance(obj,bad):
            print('police 不能攻击 police')
            return 'obj error'
        else:
            obj.hp-=self.gun-20
            print('警察%s被匪徒%s打掉了%s滴血'%(obj.name,self.name,self.gun-20))

p1=police('yuan',100,30,'man')
print(p1.__dict__)
p2=police('yuan1',100,25,'man')
print(p1.pstarck(p2))
b1=bad('dan',100,25,'chrild')
b2=bad('dan1',100,25,'chrild')
p1.pstarck(b1)
b2.bstarck(p2)