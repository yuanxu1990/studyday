'''
命名空间 类和对象分别存在不同的命名空间中

面向对象的三大特性  继承 多态 封装
继承：
     单继承
         父类
         子类（派生类）：派生方法和派生属性
         子类的对象在调用方法和属性，首先用自己的，自己没有的用父类的
     多继承
         一般不会超过三个父类
         如果子类自己有用自己的，如果没有就用离 子类 最近的父类的方法
         抽象和接口类
         经典类和新式类  继承规则不同，深度优先和广度优先
     super 只能在py3中使用
           super是根据mro广度优先顺序找上一个类 不是单纯的找父类

多态：
      多态和鸭子类型
      python天生支持多态
封装：
     私有的
     __名字
     只能在类的内部使用，子类都无法继承

装饰器：

      @property
          将类中的方法伪装成一个静态属性  @name.setter  @name.delter

      @classmethod
          类方法
             当一个方法只是用了类的静态变量时，就给这个方法加上@classmethod装饰器，默认传cls参数
             将一个方法伪装成一个类中的方法，这个方法就直接可以被类调用，不需要依托任何对象
             class goods:
                   __discount=0.8
                   @classmethod
                   def chang_discount(cls):
                       cls.__discount=0.5
             goods.chang_discount()
             把一个方法变成一个类中的方法，这个方法就直接可以被类调用，不需要依托任何对象



      @staticmethod
          静态方法    静态方法 没有默认的参数，就像函数一样
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

'''

class foo(object):
    def __init__(self):
        self.name='yuan'
    @property
    def func(self):
        print(self.age)
    def func(self):
        print('ok')

fo=foo()
fo.age=18
fo.func()