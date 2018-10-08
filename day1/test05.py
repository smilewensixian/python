import os, sys

# 假定 /tmp/foo.txt 文件存在，并有读写权限

ret = os.access("/test1.txt", os.F_OK)
print ("F_OK - 返回值 %s"% ret)

ret = os.access("/test1.txt", os.R_OK)
print ("R_OK - 返回值 %s"% ret)

ret = os.access("/test1.txt", os.W_OK)
print ("W_OK - 返回值 %s"% ret)

ret = os.access("/test1.txt", os.X_OK)
print ("X_OK - 返回值 %s"% ret)