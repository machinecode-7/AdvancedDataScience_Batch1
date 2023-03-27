#!/usr/bin/env python
# coding: utf-8

# # Assignment

# In[1]:


# concept before getting to question:
# How to get remainder when we are dividing any number by another
# for example: if we divide 12 by 3 the remainder is 0, and if we divide 7 by 2 the remainder is 1
# python has special operator to get remainders: "%"
#lets see some example


# In[3]:


print(12%3)
print(7%2)
print(17%7)


# In[28]:


#Question: In the range of 0 to 100, print the numbers that are divisible(remainder=0) by 5
#your code:
for i in range (0,101):
    if  i % 5 == 0:
        print(i)


# In[51]:


# print pattern as shown below:
*
**
***
****
*****
# ask input from user for number of lines in the pattern, above mentioned output is for input=5
#your code:


# In[44]:


for i in range (0,6):
    print ("*" *i)


# In[50]:


# print pattern as shown below:
1
22
333
4444
# ask input from user for number of lines in the pattern, above mentioned output is for input=4
#your code:
for i in range (1, 5):
    print(str(i)*i)


# In[ ]:




