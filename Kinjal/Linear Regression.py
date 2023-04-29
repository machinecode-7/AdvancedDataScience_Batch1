#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


from sklearn.linear_model import LinearRegression


# In[3]:


feature = np.array([1,2,3,4,5,6,7,8,9])
target = np.array([2,4,6,8,10,12,14,16,18])


# In[4]:


type(feature)


# In[15]:


lreg = LinearRegression()


# In[28]:


feature3 = np.array([1,2,3,4,5,6,7,8,9])
target3 = np.array([75, 112, 149, 186, 223, 260, 297, 334, 371])


# In[19]:


feature3.reshape(-1,1)


# In[20]:


lreg.fit(feature3.reshape(-1,1), target3)


# In[22]:


lreg.coef_


# In[24]:


lreg.intercept_


# In[25]:


import seaborn as sns


# In[27]:


import pandas as pd


# In[34]:


data_dict = {
    "feature":np.array([1,2,3,4,5,6,7,8,9]),
    "target":target3
}


# In[35]:


df = pd.DataFrame(data_dict)


# In[36]:


df


# In[38]:


sns.scatterplot(df,x='feature', y='target')


# In[ ]:




