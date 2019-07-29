import math

'''
round()  4舍， 6入，5取偶
math.floor() 地板
math.ceil() 天花板
'''
# print('2.6 floor ', math.floor(2.6))
# print('2.1 ceil ', math.ceil(2.1))
# print('2.0 ceil ', math.ceil(2.0))
# print('2.51 round ', round(2.51))
# print('2.5 round ', round(2.5))
# print('2.6 round ', round(2.6))
# print('2.4 round ', round(2.4))
# print('2.56 round ', round(2.56))

'''
min() 多参数或数组
max() 多参数或数组
pow(x,y) =  x**y
math.sqrt()
rint(bin(200))   二进制    0b11001000
print(oct(200))  8进制    0o310
print(hex(200))  16进制   0xc8
'''
# print(bin(200))
# print(oct(200))
# print(hex(200))

'''type(obj) 返回类型，不是字符串'''
# print(type(10))
# print(type('123'))
# print(type(type('123')))
# print(type(10) == int)
# print(type('123') == str)
# print(type('123') == list)


'''
isinstance(obj,class_or_tuple)
tuple 是元组
都是数字的可以隐式转换
'''
print(isinstance(12, int))
print(isinstance(12, str))
print(isinstance('1231', str))
print(isinstance('1231', list))
print(isinstance('xxx', (int, str)))
print(type(True))
print(type(1+True))
print(type(1+True+2.0))
