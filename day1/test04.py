print('12'.zfill(5))
print('')
print('{name}网站：{site}！'.format(name='菜鸟教程',site='www.runoob.com'))

print('{0}网站：{1}！'.format('菜鸟教程','www.runoob.com'))

f = open("/test1.txt", "a")
num=f.write("Python is a pragram language!")
print(num)

f.close()
f=open('/test1.txt','r')
str=f.read()
print(str)
