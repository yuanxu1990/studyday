'''
set：无序，不重复，可修改
（把set理解key的集合，更合适，因为set中存在的就是不可变对象）
list：有序，可重复，可修改
tuple：有序，可重复，不可修改

当元组tuple中只有一个元素时，表示为：a = (1, )
重点是元素后面，别忘加了“，”

总结：能用tuple，就不要用list，因为tuple中的数据不可修改，更安全
'''


'''
python2 python3区别  
  1 py2 默认ascii py3默认utf8
  2 py2 中print不需要加括号是一个class  py3 中print3 则需要加 是一个方法
  3 py2 中是xrange()  py3中range()
  4 py2 中raw_input() py3中是input()

'''

'''
=  ==  is
= 是赋值
== 判断是否等于
is 也是比较 比较的是内存地址

'''

# lis1=[1,2,3]
# lis2=lis1#赋值运算都指向一个内存地址  改变一个都会改变所有的值
# print(lis2 is lis1)#判断内存地址是否一致
# lis2.append(4)# lis2改变内存地址中的值 那么lis1中也回改变
# print(lis1)
# lis3=[1,2,3]
# print(id(lis1),id(lis2),id(lis3))

#数字，字符串 小数据小数据池概念 节省内存空间
#int （-5--256）
#str  （长度不能超过20 且不能含有特殊字符）

# a=6
# b=6
# print(id(a),id(b))
# c=3000
# d=3000
# #在pycharm中内存地址是一样的pycharm做了优化 但是在命令行中是不一样的
# print(id(c),id(d))

'''
编码
    ascii 一个字节代表一个字符 一个字节占8位 起始位为0
    unicode 起始是2个字节（16位）代表一个字符 后来改成了32位代表一个中文或字母
    utf-8  3个字节代表一个中文字符  最少1个字节代表一个英文字符 数字等
    gbk    最少一个字节代表一个英文字符 数字等  两个字节代表一个中文



    py3:
       1 str 在内存中是用unicode存储的 内存消耗过大
       2 bytes类型  str在存储和传输的过程中需要转成utf8或则gbk进行传输
       
       对于英文 
         str ：表现形式 s='yuan'
               编码格式 0000111   unicode
          bytes： 变现形式 s=b'yuan' 6位的是utf8 4位的是gbk
                编码格式 01010111   utf8 or gbk 
                
        对于中文
            str ：表现形式 s='中国'
               编码格式 0000111   unicode
          bytes： 变现形式 s=b'\xe4\xb8\xad\xe5\x9b\xbd' 6位的是utf8 4位的是gbk
                编码格式 01010111   utf8 or gbk 
                
'''




'''



s=b'yuan'
s1='xu'.encode(encoding='utf8')
print(type(s1))
print(type(s),id(s))
s3='中国'
print(s3.encode(encoding='utf8'))
print(s3.encode(encoding='gbk'))
s4=b'\xe4\xb8\xad\xe5\x9b\xbd'.decode('utf8')
s5=b'\xd6\xd0\xb9\xfa'.decode('gbk')
print(s4,s5)
'''



#购物车 作业

# 第一次做的
# info=[{'name':'香蕉','price':20},
#       {'name':'桃子','price':30},
#       {'name':'蓝莓','price':30}
#       ]
# print('*******欢迎光临水果店******')
# money=(input('请问你有多少money'))
# flag=True
# buy_car=[]
# while flag:
#     if str(money).isdigit() and int(money)>0:
#             for k,v in enumerate(info):
#                 print('序号{},品种{},价格{}'.format(k,v.get('name'),v.get('price')))
#             selct=input('请输入序列号')
#             money=int(money)
#             if selct.isdigit() and int(selct)<len(info):
#                 selct=int(selct)
#                 if selct==0:
#                     if money>int(info[selct].get('price')):
#                         buy_car.append(info[selct].get('name'))
#                         money=money-info[selct].get('price')
#                         print(buy_car)
#                     else:
#                         print('钱不够')
#                         break
#                 elif selct==1:
#                     if money>info[selct].get('price'):
#                         buy_car.append(info[selct].get('name'))
#                         money = money - info[selct].get('price')
#                         print(buy_car)
#                     else:
#                         print('钱不够')
#                         break
#                 elif selct==2:
#                     if money>info[selct].get('price'):
#                         buy_car.append(info[selct].get('name'))
#                         money = money - info[selct].get('price')
#                         print(buy_car)
#                     else:
#                         print('钱不够')
#                         break
#             elif str(selct).upper()=='Q':
#                 flag=False
#             else:
#                 print("输入有误")

#
# info=[{'name':'香蕉','price':20},
#       {'name':'桃子','price':30},
#       {'name':'蓝莓','price':30}
#       ]
# print('*******欢迎光临水果店******')
# money=(input('请问你有多少money'))
# buy_car={}
# while True:
#       for k,v in enumerate(info):
#           print('序列号{}，商品名称{}，价格{}'.format(k,v.get('name'),v.get('price')))
#       selct=input('请填写序列号退出请填写q')
##注意selct是字符串 即使下边代码转成int 只要没有重新赋值 就还是字符串 因为字符串是不可更改数据类型
## 因此可以直接写成 if str(selct).isdigit() and int(selct)<len(info):
##                        selct=int(selct)减少下边的代码量和转换次数 提高效率
#       if selct.isdigit() and int(selct)<len(info):
#           num=input("请输入数量")
#           if num.isdigit():
#               if int(money)>int(info[int(selct)]['price'])*int(num):
#                   print('num>>>',type(num))
#                   if info[int(selct)].get('name') in buy_car:
#                       money=int(money)-info[int(selct)]['price']*int(num)
#                       buy_car['price']=int(num)+int(buy_car['name'])
#                       print('购物车中有\t{},\n数\t{},\n剩余money\t{}'.format(buy_car['name'],buy_car['price'],money))
#
#                   else:
#                       money = int(money) - int(info[int(selct)]['price']) * int(num)
#                       buy_car['name'] = info[int(selct)].get('name')
#                       buy_car['price']=int(num)
#                       print('购物车中有\t{},\n数量\t{},\n剩余money\t{}'.format(buy_car['name'],buy_car['price'],money))
#               else:
#                   print("钱不够")
#                   break
#
#           else:
#               print("数量输入有误")
#
#       elif str(selct).upper()=='Q':
#            break
#       else:
#           print("序列号输入有误")



s='12345'
print(type(s))
d=int(s)
print(type(s))
print(type(d))
print(id(s),id(int(s)),id(d))

















