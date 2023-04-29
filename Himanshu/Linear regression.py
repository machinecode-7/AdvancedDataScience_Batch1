#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


from sklearn.linear_model import LinearRegression


# In[4]:


feature3 = np.array([1,2,3,4,5,6,7,8,9])
target3 = np.array([75, 112, 149, 186, 223, 260, 297, 334, 371])


# In[5]:


type(feature3)


# In[6]:


feature3.shape


# In[9]:


feature3.reshape(-1,1)


# In[10]:


lreg = LinearRegression()


# In[15]:


lreg.fit(feature3.reshape(-1,1), target3)


# In[16]:


lreg.predict([[10]])


# In[19]:


m = lreg.coef_


# In[22]:


m


# In[20]:


c = lreg.intercept_


# In[21]:


c


# In[27]:





# In[47]:


import seaborn as sns


# In[24]:


import pandas as pd


# In[25]:


feature3 = np.array([1,2,3,4,5,6,7,8,9])
target3 = np.array([75, 112, 149, 186, 223, 260, 297, 334, 371])


# In[36]:


data_dict = {
    "feature": np.array([1,2,3,4,5,6,7,8,9]),
    "target": target3
}


# In[38]:


df = pd.DataFrame(data_dict)


# In[44]:


df


# In[48]:


sns.scatterplot(df,x='feature',y='target')


# In[ ]:




