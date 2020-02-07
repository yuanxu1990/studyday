
import pymysql
conn=pymysql.connect(host='127.0.0.1',
                     user='root',
                     password='degnity0304',
                     port=3306,database='db5',
                     charset='utf8')
cursor=conn.cursor()

# 存储过程中没有 in out inout参数
# cursor.callproc('p1')
# 若存储过程中  含有 in 关键字 则就表示存储过程需要传值
# 在存储过程后添加元组就可以cursor.callproc('p1',(5,2))
#cursor.callproc('p2',(5,2))
# r1=cursor.fetchall()
# print(r1)


cursor.callproc('p3',(5,2))
r2=cursor.fetchall()
print(r2)


# 存储过程含有out关键字 如果想要拿到返回值   cursor.execute('select @_p3_0,@_p3_1')
#  其中 'select @_p3_0,@_p3_1'为固定写法 select @_存储过程名称_入参索引位置
cursor.execute('select @_p3_0,@_p3_1')
r3=cursor.fetchall()
print(r3)


cursor.close()
conn.close()