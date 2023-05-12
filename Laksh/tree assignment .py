#!/usr/bin/env python
# coding: utf-8

# In[59]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree


# In[2]:


data = pd.read_csv("iris.csv")


# In[4]:


data


# In[10]:


data.head()


# In[11]:


data.columns


# In[37]:


y = data['variety']


# In[38]:


from sklearn.preprocessing import LabelEncoder


# In[39]:


decode = LabelEncoder()


# In[40]:


decode.fit(y)


# In[41]:


target_new = decode.transform(y)


# In[46]:


target_new


# In[48]:


x = data[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']]
y = target_new


# In[49]:


x_train, x_test, y_train, y_test = train_test_split(x,y,random_state=36)


# In[50]:


x_train


# In[51]:


x_test


# In[52]:


dtf = DecisionTreeClassifier(max_depth=4)


# In[53]:


dtf.fit(x_train, y_train)


# In[54]:


y_pred = dtf.predict(x_test)


# In[55]:


accuracy_score(y_pred, y_test)*100


# In[56]:


for i in range(1,11):
    dtf = DecisionTreeClassifier(max_depth=i)
    dtf.fit(x_train, y_train)
    y_pred = dtf.predict(x_test)
    print(i , accuracy_score(y_pred, y_test))


# In[57]:


dtf.tree_.threshold


# In[58]:


dtf.tree_.feature


# In[60]:


tree.plot_tree(dtf)


# In[ ]:




