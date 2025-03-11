import pandas as pd
import numpy as np

#merging two df by key/keys.(may be used in database)
#left=pd.DataFrame({'key':['k0','k1','k2','k3'],
#                   'a':['a0','a1','a2','a3'],
#                   'b':['b0','b1','b2','b3']})
#right=pd.DataFrame({'key':['k0','k1','k2','k3'],
#                   'c':['c0','c1','c2','c3'],
#                   'd':['d0','d1','d2','d3']})
#res=pd.merge(left,right,on='key')
#print(res)

#consider two keys
#left1=pd.DataFrame({'key1':['k0','k0','k1','k2'],
#                   'key2':['k0','k1','k0','k1'],
#                   'a':['a0','a1','a2','a3'],
#                   'b':['b0','b1','b2','b3']})
#right1=pd.DataFrame({'key1':['k0','k1','k1','k2'],
#                    'key2':['k0','k0','k0','k0'],
#                   'c':['c0','c1','c2','c3'],
#                   'd':['d0','d1','d2','d3']})
#res=pd.merge(left1,right1,on=['key1','key2'],how='inner')#默认inner,与,（还可以是outer、left1、right1)
#print(res)

#indicator
#df1=pd.DataFrame({'coll':[0,1],'col_left':['a','b']})
#df2=pd.DataFrame({'coll':[1,2,2],'col_right':[2,2,2]})
#res=pd.merge(df1,df2,on='coll',how='outer',indicator=True)
#res=pd.merge(df1,df2,on='coll',how='outer',indicator='indicator_column')
#print(res)

#merged by index
#left=pd.DataFrame({
#    'a':['a0','a1','a2'],
#    'b':['b0','b1','b2']},
#    index=['k0','k1','k2']
#)
#right=pd.DataFrame({
#    'c':['c0','c1','c2'],
#    'd':['d0','d1','d2']},
#    index=['k0','k2','k3']
#)
#res=pd.merge(left,right,left_index=True,right_index=True,how='outer')
#print(res)

#handle overlapping
boys=pd.DataFrame({'k':['k0','k1','k2'],'age':[1,2,3]})
girls=pd.DataFrame({'k':['k0','k0','k3'],'age':[4,5,6]})
res=pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how='inner')
print(res)
