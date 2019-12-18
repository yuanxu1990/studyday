'''
多继承


'''
#钻石继承   深度和广度  python3中 所有的类都是新式类 广度优先

#当类是经典类时  多继承情况下，回按照深度优先的方式查找  py2 经典类父类或者类没有继承object
#当类是新式类时  多继承情况下  回在按照广度优先方式查找  py3
#
#多继承成中，我们子类的对象调用一个方法，默认是就近原则 找的顺序是什么
#经典类中，深度优先
#新式类中 广度优先
#py2中 新式类和经典类共存，新式类要继承object
#py3中  只有新式类 默认继承object
# 和 mro()方法 只在新式类中存在super()只在py3中存在
#  super() 本质 不是单纯的找父类  而是按照调用位置按照广度优先顺序来的


class A:
    def func(self):
        print('A')
class B(A):
    def func(self):
        print('B')
class C(A):
    def func(self):
        print('C')
class D(B,C):pass
    # def func(self):
    #     print('D')

d=D()
print(D.mro())