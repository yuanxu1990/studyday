'''


pymysql   python中的数据库模块
py2中   pymysql  mysqldb
py3中   pymysql

sql注入的问题  例如在username中输入   ‘sss’ or 1=1 -- 所以不要在sql语句上直接进行字符串拼接
pymysql中的 execute(sql,username,pwd)   会自动的做拼接过滤sql注入

'''

import pymysql
username=input('username>>>')
pwd=input('pwd>>>')
conn=pymysql.connect(host='127.0.0.1',user='root',password='degnity0304'
                     ,port=3306,database='db5')


cursor=conn.cursor()

sql='select * from userinfo where username="%s" and password="%s"'%(username,pwd)

cursor.execute(sql)
result=cursor.fetchone()

cursor.close()
conn.close()
print(result)
if result:
    print('login pass')
else:
    print('login filed')