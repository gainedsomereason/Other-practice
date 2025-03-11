import pandas as pd
#numpy相当于列表的话，pandas就相当于字典
import numpy as np
#s=pd.Series([1,3,6,np.nan,44,1])
#print(s)

#dates=pd.date_range('20160101',periods=6)
#print(dates)
#df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
#定义了横纵坐标名称
#print(df)

#df_1=pd.DataFrame(np.arange(12).reshape(3,4))
#print(df_1)
df_2=pd.DataFrame({
    'A':1,
    'B':pd.Timestamp('20130102'),
    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
    'D':np.array([3]*4,dtype='int32'),
    'E':pd.Categorical(["test","train","test","train"]),
    'F':'foo'
})
#print(df_2)
#print(df_2.dtypes)#列的数据
#print(df_2.columns)#行的数据
#print(df_2.values)
#print(df_2.describe())
#print(df_2.T)
#print(df_2.sort_index(axis=1,ascending=False))#排序
print(df_2.sort_values(by='E'))#对第六列进行排序
