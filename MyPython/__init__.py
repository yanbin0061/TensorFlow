
import sys
print('你好，闫斌')
print('你好，闫斌')
xx = 'runoob'
sys.stdout.write(xx+'\n')
x = 'a'
y = 'b'
# 换行输出
print(x)
print(y)
print('------------')
# 不换行输出
print(x, end=' ')
print(y, end='')
print()
print('---------------------------------------------------')
print('命令行参数为:')
for i in sys.argv:
    print(i)
    print('-----------')
print('\n python的路径为', sys.path)
for i in range(1000):
    print('\a')
    print('响铃')

# 菲波纳契数列
a, b = 0, 1
while b < 10000:
    print(b, end=',')
    # a, b = b, a + b
    c = a
    a = b
    b = c + b
# 狗的年龄计算判断
'''
print("")
age = int(input("请输入你家狗狗的年龄:"))
print("")
if age < 0 :
    print("你在逗我吗?")
elif age == 1 :
    print("相当于14岁的人！")
elif age == 1 :
    print("相当于22岁的人!")
elif age > 2 :
    human = 22 + (age-2)*5
    print("对应人类年龄:", human)
'''
# 数字猜谜游戏
'''
number = 7
guess = -1
print("数字猜谜游戏")
while guess != number:
    guess = int(input("请输入你猜的数字:"))
    if guess == number:
        print("恭喜你猜对了！")
    elif guess > number:
        print("你猜的数字太大了......")
    elif guess < number:
        print("你猜的数字太小了......")
 '''
# 迭代器
lists = [1, 2, 3, 4]
it = iter(lists)
for x in it:
    print(x)
print('============')
lists = [1, 2, 3, 4]
it = iter(lists)
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
