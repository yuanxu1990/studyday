import pymysql
import time


start_time=time.time()
conn=pymysql.connect(host='49.235.195.86',
                     user='yuanx',password='yuanxu1989',
                     port=3306,
                     database='db8',
                     charset='utf8')
cursor=conn.cursor()

sql='insert into index_test(name,email)values(%s,%s)'

for n in range(3000000):
    names='yuan%s'%(str(n))
    emails='%s@qq.com'%(str(n))
    cursor.execute(sql,(names,emails))
    print(n)
conn.commit()
cursor.close()
conn.close()
end_time=time.time()-start_time
print(end_time)