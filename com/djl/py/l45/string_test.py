s = 'aaaaa xxfsdf sdfasd 12312n1 v12312312'
print(s[9])
print(type(s[9]))
print('x' in s)
print('sdf' in s)
print('v123' in s)

print('>>'.join(s))

'''
字符串的分割
split(seo = None,maxsplit=-1) -> list of string
sep 指定分割字符串，缺省清空下为空白字符串(不是只是空格)
maxsplit 指定分割次数，-1标识遍历所有
'''
s1 = "I'm \ta super student"
print(s1.split())
print(s1.split("super"))
print(s1.split(" "))
print(s1.split(" ", 2))
print(s1.split("\t", 4))
print(s1.split(maxsplit=1))
