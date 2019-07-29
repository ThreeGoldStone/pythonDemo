'''
字符串与butes
字符串是字符组成的有序序列，字符可以使用编码来理解
bytes是字节组成的不可变序列
bytearray是字节组成的有序的可变序列

编码与解码

字符串按照不通的字符集编码encode返回字节序列bytes
encode(encoding='utf-8',errors='strict') -> bytes
字节序列按照不通的字符集解码decode返回字符串
bytes.decode(encoding='utf-8',errors='strict') -> str
bytearray.decode(encoding='utf-8',errors='strict') -> str


'''

encode = 'xxx我是呵呵'.encode()
print(encode)
print(*(encode))
print(bytearray(encode))
print(encode.decode())

print(bytes())  # 返回空的bytes
print(bytes(10))  # 返回10长度的填充0的byte数组
print(bytes(256))  # 返回256长度的填充0的byte数组
print(bytes([12, 33, 44, 55]))
# print(bytes([12,33,44,55,256])) #byte 范围[0，255] 256会报错

'''
bytes的操作和和string类似,都是不可变类型，随意很多方法都一样。只不过bytes的方法输入和输出都是bytes
类方法：(类似于java中的静态方法)
bytes.fromhex('6162 09 6a 6b00')
hex()
返回16进制表示的字符串
bytearray 方法类似于bytes bytearray是可变类型，修改方法变成就地修改
'''
a = b'xx,ss,fff'

print(a.split(b','))
print(bytes.fromhex('6162 09 6a 6b00'))
print(b'abc'.hex())
