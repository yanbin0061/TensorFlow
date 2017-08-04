# Python 模块
import sys
import plotFunction
print('命令行参数:')
for i in sys.argv:
    print(i)
print("Python的路径为:", sys.path)

plotFunction.print_func('闫斌')

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x**3).rjust(4))

table = {'Google': 1, 'Module': 2, 'Bai du': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))

# 打开一个文件
f = open('foo.txt', 'w')
f.write("向文件中写入文章")
f.close()

f = open('foo.txt', 'r')
str1 = f.read()
print(str1)
f.close()
