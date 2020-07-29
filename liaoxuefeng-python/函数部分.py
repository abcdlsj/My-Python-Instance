#调用函数
# -*- coding: utf-8 -*-

n1 = 255
n2 = 1000

n1 = hex(n1)
n2 = hex(n2)
print (n1)
print (n2)

#定义函数
import math
def quadratic(a, b, c):
    if b*b-4*a*c<0:
        print('没有实根')
    elif b*b-4*a*c==0:
        x1 = [-b+math.sqrt(b^2-4*a*c)]/(2*a)
        print('一个实根:{0}'.format(x1))
    else:
        x1 = [-b+math.sqrt(b^2-4*a*c)]/(2*a)
        x2 = [-b-math.sqrt(b^2-4*a*c)]/(2*a)
        print('两个实根：x1 = {0},x2 = {1}'.format(x1,x2))

a=int(input('请输入a：'))
b=int(input('请输入b：'))
c=int(input('请输入c：'))
print(quadratic(a,b,c))

#函数的参数
def product(x,*y):
    for n in y:
        x=x*n
    return x

print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

# 递归函数
def mov(n,a,b,c):
    if n==1:
        print(a,'-->',c)
        return 
    else:
        mov(n-1,a,c,b)
        mov(1,a,b,c)
        mov(n-1,b,a,c)

mov(3,'a','b','c')