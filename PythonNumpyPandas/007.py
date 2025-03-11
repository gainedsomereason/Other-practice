import pandas as pd
import numpy as np
dates=pd.date_range('20130101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])

#1，选择数据

#print(df)
#print(df['A'],df.A)#df['A']和df.A的效果是一样的
#print(df[0:3],df['20130102':'20130104'])

#select by label:loc
#print(df.loc['20130102'])
#print(df.loc[:,['A','B']])#通过标签索引,所有行的AB列

#select by position:iloc
#print(df.iloc[[1,3,5],1:3])#通过序号索引

#boolean indexing
#print(df[df.A>8])

#2，设置值

#df.iloc[2,2]=1111
#df.loc['20130101','B']=123
#df[df.A>0]=0#df中的（A列中的所有大于0的行）（所在行所有列）赋值为0
#df.B[df.A>4]=0#df中的（A列中的所有大于0的行）（所在行的B列）赋值为0
#df['F']=np.nan#新建第F列
#df['E']=pd.Series([1,2,3,4,5,6],index=pd.date_range('20130101',periods=6))#定义一列的值
#print(df)

#3，处理丢失数据

df.iloc[0,1]=np.nan
df.iloc[1,2]=np.nan
#print(df.dropna(axis=0,how='any'))#一行中只要出现NaN就将这一行丢掉
#print(df.dropna(axis=0,how='all'))#一行中所有值都是NaN就将这一行丢掉
#print(df.fillna(value=0))#将所有的NaN值都填为0
#print(df.isnull())#所有的NaN值所在位置填为true，其他位置填false
print(np.any(df.isnull()))#只要isnull中有一个True就返回True
