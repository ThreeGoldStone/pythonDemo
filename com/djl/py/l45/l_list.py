'''
reversed() -> None 将列表元素反转，返回None
就地修改
'''
# l = [1, 5, 7, 12, 3, 4, 99, 2]
# print(l.reverse())
# print(l)
'''
sort(key = None ,reverse = False) -> None 对列表元素进行排序，默认是升序
reverse 为True，反转，降序
key 是一个函数，指定key如何排序
就地修改
'''
# l = [1, 5, 7, 12, 3, 4, 99, 2]
# print(l.sort())
# print(l)
# l.sort(reverse=True)
# print(l)
# l.sort(key=lambda i: i % 2, reverse=True)
# print(l)
'''
 a in []  如果列表中有a则返回true
'''
# l = [1, 5, 7, 12, 3, 4, 99, 2]
# print(5 in l)
# print(5 not in l)
# for i in l:
#     print(i)

'''
列表的复制
'''
# lst0 = list(range(4))
# lst1 = list(range(4))
# print(lst0)
# print(lst1)
# print(id(lst0))
# print(id(lst1))
# # lst0 和 lst1 在内存中的地址是不同的
# print(lst0 == lst1)  # == 比较的是值是否相同
# print(lst0 is lst1)  # == 比较的是地址是否相同
# copy() 浅复制 对列表中的基本类型进行复制，复杂类型进行引用
# import copy copy.deepcopy() 深复制


'''
杨辉三角
'''
lst_a = []
n = 10
for i in range(1, n + 2):
    l_n = []
    for j in range(i):
        if j == 0 or j == i - 1:
            l_n.append(1)
        else:
            i_1_list = lst_a[i - 2]
            l_n.append(i_1_list[j - 1] + i_1_list[j])
    lst_a.append(l_n)
    print(' ' * ((n - len(l_n)) * 3 // 2) + str(l_n))
'''
杨辉三角 优化版
'''
lst_a = []
n = 10
for i in range(1, n + 2):
    l_n = []
    for j in range(i):
        if j == 0 or j == i - 1:
            l_n.append(1)
        else:
            i_1_list = lst_a[i - 2]
            l_n.append(i_1_list[j - 1] + i_1_list[j])
    lst_a.append(l_n)
    print(' ' * ((n - len(l_n)) * 3 // 2) + str(l_n))
