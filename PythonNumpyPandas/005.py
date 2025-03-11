import numpy as np
a=np.arange(4)
print(a)
b=a#引用复制，复制的是指针
c=a.copy()#值复制，deep copy
a[0]=6
print(b)
print(c)
