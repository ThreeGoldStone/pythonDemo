# 非0 非空为true
# flag = 10
# while flag:
#     print(flag)
#     flag -= 1
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1

# for element in iterable:
#     block

# print("for 的例子 1")
# for i in range(10):
#     print(i)
# print("for 的例子 2")
# for i in range(10, 5, -1):
#     print(i)


# help(range)
# class range(object)
#     |  range(stop) -> range object
#     |  range(start, stop[, step]) -> range object [, step]表示step是可选参数


# print("for 的例子 continue 3")
# for i in range(10):
#     if i % 2:
#         continue
#     print(i)


# print("for 的例子break 4")
# count = 0
# for i in range(0, 1000, 7):
#     print(i)
#     count += 1
#     if count >= 20:
#         break


# print("while 版本")
# count = 0
# i = 0
# while True:
#     print(i)
#     i += 7
#     count += 1
#     if count >= 20:
#         break

# numb = int(input('请输入一个整数：'))
# oTimes = 1
# t = numb
# count = 0
# print('整数由低到高个位依次是：')
# while True:
#     t = numb // oTimes
#     if t == 0:
#         break
#     count += 1
#     oTimes *= 10
#     print(t % 10)
# print('共',count,"位")


# numb = int(input('请输入一个整数：'))
# numb = str(numb)
# print('整数由低到高个位依次是：')
# for i in numb:
#     print(i)
# print('共',len(numb),"位")


''' 循环else子句'''
# for i in range(10):
#     print(i)
#     if i > 5:
#         break
# else:
#     print('正常结束循环会打印')

'''打印一个边长为n的正方形 '''
# n = 6
# m = 10
# for i in range(n):
#     if i == 0 or i == n - 1:
#         print('*' * m)
#     else:
#         print('*'+' ' * (m-2)+'*')

'''求100内所有奇数的和'''
# sum = 0
# for i in range(1, 100, 2):
#     sum += i
# print('100内的奇数的和', sum)

'''求1到5的阶乘的和'''
# n = 5
# sum2 = 0
# for i in range(n):
#     s1 = 1
#     for j in range(i + 1):
#         s1 *= (j + 1)
#     sum2 += s1
# print('1到5的阶乘的和:' + str(sum2))
'''求1到5的阶乘的和优化版'''
# n = 5
# sum2 = 0
# tmp = 1
# for i in range(n):
#     tmp *= i + 1
#     sum2 += tmp
# print('1到5的阶乘的和:' + str(sum2))

'''打印小于100000的质数'''
import datetime

# n = 100000
# count = 0
# t1 = datetime.datetime.now()
# for i in range(1, n):
#     for j in range(i):
#         if j <= 1 or j == i:
#             continue
#         elif not i % j:
#             break
#     else:
#         count += 1
#         print(i)
# print('共有质数', count)
# print((datetime.datetime.now() - t1))
'''
共有质数 9593
0:01:26.012046
'''
'''打印小于100000的质数 埃拉托色尼选筛法'''
# t1 = datetime.datetime.now()
# n = 100000
# r = range(n)
# l = list(r)
# count = 0
# for i in range(2, n):
#     if l[i]:
#         print(i)
#         count += 1
#     for j in range(2 * i, n, i):
#         l[j] = 0
# print('共：' + str(count))
# print((datetime.datetime.now() - t1))
'''
共：9592
0:00:00.216424
'''

'''打印99乘法表'''
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(j, '*', i, '=', i * j, end="\t")
#     print()
'''打印99乘法表,对其版'''
# format = '{0}*{1}={2:>2}'
# '''format 中 {0} 中的0，可以不传默认是依次对其的， 代表参数的index, :<或>2表示向左或向右按照2格对其'''
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(format.format(j, i, i * j), end="\t")
#     print()

'''打印菱形'''
# n = 11
# max_n = n // 2 + 1
# for i in range(n + 1):
#     c = abs(i - max_n)
#     print(' ' * c + '*' * (n - 2 * c))
'''打印菱形，小优化'''
# n = 11
# max_n = n // 2 + 1
# for i in range(-max_n, n - max_n + 1):
#     print(' ' * abs(i) + '*' * (n - 2 * abs(i)))
'''斐波那契数列'''
# max = 100
# t1 = 1
# t2 = 1
# tmp = 0
# while t1 < max:
#     print(t1)
#     tmp = t2
#     t2 = t1 + t2
#     t1 = tmp

'''斐波那契数列 封装版'''
# max = 100
# t1 = 1
# t2 = 1
# while t1 < max:
#     print(t1)
#     t1, t2 = t2, t1 + t2
'''猴子吃桃子，共有n个桃子，每天只吃一半在加1个桃子，第10天时只剩一个桃子，求共有多少桃子'''
d = 10
n = 1
for i in range(d-1):
    n = (n + 1) * 2
    print(n)
