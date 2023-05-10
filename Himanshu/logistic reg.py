#!/usr/bin/env python
# coding: utf-8

# In[112]:


import pandas as pd


# In[113]:


import numpy as np


# In[3]:


df = pd.read_csv('desktop/diabetes_clean.csv')


# In[4]:


df


# In[5]:


from sklearn.linear_model import LogisticRegression


# In[6]:


Logreg = LogisticRegression()


# In[7]:


type(df)


# In[8]:


type(df['pregnancies'])


# In[76]:


sorted(df['pregnancies'].unique())


# In[77]:


x = np.array(df['pregnancies']).reshape(-1,1)
y = df['diabetes'] 


# In[78]:


Logreg.fit(x,y)


# In[79]:


pregnancies = np.array(list(range(0,17))).reshape(-1,1)
predictions_on_pregnencies = Logreg.predict(pregnancies)


# In[80]:


data = {
    'pregnencies' : np.array(list(range(0,17))),
    'pred' : predictions_on_pregnencies
}


# In[81]:


pred_df = pd.DataFrame(data)


# In[147]:


import matplotlib.pyplot as plt


# In[83]:


plt.figure(figsize=(18,6))
plt.scatter(pred_df['pregnencies'], pred_df['pred'])


# In[23]:


df['pregnancies'].unique()


# In[24]:


## glucose


# In[25]:


sorted(df['glucose'].unique())


# In[26]:


Logreg = LogisticRegression()


# In[28]:


x = np.array(df['glucose']).reshape(-1,1)
y = df['diabetes'] 


# In[35]:


Logreg.fit(x,y)


# In[40]:


glucose = np.array(list(range(44,200))).reshape(-1,1)
predictions_on_glucose = Logreg.predict(glucose)


# In[41]:


data = {
    'glucose' : np.array(list(range(44,200))),
    'pred' : predictions_on_glucose
}


# In[42]:


data


# In[43]:


pred_df = pd.DataFrame(data)


# In[44]:


plt.figure(figsize=(18,6))
plt.scatter(pred_df['glucose'], pred_df['pred'])


# In[ ]:


##diastolic


# In[93]:


sorted(df['diastolic'].unique())


# In[94]:


x = np.array(df['diastolic']).reshape(-1,1)
y = df['diabetes'] 


# In[95]:


Logreg.fit(x,y)


# In[96]:


diastolic = np.array(list(range(24,122))).reshape(-1,1)
predictions_on_diastolic = Logreg.predict(diastolic)


# In[97]:


data = {
    'diastolic' : np.array(list(range(24,122))),
    'pred' : predictions_on_diastolic
}


# In[98]:


pred_df = pd.DataFrame(data)


# In[99]:


plt.figure(figsize=(18,6))
plt.scatter(pred_df['diastolic'], pred_df['pred'])


# In[ ]:


##triceps


# In[104]:


sorted(df['triceps'].unique())


# In[133]:


x = np.array(df['triceps']).reshape(-1,1)
y = df['diabetes']


# In[134]:


Logreg.fit(x,y)


# In[135]:


triceps = np.array(list(range(7,100))).reshape(-1,1)
predictions_on_triceps = Logreg.predict(triceps)


# In[136]:


data = {
    'triceps' : np.array(list(range(7,100))),
    'pred' : predictions_on_triceps
}


# In[137]:


pred_df = pd.DataFrame(data)


# In[138]:


plt.figure(figsize=(20,7))
plt.scatter(pred_df['triceps'], pred_df['pred'])


# In[139]:


##insulin


# In[149]:


import matplotlib.pyplot as plt


# In[150]:


sorted(df['insulin'].unique())


# In[151]:


x = np.array(df['insulin']).reshape(-1,1)
y = df['diabetes']


# In[152]:


Logreg.fit(x,y)


# In[153]:


insulin = np.array(list(range(14,846))).reshape(-1,1)
predictions_on_insulin = Logreg.predict(insulin)


# In[157]:


data = {
    'insulin' : np.array(list(range(14,846))),
    'pred' : predictions_on_insulin
}


# In[158]:


pred_df = pd.DataFrame(data)


# In[160]:


plt.figure(figsize=(18,6))
plt.scatter(pred_df['insulin'], pred_df['pred'])


# In[ ]:


##Bmi


# In[161]:


sorted(df['bmi'].unique())


# In[162]:


x = np.array(df['bmi']).reshape(-1,1)
y = df['diabetes']


# In[163]:


Logreg.fit(x,y)


# In[168]:


bmi = np.array(list(range(18,68))).reshape(-1,1)
predictions_on_bmi = Logreg.predict(bmi)


# In[169]:


data = {
    'bmi' : np.array(list(range(18,68))),
    'pred' : predictions_on_bmi
}


# In[170]:


pred_df = pd.DataFrame(data)


# In[171]:


plt.figure(figsize=(18,6))
plt.scatter(pred_df['bmi'], pred_df['pred'])


# In[ ]:





# In[172]:


df


# In[173]:


from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# In[183]:


x = df[["pregnancies","glucose","diastolic","triceps","insulin","bmi", 'age']]
y = df[["diabetes"]]


# In[187]:


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=52)


# In[188]:


print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)


# In[189]:


logreg = LogisticRegression(max_iter = 180)


# In[193]:


logreg.fit(X_train, y_train)


# In[194]:


y_pred = logreg.predict(X_test)


# In[195]:


accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


# In[ ]:




