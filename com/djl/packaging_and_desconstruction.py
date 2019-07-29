'''
封装与解构
l59
解构可以解构线性或非线性结构
'''

'''
解构元组 tuple
'''
a = (1, 2)  # 元组
b = 1, 2  # 自动封装为元组
print(type(a))
print(type(b))
print(a == b)

c = 10
d = 20
c, d = d, c  # 变量交换
print(c, d)
# 上面过程等效于下面
f = d, c  # 先封装
c, d = f  # 再解构
print(c, d)
'''
任意解构

'''
a, b = (1, 2)
print(a, b)
a, b = [3, 4]
print(a, b)
a, b = {6, 7}
print(a, b)
a, b = {'c': 9, 'd': 10}  # 接受字典时，接受的是key
print(a, b)
# a, b = {10, 20, 30} #会报错，因为数量不匹配
# print(a, b)
a, *b = {10, 20, 30}  # *表示接受剩下的所有
print(a, b)
[a, b] = 10, 20
print(a, b)
[a, b] = (15, 26)
print(a, b)
(a, b) = {'s', 'd'}  # 这个接受的顺序不固定
print(a, b)
a, b = {'s', 'd'}  # 这个接受的顺序不固定
print(a, b)
