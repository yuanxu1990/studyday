'''
格式化输出  format
'''
name=input(">>>>>>name")
age=input(">>>>>>>>age")
addr=input(">>>>>>>>addr")
msg="我叫%s，今年%s，来自%s"%(name,age,addr)
print("msg>>>",msg)
msg2="我叫{0}，今年{1}，来自{2}".format(name,age,addr)
print("msg2>>",msg2)


'''
编码    最初的ascii码只有七位，作者为了扩展增加了一位，变成8位
        汉字有9W多，原有的ascii无法满足，所以出现万国码 unicode 四个字节代表一个汉字
        那么unicode 可以使用2**32次方，过于浪费，后来改进成utf8 三个字节代表一个汉字
        中国后来又发明了 gbk 只代表汉字 英文 特殊字符 数字等。两个字节代表一个汉字
'''
'''
utf8 ：最少用一个字节，8位表示一个英文
       欧洲16位 ，2个字节表示一个欧洲字
       亚洲24位，三个字节表示一个中文
       
gbk：   中国国产，只能用同于中文和ascii码中的文字
'''

'''
逻辑运算符 and or 
优先级别  ()> not > and > or 
'''