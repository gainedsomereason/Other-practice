import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#折线
#data=pd.Series(np.random.randn(1000),index=np.arange(1000))
#data=data.cumsum()
#data.plot()
#单独用pyplot时需要plt.plot(x= ,y= )，但这里在pandas当中已经有表了
#plt.show()

#数据点
data=pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list("abcd"))
data=data.cumsum()
##print(data.head())
##data.plot()
##plt.show()
##plt的方法：bar,hist,box,kde,area,scatter,hexbin,pie
#一般单独用pyplot时需要plt.scatter(x= ,y= )
ax=data.plot.scatter(x='a',y='b',color='DarkBlue',label='class 1')
data.plot.scatter(x='a',y='c',color='DarkGreen',label='class 2',ax=ax)
plt.show()
