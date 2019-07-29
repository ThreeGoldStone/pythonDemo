'''
线性结构：
在内存中放在连续区域
可迭代 for ... in
len() 获取长度
通过下标访问
可以切片
学过的线性结构：
列表，元组，字符串，bytes，bytearray
'''

'''
切片
通过索引区间访问线性结构的一段数据
sequece[start:stop] 表示返回[staret,stop)区间的子序列
支持负索引
start为0的时候可以省略
stop为末尾，客忽略
超过上界就取末尾，超过下届就取开头
start一定要在stop左边
[:]表示从头到尾，全部元素被取出，等效于copy()方法



步长切片
[start:stop:step]
step为步长，可正负，默认为1
step要和start:stop同方向
'''
print('w 是一个超人'[2:5])
print('w 是一个超人'[:])
print('w 是一个超人'[:5])
print('w 是一个超人'[2:])
print('w 是一个超人'[5:2:-1])
