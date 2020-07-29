# -*- coding: utf-8 -*-

# 数据类型和变量
n = 123
f = 456.789
s1 = '\'Hello, world\''
s2 = '\'Heloo, \\\'Adam\\\'\''
s3 = 'r\'Hello, \"Bart\"\''
s4 = 'r\'\'\'Hello,\nLisa\'\'\''
print ('n = ',n)
print ('f = ',f)
print ('s1 = ',s1)
print ('s2 = ',s2)
print ('s3 = ',s3)
print ('s4 = ',s4)

# 字符串和编码

s1 = 72
s2 = 85
r = (s2-s1)*100/s1
print ('%.1f%%' % r)
print ('{:.1f}%'.format(r))

# 使用list和tuple

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])

# 条件判断
# -*- coding: utf-8 -*-
# 解决vscode乱码可以添加系统变量PYTHONIOENCODING项,值为UTF-8
height = 1.75
weight = 80.5

bmi = weight/(height*height)
if bmi<18.5:
    print('过轻')
elif 18.5<=bmi<25:
    print ('正常')
elif 25<=bmi<28:
    print ('过重')
elif 28<=bmi<=32:
    print ('肥胖')
else:
    print ('严重肥胖')

#循环
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print ('Hello ,{0}'.format(name))

#使用dict和set

#No practice