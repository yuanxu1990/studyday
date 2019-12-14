'''


模块的导入
       1  模块名称 不得以数字 中文开头
       2  import一个文件会执行回导入文件的代码
       3  多次import模块 只会执行一次 会先在
          sys.modules中查看是否存在这个模块如果有则不会被重复导入，
          如果没有则依据sys.path路径去寻找模块
          找到了就导入
          然后创建这个模块的命名空间
          把模块中的名字都放到命名空间中
        4  模块别名         import 模块 as 别名

加载顺序：
       1 找到这个模块
       2 创建这个模块的命名空间
       3 把文件中的名字都放到命名空间

导入顺序：
       1 先导内置的
       2 后导扩展的

pycharm会按照当前文件夹的父节点查找如果找不到则飘红，单只要模块存在sys.path中 就没问题 就可以使用

import .. 和 from .. import .. 区别：
          1 import会将文件中所有的名字放入内容
          2 from .. import 变量名------->导入的变量回变成全局变量，
          如果在目前文件中写一个和导入变量名相同变量则会使用本地的，
          导入的变量名则回被覆盖

导入不要使用 from time import *
         和 __all__=[name1,name2]配合使用 只有在列表中的变量名才会被导入
         但如果直接使用import不影响使用


import 模块名
       模块名.变量名   和本文件中的变量名完全不冲突
       模块不会被重复导入   sys.moudles  从哪导入sys.path
       import 模块名 as 别名 ：提高代码的兼容性
       import 模块1，模块2
form .. import ..
       from 模块名 import 变量名
       直接使用变量名就可以 但是本文件中有相同的变量名会将引入的变量覆盖掉
       from 模块名 import 变量名 as 别名
       from 模块名 import 变量名1，变量名2
       from 模块名 import *
             将模块中的所有变量都放到内存中
             如果本文件中有相同的变量名会发生冲突
             和 __all__=[]配合使用，如果存在__all__变量，回导入列表内的变量名字 如果没有导入指定的


'''


# #模块的导入
# import sys
# print(sys.modules.keys())
# print(sys.path)
#
# #导入部分
# from time import sleep
# sleep(1)

#from demo1 import *  和 __all__=[name1,name2]配合使用 只有在列表中的变量名才会被导入但如果直接使用import不影响使用
#pycharm会按照当前文件夹的父节点查找如果找不到则飘红，单只要模块存在sys.path中 就没问题 就可以使用
#当然也可以在模块名前加上父节点名字
# from demo1 import *
# print(num)
# print(moneny)
# #这样导入就可以了
# from day20.demo1 import *
# print(num)



#模块中有一个变量   __name__,当我们直接执行这个模块的时候，__name__的值就等于__main__
#当我们执行其他模块，在其他模块中引用这个模块的时候，这个模块中的__name__='模块的名字'
import demo1