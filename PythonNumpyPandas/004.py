import numpy as np
#1，索引

#a=np.arange(3,15)
#print(a[3])#索引

#a=np.arange(3,15).reshape(3,4)
#print(a[2])
#print(a[1][1])#第二行第二列
#print(a[1,1])#同上
#print(a[2,:])#第二行所有数
#print(a[1,1:3])#第二行，第二列到第三列

#for row in a:#输出每一行
#    print(row)
#for column in a.T:#输出每一列
#    print(column)
#print(a.flatten())#将a转变为只有一行
#for item in a.flat:#输出所有数
#    print(item)

#2，合并

#a=np.array([1,1,1])
#b=np.array([2,2,2])
#print(np.vstack((a,b)))#并列合并,两行三列
#print(np.hstack((a,b)))#合并，一行六列

#print(a.T)
#print(a.T.shape)#转置后矩阵形状并未改变
#print(a[np.newaxis,:])#不改变长度
#print(a[np.newaxis,:].shape)#改变形状，一行三列
#print(a[:,np.newaxis])#不改变高度
#print(a[:,np.newaxis].shape)#改变形状，三行一列

#a=np.array([1,1,1])[:,np.newaxis]
#b=np.array([2,2,2])[:,np.newaxis]
#print(np.vstack((a,b)))#合并，不改变长度
#print(np.hstack((a,b)))#合并，不改变高度
#c=np.concatenate((a,b,b,a),axis=0)#合并，不改变长度
#print(c)

#3，分割

a=np.arange(12).reshape((3,4))
#print(a)
#print(np.split(a,2,axis=1))#分割成两块，不改变高度
#print(np.array_split(a,3,axis=1))#进行不相等的分割
#print(np.vsplit(a,3))#分割成三块，不改变长度
print(np.hsplit(a,2))#分割成两块，不改变高度
