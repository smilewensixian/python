from urllib.request import  urlopen
from datetime import date


for line in urlopen('http://dingtalk.sbtjt.com'):
    line=line.decode('utf-8')
    if 'EST' in line or 'EDT' in line:
        print(line)
    for c in line:
        print(c)

now=date.today()
print(now)