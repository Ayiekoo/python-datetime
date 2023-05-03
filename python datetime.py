#!/usr/bin/env python
# coding: utf-8

# In[3]:


######## import datatime

import datetime
today = datetime.datetime.now()
print(today)


# In[5]:


today = datetime.datetime.now()
print(today.strftime("%B")) # Gives the month full name


# In[6]:


######## %Y - return year full form, e. g 2022
today = datetime.datetime.now()
print(today.strftime("%Y")) # Gives the year full name


# In[9]:


######## %b - returns month short form, e. g Dec
month = datetime.datetime.now()
print(month.strftime("%b")) # returns month short form


# In[10]:


######## %d - returns the day of the month, e. g 04
day = datetime.datetime.now()
print(day.strftime("%d")) # returns the day of the month


# In[11]:


######## %A - returns weekday, e. g Tuesday
weekday = datetime.datetime.now()
print(weekday.strftime("%A")) # returns weekday


# In[ ]:




