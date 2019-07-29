'''
string 可以理解为特殊的元组,是不可变对象，他内的字符叶复科被修改
有序，可迭代
python 中的string和java中的略有不同，它不是字符的列表，应该是字符串的列表（因为python中没有字符的概念）
'''

s1 = "I'm super super student"
s2 = "I'm very very sorry"
s3 = r"hello \n magedu.com"  # R 和r是一样的表示后面的字面量不做特殊字符转化
s4 = '''
sxxdf
xcfsd
x
dsf
sd
f   xxx
'''
print(s1[0])
print(type(s1[0]))  # 还是str
print(s3)
print(s4)

for c in s1:  # 可以当成数组使用
    print(c)
# s1[5] = "xx" #不可修改，会报错

lst = list(s1)
print(lst)
t = tuple(s1)
print(t)
'''
字符串的连接
+ -> str 拼接返回新的str
'string'.join(iterable) -> str 将可迭代对象用string连接起来，返回新的字符串
'''
print('>>'.join(s1))
print('<a<'.join(['a', 'b', 'xxx']))
# print('-xx-'.join(['a', ['b', c], 'd']))   #复杂对象不能用，会报错


'''
字符串的分割
python的设计分为两种，一种时是其他语言也有的，一种是它自有的
split（sep=None,maxsplite=-1)
从左向右
sep(separator) 指定分割字符串，缺省情况下为空白串
maxsplit 指定分割次数，-1表示遍历所有

rsplit（sep=None,maxsplite=-1)
从右往左
其他一样

splitlines([keepends]) 
按照行分割字符串
keepends 指是否保留行分割符
行分隔符包括 \n \r\n \r等

'''
print(s4.split())
print(s4.split('s'))
print(s4.split('s', 2))
print(s4.split(maxsplit=3))
print(s4.rsplit())  # 反向查找，但返回的顺序与正的相同
print(s4.splitlines())
print(s4.splitlines(True))

'''
字符分割*
partition(sep) -> (head,sep,tail) 一刀两段
从左至右， 遇到分隔符就把字符串分割为2部分，返回一个元组
sep 分割字符串，必须指定
rpartition(sep) -> (head,sep,tail) 
反方向查找
'''
print(s1.partition('super'))
print(s1.rpartition('super'))

'''
字符串的大小写
upper()
全大写
lower()
全小写
swapcase()
交换大小写
'''

print(s1.upper())
print(s1.lower())
print(s1.swapcase())

'''
字符串的排版
title() ->str
标题的每个单词都大写
captitalize() ->str
首字母大写
center(width[,fillchar]) ->str
width 打印宽度
fillchar 填充的字符
zfill(width) -> str
width 打印宽度，居右，左边填充0
ljust(width[,filchar]) -> str 左对齐
rjust(width[,fillchar]) -> str 右对齐
中文用的少，只做了解
'''
print(s1.title())
print(s1.capitalize())
print('aaa'.center(10))
print('aaa'.center(10, '#'))
print('aaa'.zfill(10))
print('abc'.ljust(10, '#'))
print('abc'.rjust(10, '#'))

'''
字符串的替换*
replace(old,new[,count]) -> str
字符串中找到匹配的
'''
print(s1.replace('super', 'very'))
print(s1.replace('super', 'very', 1))
'''
strip([chars]) -> str
从字符串的两端去掉指定字符集chars中的所有字符
如果chars没有指定，则会去除两端的空白字符
lstrip([chars]) -> str 去左边
rstrip([chars]) -> str 去右边
'''
print('\r \t\n Hello Python \n\t'.strip())
print("I'm very very very sorry ".strip('Irv '))
print("I'm very very very sorry ".strip('Irvy '))
print('\r \t\n Hello Python \n\t'.lstrip())
print('\r \t\n Hello Python \n\t'.rstrip())

'''
字符串的查找
find(sub[,start[,end]]) -> int
在指定区域(start,end), 从左至右的查找指定的sub字符串，找到立即返回字符串位置，没找到返回-1
rfind(sub[,start[,end]]) -> int
从右往左
'''
print(s2)
print(s2.find('v'))
print(s2.find('v', 4))  # 程序编程默认前包后不包
print(s2.find('v', 5))
print(s2.find('v', 5, 7))  # 找不到 返回-1
print(s2.find('v', -10, -1))  # 负索引也可以用 找不到 返回-1
print(s2.rfind('v'))

'''
字符串的查找
index (sub[,start[,end]]) -> int
rindex (sub[,start[,end]]) -> int
与find相同，但没找到是抛出异常 ValueError
count (sub[,start[,end]]) -> int
统计sub出现的次数,一般不这么做，效率太低
'''
print(s2.count('very'))
'''
字符串的判断
endswith(suffix[,start[,end]]) ->bool
判断在指定区间(start,end)内的字符串是否以suffix结尾
startswith(suffix[,start[,end]]) ->bool
判断在指定区间(start,end)内的字符串是否以suffix开始
'''

'''
字符串的判断is系列
isalnum() -> bool 是否是字母和数字组成
isalpha() 是否是字母
isdecimal 是否只包含十进制数
isdigit 是否全是数字（0~9）
isidentifier 是不是以字母和下划线开头，
...
'''

'''
字符串格式化
format 函数格式字符串语法---python鼓励使用

"{}{xxx}".format(*args,**kwargs) -> str
args 是位置参数，是一个元组
kwargs是关键字参数，是一个字典
花括号标识占位符
{}表示按照顺序匹配参数，{n}表示区位置参数索引为n的值
{xxx}表示在关键字参数中搜索名称一致的
{{}}表示打印花括号
'''
print('{}.{}.{}'.format('a', 'b', 'c'))  # 默认顺序
print('{1}.{0}.{1}'.format('a', 'b', 'c'))  # 关键字或index
print('{1}.{0}.{1}'.format('a', 'b', 'c', server='xxx'))  # 关键字或index
print('{server}.{0}.{1}'.format('a', 'b', 'c', server='xxx'))  # 关键字或index
print('{0[0]}.{0[1]}.{1}'.format(('aa', 'bb'), 'cc'))  # 访问元素

from collections import namedtuple

point = namedtuple('Point', 'x y')
x = point(4, 5)
print('{0.x}.{0.y}.{1}'.format(x, 'cc'))  # 对象属相访问

print('{0}*{1}={2:3}'.format(3, 4, 3 * 4))  # :3右对齐，3个不足补空格
print('{0}*{1}={2:<3}'.format(3, 4, 3 * 4))  # :<3左对齐，3个不足补空格
print('{0}*{1}={2:<03}'.format(3, 4, 3 * 4))  # :<3左对齐，3个不足补0
print('{0}*{1}={2:03}'.format(3, 4, 3 * 4))  # :<3右对齐，3个不足补0
print('{:^30}'.format('centered'))  # 居中补齐
print('{:x^30}'.format('centered'))  # 居中补齐
print('int:{0:d}; hex:{0:x}; oct:{0:o}; bin:{0:b}'.format(55))  # 进制
print('int:{0:d}; hex:{0:#x}; oct:{0:#o}; bin:{0:#b}'.format(55))  # 进制
octes = [192, 168, 0, 1]
print('{:02X}.{:02X}.{:02X}.{:02X}'.format(*octes))  # :02表示2位对齐不够补0，X表示16进制， * 参数解构
