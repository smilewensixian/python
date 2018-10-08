"""
定义一个学生类
"""
class Student():
    pass
xiaoli=Student()

class PythonStudent():
    name=None
    age=18
    course="Python"
    def doHomework(self):
        print("I 在做python课后作业")
        #推荐函数末尾使用return
        return None
#实例化一个PythonStudent对象
yueyue=PythonStudent()
yueyue.age
print(yueyue.age)
print(yueyue.name)
yueyue.doHomework()
print("github updating")
