import sys
import _osx_support
import winsound

a=['23','qwe']
print(a.count(333),a.count(66.25),a.count('x'))
a.insert(2,-1)
print(a)
a.append('123')
print(a)
print(a.index("123"))
print(a)

maxtri=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(maxtri)
for i in maxtri:
    print(i,end="-")

print('命令行参数如下：')
for i in sys.argv:
    print(i)
print('Python路径为：',sys.path,'\n')
