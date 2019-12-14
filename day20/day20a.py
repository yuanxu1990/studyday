'''

序列化模块
将原本的字典，列表等内容转化成一个字符串的过程叫做序列化

1 写文件的时候不能直接写成字典
2 网络上传输的时候需要bytes ，字典无法直接转成bytes，只能先转成字符串在转成bytes


从数据类型---》字符串的过程 序列化
从字符串-----》数据类型的过程 反序列化

1 json   *****
          #json  通用的序列化格式  只有很少的一部分数据类型通过json转化成字符串
2 pickle ****
          #pickle  所有的python中的数据类型都可以转化成字符串形式
                 pickle序列化的内容只有python能理解
                  且反序列化依赖python代码
3 shelve ***
          shelve 操作简单，生成序列化句柄
              使用句柄直接操作，非常方便
'''



import json
#可序列化数据类型 数字 字符串 列表 字典 元组（先转成列表在序列化）
#json  dumps序列化方法 loads反序列化方法   在内存中直接更改
#数据结构中用单引号，序列化后回转成双引号，
# 因为json是个单引号的数据类型，json_str='{"k1":"v1"}'需要将数据类型中的单引号转化才能做区分
# dict_json={'k1':'v1'}
# dict_str=json.dumps(dict_json)
# print(type(dict_str),dict_str)
# dic_d=json.loads(dict_str)
# print(type(dic_d),dic_d)


#dump   load   操作文件  dump先序列化字符串 在写到文件中  load先读出来在反序列化
# dict_json01={'k2':'v2'}
# f=open('fff','w',encoding='utf8')
# json.dump(dict_json01,f)

# f1=open('fff','r',encoding='utf8')
# ret=json.load(f1)
# f1.close()
# print(type(ret),ret)


#dump指定参数ensure_aciis=False  可以写中文 否则直接写成bytes类型 但是不影响读取
# dict_json02={'k2':'v2','k3':'大中国'}
# f=open('fff','w',encoding='utf8')
# json.dump(dict_json02,f,ensure_ascii=False)
# f.close()


# 如果插入的时候将多个数据类型放在一行 则回报错
# 解决思路
# 1 将数据用dumps一个一个的字符串后边+/n就做到了换行 然后在写入文件
# 2 然后在用for循环在一行一行的读出来，然后去空格 在load出来
# 3 这样就避开了dump和load
# f1=open('fff','r',encoding='utf8')
# ret=json.load(f1)
# f1.close()
# print(type(ret),ret)


# 方法  dumps dump（序列化，存）  loads（反序列化，读）  load
#pickle不仅可以序列化字典，列表，可以把python中的任意的数据类型序列化
import pickle
#
# dict_pickle={'k1':'v1','k2':'v2','k3':'v3'}
# str_dictp=pickle.dumps(dict_pickle)
# print(str_dictp) #返回的是二进制 所以和json中的dump不同之处就在于返回值类型不同
#
# dict_pickle01=pickle.loads(str_dictp)
# print(dict_pickle01)    #字典
#
# import time
# struct_time=time.localtime(20000000000)
# print(struct_time)
# f=open('pickle_file','wb')
# pickle.dump(struct_time,f)
# f.close()
#
# f1=open('pickle_file','rb')
# struct_time2=pickle.load(f1)
# print(struct_time2.tm_year)


'''
shelve  只提供一个open（）方法，用key来访问，类似字典
       此模块有限制，不支持多个应用同一时间往同一个DB(实际上就是shelve文件)进行写操作。
       如果应用如果值进行读操作，可以让shelve通过只读方式打开DB
       即使是以读的形式打开，也可以直接可以修改 flag=‘r’执行只读 --->f=shelve.open(filename,flag='r')
       
       由于shelve在默认情况下是不会记录 待持久化对象的任何修改的，
       所以我们在shelve.open()时候需要修改默认参数，否则对象的修改不会保存
'''
import shelve
#存数据
# f1=shelve.open('shelve_file')
# #直接对文件句柄操作，就可以存入
# f1['key']={'int':10,'float':45.21,'str':'yuan'}
# print(dict(f1))
# f1.close()
#
#
# #读取数  取出数据的时候也只需要直接用key获取即可，但是如果key不存在则会报错
# f2=shelve.open('shelve_file')
# ret=f2['key']
# f2.close()
# print(ret)


#即使是以读的形式打开，也可以直接可以修改 flag=‘r’执行只读 --->f=shelve.open(filename,flag='r')
# f=shelve.open('shelve_file01',flag='r')
# f['key']=10
# exising=f['key']
# print(exising)
# f['key']=50
# f.close()
#
# f1=shelve.open('shelve_file01',flag='r')
# existing01=f1['key']
# print(existing01)
# f1.close()

# 由于shelve在默认情况下是不会记录
# 待持久化对象的任何修改的，
# 所以我们在shelve.open()
# 时候需要修改默认参数，否则对象的修改不会保存  writeback=True
# f1=shelve.open('shelve_file03')
# f1['k1']={'value':123,'new_value':'one'}
# print(f1['k1'])
# f1['k1']['new_value']='first'
# print(f1['k1'])
# f1.close()

#shelve.open(filename,writeback=True  )
f2=shelve.open('shelev_file04',writeback=True)
f2['k1']={'value':123,'new_value':'one'}
print(f2['k1'])
f2['k1']['new_value']='first'
print(f2['k1'])
f2.close()

