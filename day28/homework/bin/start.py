'''


修改sys.path 把homework 这个路径写到sys.path列表中
所的模块导入，都是基于homework
'''

# import os
# import sys
# #print(os.getcwd())
# print(os.chdir('..'))
# print(os.getcwd())
# print(sys.path)

from os import getcwd,path
from sys import path as sys_path
sys_path.insert(0,path.dirname(getcwd()))

from core import main
if __name__ == '__main__':
    main.main()