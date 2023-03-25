#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Imagine you are on a date :)
# You both mutually decide that..
#if *bill amount* is between 75$ to 100$ the girl will pay (print "girl" in this case)
#if bill amount is less than 25$ again girl will pay (print "girl" in this case)
#if bill amount is more than 150$ again girl will pay (print "girl" in this case)
#else the boy will pay. (print "boy" in this case)
# Completely hypothetical (we know who pays, right!!)
#Jokes apart, this question shall solidify your concept on Logical operators(And,Or) and Conditional Statements(if-elif-else)


# In[3]:


billamount=20


# In[4]:


if billamount>=75 and billamount<=100:
    print('Girl')
elif billamount<25:
    print('Girl')
elif billamount >=150:
    print('Girl')
else:
    print('Boy')


# In[ ]:




