'''

logging

     一键控制
     拍错的时候需要打印很多细节来帮拍错
     严重的错误记录下来
     有一些用户行为 有没有错都要记录下来

'''
#basicConfig   简单 能做的事情相对少
#                中文的乱码问题
# import logging
# logging.basicConfig(
#                     level=logging.WARNING,
#                     format='%s(asctime)s%(filename)s[line:%(lineno)d]%(levelname)s%(message)s',
#                     datefmt='%a,%d %b %Y %H:%M:%S',
#                     #删除一下两行 就是不往文件中写 直接在屏幕输出
#                     filename='test.log',
#                     filemode='a'
# )
#
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

# try:
#     int(input('num'))
# except ValueError:
#
#     logging.error('输入的不是数字')




import logging


#实现程序的高度可定制 程序的高度解耦


# logger=logging.getLogger()
# #创建一个handler 用于写入日志文件
# fh=logging.FileHandler('test1.log',encoding='utf-8')
#
# #再创建一个handler 用于输出到控制台
# ch=logging.StreamHandler()
# formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(message)s')
# fh.setLevel(logging.DEBUG)
#
# fh.setFormatter(formatter)
# ch.setFormatter(formatter)
# logger.addHandler(fh)
# logger.addHandler(ch)#logger对象可以添加多个fh和ch对象
#
#
# logger.debug('logger debug message')
# logger.info('logger info message')
# logger.warning('logging warning message')
# logger.error('logger error message')
# logger.critical('logger critical message')


'''
logging  
        有5种级别的日志记录模式
        两种配置方式
                  basicconfig  
                  log对象 高可定制化
'''