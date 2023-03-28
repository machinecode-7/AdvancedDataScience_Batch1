#!/usr/bin/env python
# coding: utf-8

# ## Question 1

# In[1]:


# Take a value greater than 1 from user (You can put it in any variable)
# Print the sum of all numbers from 1 to that number
#for eg: num=3
#output should be 6 (since 1+2+3 is 6
#Try implementing it with *For* as well as *While* Loop


# In[5]:


N=6
sum=0
for i in range(0,N+1):
    sum += i
    print(sum)


# In[1]:


#Question 2
# Use a loop to display elements from a given list present at odd index positions
# my_list = [10,20,11,22,33,44,66,76,87,98,20,30,40,50,23,45,67,89]


# In[8]:


my_list = [10,20,11,22,33,44,66,76,87,98,20,30,40,50,23,45,67,89]


# In[4]:





# In[ ]:


#Question 3
#print pattern in the output as shown below, if the user input(or your variable value) is 4
*
**
***
****
***
**
*
# the variable value represents the max value of stars


# In[26]:


star = 5


# In[32]:


for i in range (0,star +1):
    print ("*" *i)
for i in range (star-1, 0, -1):
    print("*" *i)


# In[8]:


# concept: Factorial of 5 is 5*4*3*2*1 = 120
# Find the factorial of any number provided by user

N=8
sum=1
for i in range(1,N+1):
    sum *= i
    print(sum)


# In[6]:


#Question 5
# Display numbers from -10 to -1 using While and For Loop

for i in range(-10, 10):
    print(i)
    if i == -1:
        break


# In[ ]:




