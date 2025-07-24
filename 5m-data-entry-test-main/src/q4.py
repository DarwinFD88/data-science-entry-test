#!/usr/bin/env python
# coding: utf-8

# In[11]:


def string_reverse(s):
    #First I want to check if input for 's' is a string
    if type(s) == str:
    #If 's' is indeed a string, then I want to return 's' in reverse by slicing that starts from the end of the string; moves backward by -1 step
        return s[::-1]
    else:
    #If 's' is not a string; I want to print a message saying that 's' is not a string
        print('This is not a string')


# In[12]:


string_reverse("Hello World")


# In[13]:


string_reverse("Python")


# In[ ]:




