import pandas as pd
import numpy as np
#data=pd.DataFrame(np.arange(24).reshape((8,3)),index=pd.date_range('20241012',periods=8),columns=['a','b','c'])
#data.to_csv('student.csv')
data=pd.read_csv('student.csv')#读文件
print(data)
#data.to_pickle('student.pickle')#存文件
