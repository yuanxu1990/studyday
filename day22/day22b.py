'''
d={'k','v'}
print(dict)类
print(d) 对象  对象是通过类生成的

类的定义    ：
             class 类名  或  class 类名（）
             print(类名.属性)
class 内的 __init__方法，在调用类的时候回执行该函数 类的初始化 不能写return  self回自动的返回 self视为类本身 属性绑定

过程：
    类名()首先 会创造出一个对象，创建了一个self变量
    调用init方法，类名括号里的参数会被这里接受
    执行init方法
    返回self  self 就是一个可以存储很多属性的大字典

    查看属性  print(obj.__dict__)
    查看属性值  print(obj.name)
对象能做的事情：
       查看属性
       调用方法
       __dict__对于对象的增删改查可以通过字典的方式来处理
类名能做的事：
       实例化
       调用方法：只不过要自己传递self参数  ———》Persion.func(yu,2)
       __dict__  只能查

'''
# class lei:
#     st='a'
# print(lei.st)

class Persion:
    def __init__(self,*args):
        print(self.__dict__)  #self 就是一个可以存储很多属性的大字典
        self.name=args[0]     #往字典里天机属性的方式发生了一些变化
        self.hp=args[1]
        self.aggr=args[2]
        self.kind=args[3]
        print(self.__dict__)
        print(id(self))
    def func(self,n):   #写在class之内的def被称为方法  必须传self 且在首位
        print('dddd%s %s'%(self.name,n))
    def func01(s):
        print('%sjksjd'%s.name)
    def func02(self):
        print('os')

yu=Persion('蛋蛋',100,1,'男')#这里yu就等于self,yu接受了self返回的值
print(yu)
print(yu.__dict__)
print(id(yu))
print(yu.name)
Persion.func(yu,2)
yu.func(2)
yu.func02()
Persion.func01(yu)

