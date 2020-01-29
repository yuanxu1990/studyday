'''
pymysql   python中的数据库模块
py2中   pymysql  mysqldb
py3中   pymysql

sql注入的问题  例如在username中输入   ‘sss’ or 1=1 -- 所以不要在sql语句上直接进行字符串拼接
pymysql中的 execute(sql,username,pwd)   会自动的做拼接过滤sql注入


pymysql的操作：
  1 创建链接
  2 获取游标
  3 执行sql(增删改查)
  4 查询结果
  5 其他


'''

#1 基本操作 创建链接 游标 执行sql 获取查询结果

import pymysql
#
# conn=pymysql.connect(host='127.0.0.1',
#                      user='root',
#                      password='degnity0304',
#                      port=3306,database='db5'
#                      )

# cursor=conn.cursor()

#当然也可以不用在execute内传参，直接在sql上拼接，但是可能会导致sql注入的问题
# sql='select * from userinfo where username=%s and password=%s'
# cursor.execute(sql,['yuan','123456'])
# result=cursor.fetchone()    #仅仅拿第一条数据
# result1=cursor.fetchmany(4) #指定拿几条数据
# result2=cursor.fetchall()   #拿所有的数据
# print(result)
#返回结果默认是一个元组(1, 'yuan', '123456')
#pymysql可以指定返回的数据类型 分别可以在链接和获取游标处修改一个key的值
# conn=pymysql.connect(host='127.0.0.1',
#                      user='root',
#                      password='degnity0304',
#                      port=3306,database='db5'
#                      cursorclass=pymysql.cursors.DictCursor
#                      )
#或则 在获取有标的时候修改
# cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
# sql='select * from userinfo where username=%s and password=%s'
#执行sql   这里也可以写成q=cursor.execute(sql),q是收影响的行数
#当然 execute可以接受args execute(sql,args) args应可迭代类型
# cursor.execute(sql)
# result=cursor.fetchone()
# cursor.close()
# conn.close()
# print(result)

#获取有标的另外一种写法 在with执行完毕后 自动关闭游标
# with conn.cursor()as cursor:
#     sql='select * from info'
#     cursor.execute(sql)
#     result=cursor.fetchone()
# conn.close()





# 移动游标 cursor.scroll(num,mode)
# cursor.scroll(1,mode='relative') #相对当前位置移动
# cursor.scroll(1,mode='absolute') #相对绝对位置移动


#2 pymysql的增删改查 操作 实际上分为2类，select不需要commit 但是insert update delete都需要commit
# insert  单条操作
# conn=pymysql.connect(host='127.0.0.1',
#                      user='root',
#                      password='degnity0304',
#                      port=3306,database='db5')
# cursor=conn.cursor()
# sql = 'insert into userinfo (username,password) values (%s,%s);'
# name = 'aoteman'
# pwd = '123456789'
# cursor.execute(sql, [name, pwd])
# conn.commit()
# cursor.close()
# conn.close()
# insert  多条操作
# conn=pymysql.connect(host='127.0.0.1',
#                      user='root',
#                      password='degnity0304',
#                      port=3306,database='db5')
# cursor=conn.cursor()
# sql = 'insert into userinfo (username,password) values (%s,%s)'
# data = [
#     ('xxoo', '789'),
#     ('ooxx', '456'),
#     ('xoxo', '123')
# ]
# # executemany方法 执行多条
# cursor.executemany(sql, data)
# conn.commit()
# cursor.close()
# conn.close()
#获取最后一条新增数据的自增id，lastrowid  但是如果在使用lastrowid之前没有insert则回报错
#last_id=cursor.lastrowid()


#delete操作
# conn=pymysql.connect(host='127.0.0.1',
#                      user='root',
#                      password='degnity0304',
#                      port=3306,database='db5')
# cursor=conn.cursor()
# sql = "delete from userinfo where username=%s;"
#
# cursor.execute(sql,'yuan')
# conn.commit()
# cursor.close()
# conn.close()

#update操作
# conn=pymysql.connect(host='127.0.0.1',
#                      user='root',
#                      password='degnity0304',
#                      port=3306,database='db5')
# cursor=conn.cursor()
# sql = "update userinfo set pwd=%s where username=%s;"
# cursor.execute(sql,'xu','22222')
# conn.commit()
# cursor.close()
# conn.close()

# 3 pymysql支持回滚  rollback()
# conn=pymysql.connect(host='127.0.0.1',
#                      user='root',
#                      password='degnity0304',
#                      port=3306,database='db5')
# cursor=conn.cursor()
# sql1 = "insert into userinfo (username, pwd) values (%s, %s);"
# sql2 = "insert into hobby (id, hobby) values (%s,%s);"
# user = "xxx"
# pwd = "ooo"
# id = "你妹"  # 表中 id int
# hobby = "散步"
# try:
#     cursor.execute(sql1, [user, pwd])
#     print(sql1)
#     cursor.execute(sql2, [id, hobby])
#     conn.commit()
# except Exception as e:
#     print(str(e))
#     # 出现报错回滚
#     conn.rollback()
# cursor.close()
# conn.close()


