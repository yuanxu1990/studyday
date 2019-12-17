'''

异常处理  try  except

         程序一旦发生错误，就会从错误的位置停下来，不在继续执行后边的内容
         使用try 和 except 就能处理异常
             try 是我们需要处理的代码
             except 后面跟一个错误类型，当代码发生错误且错误类型符合的时候，就会执行except中的代码
             except 支持多分支
             Exception 万能异常应该写在最下边可以和单个except配合使用，方便知道哪里出了问题
             try 和 except 可以和else配合使用 在没有异常的时候回执行 else 下的代码
             findall  不管是否发生异常都回执行，就算是在函数中和return相遇 依然回执行
                       #函数里做异常处理，不管是否异常会做一些收尾工作

            Exception 和as 的配合，except Exception as e ---》 print('异常测试',e) 会打印报错信息


'''


# try:
#     #[][4]
#     ret=int(input("number>>>"))
#     print(ret*'*')
# except ValueError:
#     print('value error')
# except IndexError:
#     print('index error')
# else:
#     print('没有异常')
# finally:
#     print('不管代码是否异常都会执行')
#
# try:
#     {}['k']
#     '3'+4
# except KeyError:
#     print('value error')
# except Exception as e:
#     print('异常测试',e)
