'''
   模块
       re模块
       正则表达式------字符串匹配
           正则表达式本身也和python没有什么关系 就是匹配字符串内容的一种规则
           官方定义
              正则表达式是对字符串操作的一种逻辑公式，
              就是用事先定义好的一些特定字符，及这些特定字符的组合
              ，组成一个 ‘规则字符串’，这个‘规则字符串’用来表达对字符串一种过滤逻辑


        正则字符组  [字符组]
          在同一个位置可能出现的各种字符组成了一个字符组，
          在正则表达式中用[]表示
          字符分为很多累，比如数字，字母，标点等等


          元字符：
            1 .      匹配除换行符以外的任意字符
            2 \w     匹配字母或数字或下划线
            3 \s     匹配任意的空白符
            4 \d     匹配数字
            5 \n     匹配一个换行符
            6 \t     匹配一个制表符tab
            7 \b     匹配一个单词的结尾
            8 ^      匹配一个字符串的开始
            9 $      匹配一个字符串的结束
            10 \W    匹配非字母或数字或下划线
            11 \D    匹配非数字
            12 \S    匹配非空白符
            13 a|b   或 a或则b
            14 ()    匹配括号内的表达式，也表示一个组
            15 [..]  匹配字符组中的字符
            16[^..]  匹配除字符组中字符的所有字符



            量词   用来约束元字符
            1 *       重复0次或更多次
            2 +       重复一次或更多次
            3 ？      重复0次或一次
            4{n}      重复n次
            5{n，}    重复n次或更多次
            6{n,m}    重复n到m次

            ()分组与 或 |  组合使用的时候要注意将长的放在前边
            可以将多个元字符放入一组
            后边在加量词可以约束组内的所有字节

            贪婪匹配和费贪婪匹配
             1 贪婪匹配：在满足匹配时，匹配尽可能长的字符串，默认情况下采用贪婪
             2 非贪婪：在满足匹配时，匹配尽可能少的字符串

             几个常用的非贪婪匹配Pattern
                *? 重复任意次，但尽可能少重复
                +? 重复1次或更多次，但尽可能少重复
                ?? 重复0次或1次，但尽可能少重复
                {n,m}? 重复n到m次，但尽可能少重复
                {n,}? 重复n次以上，但尽可能少重复



 '''
import re


#  findall  返回所有满足匹配条件的结果 放在列表里
# ret01=re.findall('[a-z]+','eva egon yuan')
# ret01a=re.findall('a','eva egon yuan')
# print(ret01,ret01a)
# #   search
# #   从前往后走，找到一个就返回，返回的变量需要调用group才能拿到结果
# #   如果没有找到，那么就返回None 调用group回报错
# ret02=re.search('a','eva egon yuan').group()
# print(ret02)
# # match
# # 必须从头开始匹配，如果正则规则从头开始可以匹配上，就返回一个变量
# # 匹配的内容需要用group才能显示
# #如果没有匹配上，就返回None 调用group回报错
# ret03=re.match('ev','eva egon yuan').group()
# print(ret03)
# #split分割
# #先按照a分割得到bcd，再按照b分割得到cd
# ret04=re.split('[ab]','abcd')
# print(ret04)
#
# #sub
# #将数字替换成H  参数2 代表替换了几次
# ret05=re.sub('\d','H','eva3egon4yuan5',2)
# print(ret05)
#
# #subn
# #将数字替换成H，返回元组，返回内容是（替换的结果，替换了几次）
# ret06=re.subn('\d','H','eva3egon4yuan5')
# print(ret06)
# #
# #compile 将正则表达式编译成一个正则表达式对象
# 应用场景  正则较长 且经常使用
# obj=re.compile('\d{3}')
# ret07=obj.search('abc123ccc')
# print(ret07.group())
# ret071=obj.search('abc456cccsadf1')
# print(ret071.group())

#finditer
#finditer 返回一个存放匹配结果的迭代器
#
# ret08=re.finditer('\d','dsf1dsf1e41gb1')
# print(ret08) #迭代器内存地址
# # # # print(next(ret08).group()) #取第一个值
# # # # print(next(ret08).group()) #取第二个值
# # print([i.group() for i in ret08])#列表推倒式
#
# for i in ret08:
#     print(i.group())




#  控制分组   可根据group的参数取回下标对应分组的值  下边例子就有2个分组
# import re
# ret=re.search('[1-9](?P<id>\d{14})(\d{2}[0-9x])?$','412702199002027515')
# print(ret.group())
# print(ret.group('id'))
# print(ret.group(1))
# print(ret.group(2))

#分组优先  findall的优先级查询
# ret09=re.findall('www.(baidu|jd).com','www.baidu.com')
# print(ret09)# 只返回['baidu'] 因为findall会优先把匹配结果 组内里的内容优先返回
# # 取消分组优先  在分组内 起始位置加入？  取消分组优先
# ret09a=re.findall('www.(?:baidu|jd).com','www.baidu.com')
# print(ret09a)
#
#
# #分组优先  split的优先级查询
# ret10=re.split("\d+","eva3egon4yuan")
# print(ret10) #结果 ： ['eva', 'egon', 'yuan']
#
#
# #如果在正则上加上分组 会保留正则匹配的结果
# ret11=re.split("(\d+)","eva3egon4yuan")
# print(ret11) #结果 ： ['eva', '3', 'egon', '4', 'yuan']

#在匹配部分加上（）之后所切出的结果是不同的，
#没有（）的没有保留所匹配的项，但是有（）的却能够保留了匹配的项，
#这个在某些需要保留匹配部分的使用过程是非常重要的。


#引用分组 前后需要一样
# ret12=re.search("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>","<h1>helloword</h1>")#(?P=tag_name) 意思是引用前边分组名字且内容一致
# ret12a=re.search("<(?P<tag_name>\w+)>\w+</\1>","<h1>helloword</h1>")#  </\1> 中的\1意思是引用第一组的内容，且前后内容一致
# print(ret12.group())
# print(ret12a.group(1))
# print(ret12.group('tag_name'))

ret13=re.findall(r"\d+\d.\d+|(\d+)","1-2*(60+(-40.35/5))-(-4*3)")
print(ret13)
ret13.remove('')
print(ret13)