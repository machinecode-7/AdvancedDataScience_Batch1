#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv('diabetes_clean.csv')


# In[3]:


df


# In[4]:


from sklearn.linear_model import LogisticRegression


# In[5]:


#model initiate (storing model in a variable)
Logreg = LogisticRegression()


# In[6]:


type(df)


# In[7]:


type(df['pregnancies'])


# In[27]:


x = np.array(df['pregnancies']).reshape(-1,1)
y = df['diabetes']


# In[28]:


Logreg.fit(x,y)


# In[29]:


Logreg.predict([[8]])


# In[ ]:





# In[30]:


pregnancies = np.array(list(range(0,15))).reshape(-1,1)
predictions = Logreg.predict(pregnancies)


# In[31]:


data = {
    'pregnancies' : np.array(list(range(0,15))),
    'pred' : predictions
}


# In[32]:


pred_df = pd.DataFrame(data)


# In[33]:


import matplotlib.pyplot as plt


# In[34]:


plt.scatter(pred_df['pregnancies'], pred_df['pred'])


# In[17]:


sorted(df['glucose'].unique())



# In[18]:


x = np.array(df['glucose']).reshape(-1,1)
y = df['diabetes'] 


# In[19]:


Logreg.fit(x,y)


# In[20]:


glucose = np.array(list(range(0,200))).reshape(-1,1)
predictions = Logreg.predict(glucose)


# In[21]:


data = {
    'glucose' : np.array(list(range(0,200))),
    'pred' : predictions
}


# In[22]:


pred_df = pd.DataFrame(data)


# In[24]:


plt.scatter(pred_df['glucose'], pred_df['pred'])


# In[35]:


sorted(df['diastolic'].unique())


# In[36]:


x = np.array(df['diastolic']).reshape(-1,1)
y = df['diabetes'] 


# In[44]:


Logreg.fit(x,y)


# In[70]:


diastolic = np.array(list(range(0,123))).reshape(-1,1)
predictions = Logreg.predict(diastolic)


# In[71]:


data = {
    'diastolic' : np.array(list(range(0,123))),
    'pred' : predictions
}


# In[72]:


pred_df = pd.DataFrame(data)


# In[73]:


plt.scatter(pred_df['diastolic'], pred_df['pred'])


# In[49]:


sorted(df['triceps'].unique())


# In[50]:


x = np.array(df['triceps']).reshape(-1,1)
y = df['diabetes'] 


# In[60]:


Logreg.fit(x,y)


# In[74]:


triceps = np.array(list(range(0,100))).reshape(-1,1)
predictions = Logreg.predict(triceps)


# In[79]:


data = {
    'triceps' : np.array(list(range(0,100))),
    'pred' : predictions
}


# In[80]:


pred_df = pd.DataFrame(data)


# In[57]:


plt.scatter(pred_df['triceps'], pred_df['pred'])


# In[58]:


sorted(df['insulin'].unique())


# In[59]:


x = np.array(df['insulin']).reshape(-1,1)
y = df['diabetes'] 


# In[61]:


Logreg.fit(x,y)


# In[81]:


insulin = np.array(list(range(0,100))).reshape(-1,1)
predictions = Logreg.predict(insulin)


# In[82]:


data = {
    'insulin' : np.array(list(range(0,100))),
    'pred' : predictions
}


# In[83]:


pred_df = pd.DataFrame(data)


# In[84]:


plt.scatter(pred_df['insulin'], pred_df['pred'])


# In[85]:


sorted(df['bmi'].unique())


# In[67]:


x = np.array(df['bmi']).reshape(-1,1)
y = df['diabetes'] 


# In[68]:


Logreg.fit(x,y)


# In[86]:


bmi = np.array(list(range(0,68))).reshape(-1,1)
predictions = Logreg.predict(bmi)


# In[91]:


data = {
    'bmi' : np.array(list(range(0,68))),
    'pred' : predictions
}


# In[92]:


pred_df = pd.DataFrame(data)


# In[93]:


plt.scatter(pred_df['bmi'], pred_df['pred'])


# In[94]:


from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# In[95]:


x = df.iloc[:, :-1] 
y = df['diabetes']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.8, random_state=42)


# In[96]:


print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)


# In[100]:



logreg = LogisticRegression(max_iter = 300)

logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)


# In[101]:


accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


# In[ ]:




