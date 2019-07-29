'''
元组 tuple
一个有序的序列
使用小括号()表示

元组是不可变对象,相当于一个只读的简化列表，占用的内存小
'''

'''
元组的定义 初始化
定义：
    tuple() -> empty tuple
    tuple(iterable) -> tuple initialized from iterable`s items

'''

# t = tuple()  # 工厂方法
# print(t)
# t = tuple(range(10))  # 工厂方法
# print(t)
# t = (1, 2, 5, 6, 7, 8)
# print(t)
#
# t = (1,)  # 一个元素的时候需要加，
# print(t)
#
# t = (1,) * 5
# print(t)

'''
支持索引
'''
# t = tuple(range(10))
# print(t[5])
#
# t[3] = 5  # 只读不允许设置

'''
命名元组 namedtuple
 namedtuple(typename,field_names,verbose=False,rename=False)
 命名元组，返回一个元组的子类，并定义了字段
 field_names 可以使空格或','分割的字段的字符串,可以使字段列表
比面向对象的类更轻巧
'''
from collections import namedtuple

Point = namedtuple('_point', ['x', 'y'])
p = Point(1, 2)
print(p)
print(p.x)
Student = namedtuple('Student', 'name age,sex')
tom = Student('djl', 26, 1)
print(tom)
