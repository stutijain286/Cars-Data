#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
police = pd.read_csv(r"C:\Users\ASUS\OneDrive\Documents\Python\DATA\3. Police Data.csv")
police


# In[4]:


police.shape


# In[ ]:


police.


# In[5]:


police.count()


# In[6]:


police.describe()


# In[7]:


police.isnull()


# In[8]:


police.isnull().sum()


# In[10]:


police.drop(columns = "country_name", inplace = True)


# In[11]:


police


# In[13]:


police.drop(index= 4)


# In[15]:


police.drop(["stop_date","stop_time"],axis = 1)


# In[16]:


police.drop([1,2],axis = 0)


# In[6]:


police[police["violation"].isin(["Speeding"])]


# In[7]:


police[police.violation=="Speeding"]


# In[10]:


police[police["violation"].isin(["Speeding"])].driver_gender.value_counts()


# In[11]:


police[police.violation=="Speeding"].driver_gender.value_counts()


# In[12]:


police.violation


# In[16]:


police[["violation","driver_gender"]]


# In[17]:


police.head()


# In[23]:


police.groupby("driver_gender").search_conducted.sum()


# In[26]:


police.search_conducted.value_counts()


# In[27]:


police.groupby("driver_gender").sum()


# In[28]:


police.head()


# In[29]:


police.stop_duration.value_counts()


# In[33]:


police["stop_duration"] = police["stop_duration"].map({"0-15 Min":7.5,"16-30 Min":24,"30+ Min":45})
police["stop_duration"]


# In[34]:


police


# In[35]:


police["stop_duration"].mean()


# In[36]:


police["stop_outcome"].value_counts()


# In[37]:


police.head(2)


# In[43]:


police.groupby("violation").sum()


# In[44]:


police.groupby("violation").driver_age.describe()


# In[ ]:




