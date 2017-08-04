"""
 定义函数的规则
     1.函数代码快以def开头， 后面接标识符合圆括号
"""


def hello():
    print('Hello world!')


hello()


# 计算矩形的面积

def area(width, height):
    return width * height


def print_welcome(name):
    print("Welcome", name)


print_welcome("闫斌")
w = 4
h = 5
print("width:", w, "heigh:", h, "area = ", area(w, h))


# 定义函数
def print_me(strs):
    "打印传入的字符串"
    print(strs)
    return


# 调用函数
print_me("调用自定义函数")
print_me("调用同一个自定义的函数")


# 传不可变的对象（整数， 字符串， 元组）

def changeInt(a):
    a = 10


b = 2
changeInt(b)
print(b)


# 传可变的对象
def changeList(myList):
    myList.append([1, 2, 3, 4])
    print("函数内取值:", myList)
    return


myList = [10, 20, 30]
changeList(myList)
print("函数外取值:", myList)


# 使用关键字参数
def printInfo(name, age):
    print("姓名:", name)
    print("年龄:", age)
    return


printInfo(age=20, name="闫斌")


# 默认参数
def printInfo1(name, age=50):
    print("姓名:", name)
    print("年龄:", age)
    return


printInfo1(name="张三", age=14)
printInfo1(name="李四")


# 不定长参数
def printInfo2(arg1, *varTuple):
    "打印任何传入的参数"
    print("输出:")
    print(arg1)
    for var in varTuple:
        print(var)
    return


print('----------------------')
printInfo2(10)
printInfo2(10, 10, 10, 10)

# 匿名函数
sum1 = lambda arg1, arg2: arg1 + arg2

print("相加后的值:", sum1(10, 20))

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])
