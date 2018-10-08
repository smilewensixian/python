import math
import random
import sys
str='this is a string'                   #字符串类型
list=['list1','list2','list3',213,23.1]  #列表类型
tuple=('123','tuple2',23123)              #元组类型
dict={'dic1':'value1','dict2':'value2'}                         #字典类型
set={'123','qwe','qwe',12,'asd','qwe'}       #集合类型set

print(str)
print(str[5:])
print(list)
print(list[0])
print(tuple)
print(tuple[0])
print(dict)
print(dict["dic1"])
print(dict.keys())
print(dict.values())
print(set)
if 'qwe' in set:
    print('qwe 在set集合中存在')
else:
    pass

print(isinstance('12',int))
print(5**3)
print(5.1*3)
print(5.1*3.0)
print(5.2*3)
print((5.1*3))
print(str)
print(str+'  dfadfsdfdfa')
print(list)
print(list[0])
print(len(list))
tinydict = {2: 'runoob','code':1, 'site': 'www.runoob.com'}
print(tinydict[2])
flag=False
if flag:
    print(flag)
else:
    print(flag)
def a():
    '''
    这是文档字符串22
    顶替人人人人人人人人人人人人人人人人
    '''
    print('hahhahahhah')
print(a.__doc__)
a()
a=10
b=20
b=a
print(a==b)
print(a is b)

a=20
b=10
c=15
d=5
e=0
e=(a+b)*c/d
print(e)
print(17//3)
print(abs(-12))
print(max(1,2,3,1,2,3,4))
print(random.choice(range(200)))
number=0XA0F
print(number)
print(int(3.2))
print(float(3))
random.randrange(5,10,1)
list=[1,4,6,7,8,999]
print(random.shuffle(list))
var1='hello world'
print('已更新字符串：',var1[:6]+'Runoob!')
print(var1)
print(var1+'  new'+'\a')
print("我叫%s 今年 %d岁！" %('小明',10))
para_str="""this is a para string
多行字符串可以使用tab(\t)
也可以使用换行符"""
print(para_str)
s1 = "-"
s2 = ""
seq = ("r", "u", "n", "o", "o", "b") # 字符串序列
print (s1.join( seq ))
print (s2.join( seq ))
print(str)
print(str.upper())
list=['list2','234','df',12]
print(list[2])
list[2]='eeee'
print(list[2])
del list[2]
print(list)
print(dict)
a={'a','b','c','d'}
if 'a' in a:
    print(True)
else:
    print(False)
print(a)
a.add('e')
print(a)

a,b=0,1
while b<56:
    print(b,end=',')
    a,b=b,a+b

print(2**10)
print(2**16)
print(2**17)
"""
var1=100
if var1:
    print('1-if表达式条件为True')
    print(var1)
age=input("请输入你家狗狗的名称:")
print("")
if int(age)<0:
    print("Are you kidding me")
if int(age)==1:
    print("相当于14岁的人")
elif int(age)==2:
    print("相当于24岁的人")
elif int(age)>2:
    print('df')
input('点击enter键退出')
num=10
flag=1
while flag:
    guessint = input('please input a number')
    if int(guessint)<num:
        print('num is bigger than you,please input')
    if int(guessint)>num:
        print("num is smaller than you ,please input")
    if int(guessint)==num:
        print("conguatulations ,you guess it ")
        flag=0
for i in range(5,9):
    print(i)

for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")

lst=[1,2,3,4,5]
it=iter(lst) #创建迭代器
print(next(it)) #创建迭代器的下一个元素
print(next(it))
for i in lst:
    print(i,end=",")
print()

def fibonacci(n):
    a,b,counter=0,1,0
    while True:
        if(counter>n):
            return
        yield a
        a,b=b,a+b
        counter+=1
f=fibonacci(10)

while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()
"""
def ChangeInt(a):
    a=10
b=2
ChangeInt(b)
print(b)


# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)
#生成器的问题
#匿名函数

total=0
def sum(arg1,arg2):
    total=arg1+arg2
    print(total)
    return total
sum(10,20)
print(total)