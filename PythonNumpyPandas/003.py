import numpy as np
#a=np.array([10,20,30,40])
#b=np.arange(4)
#print(a,b)
#c=a-b'两矩阵相加减'
#c=b**2#b的平方
#c=10*np.sin(a)#三角函数
#print(c)
#print(b<3)#输出bool型数组，大小和b一样
#print(b==3)

#a=np.array([[1,1],
#           [0,1]])
#b=np.arange(4).reshape(2,2)
#print(a)
#print(b)
#c=a*b#各项相乘
#c_dot=np.dot(a,b)#矩阵的乘法
#c_dot_2=a.dot(b)#和上面一样
#print(c_dot)
#print(c_dot_2)

#a=np.random.random((2,4))
#print(np.sum(a))#求和
#print(np.sum(a,axis=1))#axis=0,对每一列求和，axis=1，对每一行求和
#print(np.max(a))#最大值
#print(np.min(a))#最小值
#print(a)

#a=np.arange(2,14).reshape(3,4)
#print(a)
#print(np.argmin(a))#最小索引，0
#print(np.argmax(a))#最大索引，11
#print(np.mean(a))#平均值
#print(a.mean())#同上
#print(np.average(a))#平均值
#print(np.median(a))#中位数
#print(np.cumsum(a))#和a的元素个数一样，每一项为a中到次位置元素的累加，前n项和
#print(np.diff(a))#每两项之间的差,12之间，23之间，34之间，这样的
#print(np.nonzero(a))#非零项的位置
a=np.arange(14,2,-1).reshape(3,4)
#print(np.sort(a))#排序
#print(np.transpose(a))#转置矩阵
#print(a.T)#同上
print(np.clip(a,5,9))#小于5的数替换为5，大于9的数替换为9
