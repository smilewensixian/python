l = []
print(type(l))
l = [100, 2, 109]
print(l)
l2 = (100, 3, 13, 113, 23, 1, 3, 2, 3, 4, 12, 4, 2, 4, 12, 41, 24, 124, 12, 4, 12)
print(l2)
print(l2.__len__())
for i in l2:
    print(i, end=" ")
print(l2[1:15:2])
print(id(l2))
print(id(l2[1:3]))
exec('print("滴")')
s = eval("print('滴','菜鸟！','打个卡')")
a = [1, 2, 3, 4, 5, 6, 7]
for i in a:
    print(i, end='#')
b = ['I love wangxiaojing', '123']
for i in b:
    print(i, end=';')
a = [1, 2, 4, 4, 5, 6]
length = len(a)
print(length)
for i in range(1, 10):
    print(i, end=',')
print()
for i in a:
    print(i)

b = [x for x in range(1, 10)]
print(b)

s = 'I love wangxiaojing'
print(list(s))

# tuple不可修改，与list唯一的区别，所有list的属性，他都存在
t = ()
print(type(t))
t1 = (5, 2, 3, 15, 12)
print(t1)
print(t1[1])
print(t1[1:10])
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(id(t1))
print(id(t2))
t1 = t1 + t2
print(t1)
print(id(t1))

print(t1)
t={1,2,3}
if 2 in t:
    print("YES")
else:
    print("NO")
a=1
b=3
print(a)
print(b)

a,b=b,a
print(a)
print(b)

t=(1,2,"12",2)
print(set(t))
s=set()
s={1,2,1,2,12,1,32}
print(type(s))
print(s)
e={1,2,3}
print(type(e))
f=[1,2,13,21321]
print(type(f))
#list []
#tuple ()
#set {}
#dict {'name',"xiaoming"}
l=[121,34]
t=(1,2,3,3,2)
s={1,23,2,1,2}
dict={'name':"xiaoli","sex":"nan"}
print(type(l))
print(type(t))
print(type(s))
print(type(dict))
print(l)
print(t)
print(s)
print(dict)
print(dict["sex"])

print(l[1])
s1={1,3,2,33}
print("s1=",s1)
s2={3,4,2,34,4}
ss1=s1.intersection(s2)
print("s1=",s1)
print(ss1)
ss2=s1.difference(s2)
print("s1=",s1)
print(ss2)
ss3=s1.copy()
print(s1)
print(ss3)

d1={"one":1,"two":2,"three":3}
print(d1)
print(type(d1))
d2=({"one":1,"two":2,"three":3})
print(d2)
print(type(d2))
d1.items()
#通过键值进行访问
print("d1字典的值是：",d1["one"])
if 2 in d1:
    print("value")
if "two" in d1:
    print("key")

print(d1)
for k in d1:
    print(d1[k])
for v in d1.values():
    print(v)
for k,v in d1.items():
    if(v%2==0):
        print(k, '..', v)
dd={k:v for k,v in d1.items() if v%2==1}
print(dd)
print(d1.items())
print(d1.items())
print(d1.get("one",222))
print(d1.get("one12",2222))