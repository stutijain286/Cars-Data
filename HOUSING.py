#!/usr/bin/env python
# coding: utf-8

# In[1]:


from __future__ import division, print_function, unicode_literals


# In[2]:


import os
import tarfile
import pandas as pd


# In[3]:


print(os.getcwd())


# In[4]:


from six.moves import urllib
import zipfile


# In[5]:


DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"


# In[6]:


def fetch_housing_data(housing_url= HOUSING_URL, housing_path= HOUSING_PATH):
    os.makedirs(housing_path, exist_ok=True)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(housing_path)
    housing_tgz.close()


# In[7]:


fetch_housing_data()


# In[8]:


import pandas as pd

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


# In[9]:


housing = load_housing_data()
housing.head()


# In[10]:


housing.info()


# In[11]:


housing["ocean_proximity"].value_counts()


# In[12]:


housing.describe()


# In[13]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
housing.hist(bins=50, color="g", figsize=(20,15))
plt.savefig("attribute_histogram_plots.png")
plt.show()


# In[16]:


import numpy as np
def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]


# In[24]:


train_set, test_set = split_train_test(housing, 0.2)
print(len(train_set), "train +", len(test_set), "test")


# In[ ]:




