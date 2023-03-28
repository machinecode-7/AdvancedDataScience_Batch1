#!/usr/bin/env python
# coding: utf-8

# question 1

# In[ ]:


# Take a value greater than 1 from user (You can put it in any variable)
# Print the sum of all numbers from 1 to that number
#for eg: num=3
#output should be 6 (since 1+2+3 is 6
#Try implementing it with *For* as well as *While* Loop


# In[28]:


x = 6
y = 0
for i in range(1,x+1):
    y += i
    print(y)


# In[ ]:


# Display numbers from -10 to -1 using While and For Loop


# In[4]:


k = -10
while k < 0:
    print(k)
    k = k + 1


# In[8]:


for i in range(-10,0):
    print(i)


# In[ ]:


# concept: Factorial of 5 is 5*4*3*2*1 = 120
# Find the factorial of any number provided by user


# In[3]:


x = 5
y = 1
for i in range(1,x+1):
    y *= i
    print(y)


# In[ ]:


#print pattern in the output as shown below, if the user input(or your variable value) is 4
*
**
***
****
***
**
*
# the variable value represents the max value of stars


# In[19]:


k=7
for i in range(0,k+1):
    print("*"*i)
for i in range(k-1,0,-1):
    print("*"*i)


# In[ ]:


Use a loop to display elements from a given list present at odd index positions
# my_list = [10,20,11,22,33,44,66,76,87,98,20,30,40,50,23,45,67,89]


# In[20]:


my_list = [10,20,11,22,33,44,66,76,87,98,20,30,40,50,23,45,67,89]


# In[ ]:




