### map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
### Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。

### reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
### reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

### 1 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其它字母小写的规范名字。
### 输入：['adam', 'LISA', 'barT']
### 输出：['Adam', 'Lisa', 'Bart']

def normalize(name):
	return (name[0].upper() + name[1:].lower())

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


### 2 请编写一个prod()函数，可以接受一个list并利用reduce()求积
from functools import reduce

def prod(L):
    return reduce(lambda x, y : x * y, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


### 3 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456

def str2float(s):
	s = s.split('.')  ### 拆分结果是['123', '456']

	def fleft(x,y):
		return (x*10+y)

	def fright(x,y):###注意输入结果从后往前：654
		return (x/10+y)

	def str2num(ch):
		dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
		return dic[ch]

	str2digit = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

	return (reduce(fleft, map(lambda ch: str2digit[ch], s[0])) + reduce(fright, map(str2num, list(s[1])[::-1]))*0.1)

print('str2float(\'123.456\') =', str2float('123.456'))

if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')