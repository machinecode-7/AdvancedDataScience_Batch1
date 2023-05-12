#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.tree import DecisionTreeClassifier


# In[2]:


from sklearn.model_selection import train_test_split


# In[3]:


import pandas as pd


# In[5]:


data = pd.read_csv('desktop/iris.csv')


# In[6]:


data.head()


# In[33]:


from sklearn.preprocessing import LabelEncoder


# In[7]:


data.columns


# In[9]:


x = data[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']]
y = data['variety']


# In[38]:


le = LabelEncoder()
y = le.fit_transform(y)


# In[39]:


print(y)


# In[40]:


varieties = le.inverse_transform(y)


# In[41]:


varieties_list = list(varieties)


# In[10]:


x_train, x_test, y_train, y_test = train_test_split(x,y)


# In[11]:


x_train


# In[12]:


x_test


# In[46]:


dtf = DecisionTreeClassifier(max_depth=3)


# In[47]:


dtf.fit(x_train, y_train)


# In[48]:


y_pred = dtf.predict(x_test)


# In[49]:


from sklearn.metrics import accuracy_score


# In[50]:


accuracy_score(y_pred, y_test)*100


# In[51]:


variety = data["variety"]


# In[52]:


import numpy as np


# In[53]:


for i in range(1,11):
    dtf = DecisionTreeClassifier(max_depth=i)
    dtf.fit(x_train, y_train)
    y_pred = dtf.predict(x_test)
    print(i , accuracy_score(y_pred, y_test))


# In[54]:


dtf.tree_.threshold


# In[55]:


from sklearn import tree


# In[45]:


tree.plot_tree(dtf)


# In[ ]:




