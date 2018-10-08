"""
while True:
    try:
        x=int(input("please input a number:"))
        print("You input a number is ",x)
        break
    except ValueError:
        print("Oops! That was no valid number.Try again  ")
    except NameError:
        print("Name is error")

    except ZeroDivisionError:
        print("Handling run-time error:",error)
    else:
        print("This is no error!")

try:
    raise  NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise

class MyClass:
    i=122
    def fu(self):
        return "this is a functhion"
x=MyClass()
print("this is a 属性",x.i)
print('this is a function:this is a function',x.fu())

class Test:
    def prt(self):
        print(self)
        print(self.__class__)
t=Test()
t.prt()

class Test:
    def prt(runboot):
        print(runboot)
        print(runboot.__class__)
try:
    t=Test()
    t.prt()
except NameError:
    print("this is a error name")
"""
class people:
    name=''
    age=0
    _weigth=0
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self._weigth=w
    def speak(self):
        print("%s 说：我%d岁。" %(self.name,self.age))

class student(people):
    grade=0
    def __init(self,n,a,w,g):
        people.__init__(self,n,a,w)
        self.grade=g
    def speak(self):
        print("%s说：我%d岁了，我在读%d年级" %(self.name,self.age,self.grade))
s=student('ken',10,69)
s.speak()

class Parent:
    def myMethod(self):
        print('调用父类方法')
class Child(Parent):
    def myMethod(self):
        print('调用子类方法')
c=Child()
c.myMethod()
super(Child,c).myMethod()