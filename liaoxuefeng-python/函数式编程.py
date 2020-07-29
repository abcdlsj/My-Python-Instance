#高阶函数----一个函数可以接收另一个函数作为参数的函数
def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))

# map/reduce
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
from functools import reduce
def normalize(L):
    return L[0].upper()+L[1:].lower()

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
from functools import reduce
def prod(L):
    def fn(x,y):
        return x*y
    return reduce(fn,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

from functools import reduce
import math
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2float(s):
    n=s.index('.')
    s=s[:n]+s[n+1:]
    n=len(s)-n
    def fn(x,y):
        return x*10+y
    def charnum(s):
        return DIGITS[s]
    return reduce(fn,map(charnum,s))/(pow(10,n))
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

#filter

def is_palindrome(n):
    L=str(n)
    return L==L[::-1]

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

#sorted
# 按照名字排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0].lower()
L2 = sorted(L,key=by_name)
print(L2)

# 按照成绩从高到低排序

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_score(t):
    return t[0][-1]
L2 = sorted(L,key=by_score)
print(L2)


## 返回函数
def createCounter():
    a=0
    def counter():
        nonlocal a
        a=a+1
        return a
    return counter
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

# 匿名函数
def is_odd(n):
    if n%2 == 1:
        return lambda n:n 
L = list(filter(is_odd, range(1, 20)))
print(L)

# 装饰器

import time,functools
def metric(fn):
    @functools.wraps(fn)
    def func(*args, **kw):
        print ('%s executed in %s ms' % (fn.__name__,10.24))
        return fn(*args, **kw)
    return func
# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


# 偏函数

## 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

