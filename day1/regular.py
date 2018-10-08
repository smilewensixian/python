import re
import math
import random

print(re.findall(r'\bf[a-z]]','which foot or hand fell fastest'))

print(re.sub(r'(\b[a-z]+) \1',r'\1','cat in the hat'))

print(math.cos(math.pi/4))
print(math.log(1024,2))

print(random.choice(['apple','pear','banana']))
#print(random.sample(range(100),10))
print(random.random())
print(random.randrange(100))
r=random.sample(range(100),10)
print(r)
for i in r:
    print(i,end=',')