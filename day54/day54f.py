#  字符串格式化%和format有什么区别？
# python新版本推荐使用format，python2.6新加入format语法支持


c=(200,250)

command1="坐标%s开炮"%(c,)
command="坐标{}开炮".format(c)
print(command1,command)