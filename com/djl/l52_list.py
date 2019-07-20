'''
list.append(obj) -> None 往列表尾部添加元素
时间复杂度o(1)
'''
# list = [1, 2, 3, 5, 8, 2]
# list.append(4)
# print(list)
'''
list.insert(index,obj) -> None 往列表的index前插入一个元素
时间复杂度o(n)
'''
# list = [1, 2, 3, 5, 8, 2]
# list.insert(4,0)
# print(list)


'''
list.extend(iteratable) -> None 把可迭代的对象元素追加进来，就地修改
'''
# list = [1, 2, 3, 5, 8, 2]
# list.extend([4,4])
# print(list)
'''
+ -> list 连接操作 返回新的列表，之前的列表不变
'''
# list = [1, 2, 3, 5, 8, 2]
# list2 = [5, 8]
# print(list + list2)

'''
* -> list 重复操作，将本列表的元素重复n次，返回新的列表
'''
# list = [1, 2, 3, 5, 8, 2]
# print(list * 3)

'''
remove() -> None 删除第一个匹配的元素，就地修改（意思是在原数组上做修改，被删除的位置后面的会向前移动，效率略差）
pop([index]) -> item 不指定index时从末尾弹出，指定index后从index弹出，返回弹出的对象 
clear() -> 清空列表所有元素，剩下一个空列表,
'''
list = [1, 2, 3, 5, 8, 2]
print(list)
list.remove(2)
print(list)
print(list.pop())
print(list)
print(list.pop(1))
print(list)
list.clear()
print(list)
