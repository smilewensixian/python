
s='{0},I am {0},I\'m {1} years old'
print(s.format('xiaowang',12))

sex=input("请输入您的性别：")
print("您的性别为{0}".format(sex))

if(sex=='男'):
    print("您是男的")
    print("打工去")
else:
    print("你是女的")
    print("请吃饭")
score=int(input('please input your score:'));
if(score<60):
    print("不及格")
elif(score>=60 and score<80):
    print("及格")

list=['张三','李四','王五']
for i in list:
    if i=='张三':
        print("我们需要表达自己,{0}".format(i))
    else:
        print("我们需要冷酷的拒绝{0}".format(i))
for j in range(0,10):
    while j > 1:
        print(j)
        break
    print(j)

benjing=100000
fanbei=200000
year=0

def func():
    print("this is a blank functhion")

while benjing<fanbei:
    benjing=benjing*(1+0.067)
    year+=1
    if benjing<fanbei:
        print("第{0}年了，本金还没有翻倍".format(year))

else:
    print("第{0}年，您的本金是：{1}".format(year, benjing))
    print("congratuation !!!")
    func()

for i in range(1,10):
    for j in range(1,i+1):
       # if i>=j:
            print("{1}*{0}={2}".format(i,j,i*j),end='    ')
    print('')

def funct1(p1,p2,p3):
    print(p1,p2,p3=2)

def stu( **kwargs):
    for i in kwargs.items():
        print(i)
stu(name='liuying',age=19,addr='北京大院')

a1=100
def fun():
     print(a1,end=',')
     print("I am in functhion")
     global a2
     a2=99
     print(a2,end=', ')
print(a1)
fun()
print(a2)

a=1
b=2
def fun1(c,d):
    e=111
    print("locals={0}".format(locals()))
    print("Globals={0}".format(globals()))
fun1(200,100)

#eval()函数
#exec()函数，无返回结果，
#把一个字符串当成一个表达式来执行，返回表达式执行后的结果
x=2
y=43
z=eval("x+y")
print(z)
z2=exec(("x*y"))
z3=exec("print('x+y=',x+y)")
print(z2)

