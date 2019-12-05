'''


迭代器

   什么是迭代
      迭代是一个重复的过程，
      并且每次重复都是基于上一次的结果而来

    迭代器 ：
            迭代取值的工具。不依靠索引取值
            可迭代的对象执行.__iter__方法得到的返回值就是迭代器对象

    优点：
        提供了一种不依赖索引的取值方式


'''

# lista=[1,2,3]
#索引查询
#循环for 查询

'''
可迭代的对象
已知可被for循环的类型  
         str
          list
          dict
          set
          tuple 
          f=open()
          range()
          enumerate   
          
          可迭代对象加 
             .__iter__ 方法就是一个迭代器 >>>[].__iter__ >>>>通过next就可以从迭代器中一个一个的取值  
           只要含有 __iter__方法的都是可迭代的—————可迭代协议
           
           迭代器协议  -----内部含有__next__和__iter__方法的就是迭代器
          
          

'''
#告诉我传入的数据类型所拥有的所有方法
# print(dir({}))
# print(dir([]))
# print(dir(''))
# print(dir(range(10)))
# rest=set(dir([]))&set(dir([]))&set(dir(''))&set(dir(range(10)))
# print(rest)
# print(dir(int))
# # 双下方法 是内置方法 是c语言写好的 并不止一种方法可以调用
# print([1].__add__([2]))
# print([1]+[2])
#
# lista=[1,2,3,'abc']
# iterators=lista.__iter__()
# #迭代器本身执行.__iter__()方法返回迭代器本身
# # 文件类型本身就是迭代器对象，因为可以直接调用.__next__方法
# print(iterators.__iter__())
# print(iterators.__next__())
#print(iterators.__length_hint__())

#for 循环成为迭代器循环，in后跟的必须是可迭代对象
# for line in lista:  #lista.__iter__()   这里for实际上就执行了下边的while循环
#     print(line)
#
# while True:
#     try:
#         print(iterators.__next__())
#     except StopIteration:
#         break


#py2和py3的range的区别,py2中直接便利后生成列表，py3中直接返回range对象，在调用.__iter__一个一个取值，节省空间
#优点：迭代器更加的节省内存
# items=range(10000000000000000000000000000)
# print(items)


#缺点： 1取值麻烦，只能以一个取，只能往后取，并且是一次行的 无法使用len获取长度
lista=[1,2,3,'abc']
iterators=lista.__iter__()
iterators_01=iter(lista)
print(iterators_01,"\n",iterators)
print(iterators is iterators_01)
# while True:
#     try:
#         print(iterators.__next__())
#     except StopIteration:
#         break
# print("第二次取值》》》》》》》")
# iterators=lista.__iter__()
# while True:
#     try:
#         print(iterators.__next__())
#     except StopIteration:
#         break
# # print(dir(lista))
# print(dir(iterators))
# print(set(dir(iterators))-set(dir(lista)))