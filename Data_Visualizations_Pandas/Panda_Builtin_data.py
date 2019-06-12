#!/usr/bin/env python
# coding: utf-8

# In[85]:


import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')


# In[86]:


df1 = pd.read_csv('df1.csv', index_col=0)


# In[87]:


df1.head()


# In[109]:


df2 = pd.read_csv('df2.csv')


# In[110]:


df2


# In[90]:


df1['A'].plot.hist()


# In[91]:


df1['A'].plot.hist(bins=20,edgecolor='k').autoscale(enable=True,axis='both',tight=True)


# In[92]:


df1['A'].plot.hist(bins=80,edgecolor='k').autoscale(enable=True,axis='both',tight=True)


# In[93]:


df1['A'].plot.hist(grid=True)


# In[111]:


df2.head()


# In[112]:


df2.plot.bar(stacked=True)


# In[113]:


df2.plot.barh(stacked=True)


# In[114]:


df1.head(9).plot.line(y='A',figsize=(10,4))


# In[115]:


df2.plot.line(y='a',figsize=(12,3),lw=2);


# In[118]:


df2.plot.line(y=['a','b','c'],figsize=(12,3),lw=2);


# In[116]:


df4 = pd.read_csv('example.csv')


# In[117]:


df4.head()


# In[100]:


df4.plot.area(alpha=0.4)


# In[101]:


df4.plot.area(stacked=False,alpha=0.4)


# In[102]:


df1.plot.scatter(x='A',y='B',c='D',cmap='coolwarm')


# In[103]:


df1.plot.scatter(x='A',y='B',s=df1['C']*25,c='D',cmap='tab10',alpha=0.5)


# In[119]:


df2.plot.box()


# In[120]:


df2.boxplot()


# In[121]:


df2.head()


# In[122]:


df2['a'].plot.kde()


# In[123]:


df2.plot.kde()


# In[126]:


import numpy as np
df = pd.DataFrame(np.random.randn(1000,2),columns=['a','b'])


# In[128]:


df.head()


# In[129]:


df.plot.scatter(x='a',y='b')


# In[139]:


df.plot.hexbin(x='a',y='b',gridsize=40,cmap='jet')


# In[ ]:




