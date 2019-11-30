'''

闭包 ：  嵌套函数，内部函数调用外部函数的变量
'''

#
# def outer():
#     a=1
#     def inner():
#         print(a)
#     print(inner.__closure__)# 只要返回的内存地址以cell开头就证明是闭包
# outer()



'''
若在函数中返回闭包函数的地址，
则闭包函数内使用的外部的变量不会在内存销毁
'''
# def outer():
#      a=1
#      def inner():
#          print(a)
#      return inner
#  inn=outer()
#  inn()


from urllib.request import urlopen

def get_url():
    urla='http://www.jd.com/'
    def gets():
        rest=urlopen(urla).read()
        print(rest)
    return gets

ss=get_url()
ss()
