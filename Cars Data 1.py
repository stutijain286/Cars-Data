#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
cars= pd.read_csv(r"C:\Users\ASUS\OneDrive\Documents\Python\DATA\Cars Data1.csv")
cars


# In[5]:


cars.shape


# In[6]:


null=cars.isnull()
null


# In[7]:


null.head(432)


# In[8]:


cars.count()


# In[15]:


cars.isnull().sum()


# In[10]:


cars["Cylinders"].fillna(cars["Cylinders"].mean(),inplace=True)


# In[11]:


cars


# In[13]:


cars["Horsepower"].fillna(cars["Horsepower"].mean(), inplace=True)


# In[14]:


cars["Make"].fillna("NAN",inplace=True)


# In[16]:


cars.head(2)


# In[19]:


cars.count()


# In[46]:


cars["Make"].value_counts()


# In[20]:


cars.fillna(cars.mean())


# In[21]:


cars=cars.fillna(cars.mean())


# In[22]:


cars.isnull().sum()


# In[57]:


cars[cars["Origin"].isin(["Asia","Europe"])]


# In[61]:


df= cars[(cars["Make"]=="Acura") & (cars["Origin"]==("Asia","Europe"))]
df


# In[1]:


df= cars[(cars["Make"]=="Acura") & (cars["Origin"]==(["Asia","Europe"]))]
df


# In[65]:


cars.head()


# In[98]:


d2=cars[~(cars["Weight"] > 4000)]
d2


# In[99]:


d2.shape


# In[106]:


cars.head(2)


# In[109]:


cars["MPG_City"] = cars["MPG_City"].apply(lambda x:x+3)


# In[110]:


cars


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




