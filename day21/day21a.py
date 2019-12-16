'''

包 ：
    一大堆模块的集合
    把解决一类问题的模块放在同一个文件夹里---包

    sys.moudles 记录了所有被导入的模块
    sys.path记录了导入模块的时候寻找的所有路径

     import     后边不能 .
     凡是在导入时带点的，点的左边必须是一个包，在导入后在使用的时候则没有这种显示
     点的左边可以是包，模块，函数，类（它们都可以用点的方式调用自己的属性）

'''
# import sys
# print(sys.path)#返回python搜索模块的路径列表
#

# import os

# os.makedirs('glance/api')
# os.makedirs('glance/cmd')
# os.makedirs('glance/db')
# l=[]
# l.append(open('glance/__init__.py','w'))
# l.append(open('glance/api/__init__.py','w'))
# l.append(open('glance/api/policy.py','w'))
# l.append(open('glance/api/versions.py','w'))
# l.append(open('glance/cmd/__init__.py','w'))
# l.append(open('glance/cmd/manage.py','w'))
# l.append(open('glance/db/__init__.py','w'))
# l.append(open('glance/db/models.py','w'))
# map(lambda f:f.close(),l)


# import glance.api.policy as p

# 实际上 p=glance.api.policy
# p.get()

# from glance.api import policy
# policy.get()

# sys.path.insert(0,'C:\\Users\\Administrator\\PycharmProjects\\day\\day21\\glance')
# print(sys.path)
# print(sys.modules)


#__init__ 在被导入的时  回默认执行 __init__.py内的代码



# import glance
# glance.api.policy.get()
# glance.cmd.manage.main()
# glance.db.models.register_models(12)
# import json
# from glance.api import policy
# policy.get()
# print(sys.modules)
# print('glance.api' in sys.modules)
# print(type(sys.modules))
# l=[]
# for i in sys.modules:
#     l.append(i)
# lb=json.dumps(l)
#
# print(re.findall('glance\.api\.policy.*>',lb))

'''
导入模块默认执行模块内代码  
导入包默认执行包内的  __init__.py内的文件


导入顺序  ：
         1     sys.path是python中的模块搜索路径列表，每个路径是列表的一个元素
               会默认搜索路径下所有的目录 列表第一个是当前文件所处的根目录路径
               
               注：  A 当在执行本文件时，python会将本文件的当前路径的父节点
                       放入sys.path中索引位置位0 首先只会在该父节点下寻找包
                       也就是当前文件的同级目录。如果没有在在sys.path的路径中
                       向下寻找一级
                     B import 包的时候包内如果有init文件提供内部路径，直接引用
                       如果没有则需要在import的时候写入全路径，导入模块时存在多级关系的时候
                       最好还是使用from..import..
                       
                     C init文件作用之一就是  init就是所在文件内部所有名字被外界访问的借口
                       导入包的时候默认执行init方法
               
         2     在day21a中导入glance的时候，会在列表第一个元素的目录下寻找，
               找到后回执行glance包内的__init__.py文件中的代码
         3     在glance的__init__.py中导入下边api包就会执行api包内的__init__.py文件
         4     在api的__init__.py中依然还是回调用sys.path中第一个元素的值，也就是包的根节点
               也就是day21，但是在day21下级目录中并没有api包，只有glace包，所以直接在
               api的__init__.py中import policy是会报错的。但是galnce是在包的本目录下的
               所以只能 from glance.api import policy这样才能导入成功
'''

# #相对路径，以上是绝对路径
''' 
相对路径：
        如果在包内的模块内使用相对路径就会报错，
        因为在模块的上层并没有使用所以并没有加载到内存中，
        也就是无法找到上层路径所以包内模块想使用包内其他模块只能使用相对路径
        # 而在包外应用时则没有这样的错误，这是因为在包外引用的时候，
        从包的最外层就开始执行了init文件等于加载到了内存形成了完整的路径
绝对路径：
        使用绝对路径 不管在包内部还是外部 导入了就能用 不能挪动但是直观
        
__all__ =[]在包中的用法
        在包一级（glance）的 __init__ 中from .cmd import *
        在包的次一级(cmd)的 __init__ 中 __all__=[模块1,模块2]
'''

# from glance.api import policy
# policy.get()

# import sys
# print('day21a path',sys.path)
# print('day21a modules',sys.modules)

import glance
glance.api.policy.po()
# def day21a():
#     print('test in api import day21a')