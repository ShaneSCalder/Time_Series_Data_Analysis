#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np


# In[6]:


df2 = pd.read_csv('df2.csv')


# In[7]:


df2


# In[13]:


df2['c'].plot(figsize=(20,6),ls=':',c='pink',lw='5')


# In[14]:


title = "My Plot title"
xlabel = 'My X data'
ylabel = 'My Y data'


# In[15]:


ax = df2['c'].plot(figsize=(10,5),ls=':',lw='4',c='pink',title=title)
ax.set(xlabel=xlabel,ylabel=ylabel)


# LOCATION CODE	LOCATION STRING
# 0	'best'
# 1	'upper right'
# 2	'upper left'
# 3	'lower left'
# 4	'lower right'
# 5	'right'
# 6	'center left'
# 7	'center right'
# 8	'lower center'
# 9	'upper center'
# 10	'center'

# In[16]:


#use to move legend loc = and a number from the list or string i.e. loc=3 for lower right
ax = df2.plot()
ax.legend(loc=0)


# In[23]:


ax = df2.plot()
ax.legend(loc=0, bbox_to_anchor=(1.0,0.32))


# In[ ]:




