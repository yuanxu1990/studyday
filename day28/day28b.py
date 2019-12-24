from collections import namedtuple
import json
card=namedtuple('card',['rank','suit'])


# class franchdeck(object):
#     ranks=[str(n) for n in range(2,11)]+list('JQKA')
#     suits=['红心','方块','梅花','黑桃']
#
#     def __init__(self):
#         self._cards=[card(rank,suit)for rank in franchdeck.ranks for suit in franchdeck.suits]
#
#     def __len__(self):
#         print('it len')
#         return len(self._cards)
#     def __getitem__(self, item):
#         return self._cards[item]
#     def __setitem__(self, key, value):
#         self._cards[key]=value
#     def __str__(self):
#         return json.dumps(self._cards,ensure_ascii=False)
#
#
#
# a=franchdeck()
# # print(a.__dict__)
# # print(a[0])
# from random import choice,shuffle
# print(choice(a))
# shuffle(a)
# print(a[10])
# print(a)
# print(a[5])
# print(a[:5])


#内置函数 内置模块 内置的基础类型   ------》类的内置方法
#len（） __len__
#==      _eq__


#100个名字和性别 年龄不同

class hashs:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def __eq__(self, other):
        print(self,other)
        print('eq2222')
        if self.name==other.name and self.sex==other.sex:
            return True
        else:
            return False
    def __hash__(self):
        print('hash111')
        return hash(self.name+self.sex)

a=hashs('yuan',18,'man')
b=hashs('yuan',25,'man')

#set的实现 依赖对象hash eq方法 先调用hash 拿到hash值 在调用eq
print(set((a,b)))
hs=set((a,b))
print(hs)
