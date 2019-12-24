'''

用户注册
用户 输入用户名
用户 输入密码
明文的密码进行摘要 拿到一个密码的密码
写入文件




# >>> import hashlib
# >>> md5=hashlib.md5()
# >>> md5.update('123'.encode('utf-8'))
# >>> print(md5.hexdigest())
# 202cb962ac59075b964b07152d234b70
# >>> md5.update('123'.encode('utf-8'))
# >>> print(md5.hexdigest())
# 4297f44b13955235245b2497399d7a93
经过测试发现 md5.update  会将每次字符串拼接，我们看下 “123123”的结果如下：

# >>> md5=hashlib.md5()        //重新定义md5
# >>> md5.update('123123'.encode('utf-8'))
# >>> print(md5.hexdigest())
# 4297f44b13955235245b2497399d7a93        //发现123123  和上面的结果一样 就验证了 md5.update 是拼接的效
为了防止这种干扰我们每次都要重新实例化：

每次使用update之前都要重新定义：md5=hashlib.md5()

eg：

import hashlib
f = open('top10.md5.txt','w')
p = open('top10.txt','r')
for i in p:
    md5 = hashlib.md5()
    i=i.strip()    //过滤空白字符
    md5.update(i.encode('utf-8'))
    c=md5.hexdigest()
    c=c+'\n'
    f.write(c)
'''
#用户登录
import hashlib
# # user=input('username')
# # pwd=input('pwd')
# # with open('logintest') as f:
# #     for line in f:
# #
# #         username,password,role=line.split(',')
# #         md5=hashlib.md5()
# #         md5.update(bytes(pwd,encoding='utf-8'))
# #         md5_pwd=md5.hexdigest()
# #         if username==user and md5_pwd==password:
# #             print('login pass')
# # md5=hashlib.md5()
# # md5.update(bytes("xu",encoding='utf-8'))
# # md5_pwd=md5.hexdigest()
# # print(md5_pwd)
#
# #加盐
# md5=hashlib.md5(bytes('x',encoding='utf-8'))
# md5.update(b'xu')
# print(md5.hexdigest())



#每次调用的md5.update() 的时候 会将每次传入update的字节类型拼接 这样方便对整个文件进行摘要算法
#如果想要避免这样的情况 需要重新实例化化md5对象 md5=hashlib.md5() ----》md6=hashlib.md5()
# import hashlib
md5=hashlib.md5()
md5.update('123'.encode('utf-8'))
print(md5.hexdigest())
md5.update('123'.encode('utf-8'))
print(md5.hexdigest())
md6=hashlib.md5()
md6.update('123'.encode('utf-8'))
print(md6.hexdigest())



