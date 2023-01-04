#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd


# In[8]:


df=pd.read_excel('Global Superstore.xlsx')


# In[9]:


df.info()


# In[10]:


df1 = pd.read_excel(df, 'Orders')
df2 = pd.read_excel(df, 'Return')


# In[ ]:


df.columns


# ## 2

# In[ ]:


pd.merge(df1, df2, on='Order_ID', how='inner') 


# In[ ]:





# In[ ]:





# ## 3

# In[ ]:


df.iloc[1:11,1:6]


# ## 4

# In[ ]:





# In[ ]:





# ## 5

# In[ ]:


df=df.rename(columns={'Sales': 'Revenue'})


# In[ ]:


df


# ## 6

# In[ ]:


df.Order_ID=df.Order_ID.astype(float) 
df.Quantity=df.Quantity.astype(float) 


# In[ ]:





# In[ ]:




