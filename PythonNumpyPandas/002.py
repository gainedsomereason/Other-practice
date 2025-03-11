import numpy as np
#a=np.array([2,34,5],dtype=np.int32)
#a=np.array([2,34,5],dtype=np.float64)#定义类型
#print(a.dtype)

#a=np.zeros((3,4))#3行4列的矩阵，元素全是零
#a=np.ones((3,4),dtype=np.int16)#全为1
#a=np.empty((3,4))#各元素接近0的矩阵

#a=np.arange(10,20,2)#大于10，小于20，步长为2
#a=np.arange(12).reshape(3,4)#大小为12，重排列为3行4列
#a=np.linspace(1,10,20)#生成线段，头为1，尾为10，数组元素个数为20
a=np.linspace(1,10,6).reshape(2,3)#线段重排列为2行3列

print(a)
