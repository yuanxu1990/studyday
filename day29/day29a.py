'''
configparser  配置文件


logging      日志文件


'''
#创建配置文件
import configparser
# config=configparser.ConfigParser()
# config['DEFAULT']={
#                    'ServerAliveInterval':'45',
#                    'Compression':'yes',
#                    'CompressionLevel':'9',
#                    'ForwardX11':'yes',
# }
#
# config['bitbucket.org']={'User':'hg'}
#
# config['topsecret.server.com']={'Host Port':'50022','ForwardX11':'no'}
#
#
# with open('example.ini','w')as f:
#     config.write(f)
#





# config=configparser.ConfigParser()
# #--------------查找文件内容 基于字典形式
# # print(config.sections())
# config.read('example.ini')
# print(config.sections())
#
#
# print('bitbucket.org' in config)
# print('bitbucket.org11' in config)
#
# print(config['bitbucket.org']['user'])
#
# #默认节点 不会显示出来 但是不影响拿值
# print(config['DEFAULT']['Compression'])
#
# #注意  如果配置文件中有default节 在循环其他节的时候，也会默认打出default节的值
# # for key in config['bitbucket.org']:
# #     print(key)
#
# #同for循环 找到'bitbucket.org'下所有的键 但是不会打印default节的值
# print(config.options('bitbucket.org'))
#
#
# #找到 'bitbucket.org' 下所有的键值对 返回一个列表套元组的数据类型
# print(config.items('bitbucket.org'))
#
#
# #get方法section下的key对应的value
#
# print(config.get('bitbucket.org','compression'))



#增删
import configparser
config=configparser.ConfigParser()
config.read('example.ini')        #读文件
config.add_section('yuan')        #增加section
config.remove_section('bitbucket.org')          #删除一个section
config.remove_option('topsecret.server.com','forwardx11')#删除一个配置项
config.set('topsecret.server.com','k1','1111')
config.set('yuan','k2','22222')
with open('new2.ini','w')as f:
    config.write(f)#写进文件


