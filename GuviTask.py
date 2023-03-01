#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')



# In[2]:


pip install xlrd


# In[3]:


df1 = pd.read_excel("/Users/sharanyakarthikeyan/Downloads/Data Analyst Task (4) (1).xls",sheet_name = 'Sales data')


# In[4]:


df1


# In[5]:


df2 = pd.read_excel('/Users/sharanyakarthikeyan/Downloads/Data Analyst Task (4) (1).xls', sheet_name ='Product-language')


# In[6]:


df2


# In[7]:


df1.isnull().sum()


# In[8]:


df1.describe()


# In[9]:


sales_data = df1.drop(['Coupon code','Payment Mode','Transaction Bank'], axis = 1)


# In[10]:


sales_data


# In[11]:


sales_data.dtypes


# In[12]:


sales_data['Payment Status'].value_counts()


# In[13]:


sales_data['Currency  Code'].value_counts()


# In[14]:


sales_data['Source'].value_counts()


# In[15]:


product_names = sales_data['Product Code'].value_counts()


# In[16]:


product_names


# In[17]:


df2.isnull().sum()


# In[18]:


df2.dtypes


# In[19]:


df2.describe()


# In[20]:


df2['Language'].value_counts()


# In[21]:


data = {"source":["Direct ","Influencer","Email ","Paid"]
       }
df = pd.DataFrame(data)
df.head()


# In[22]:


df_encoded = pd.get_dummies(df["source"])
df_encoded .head()


# In[23]:


sales_data


# In[32]:


train_data.head()


# In[33]:


train_data['Payment Status'].value_counts(normalize=True).plot(kind = 'bar', title = "Payment status")


# In[34]:


train_data['Source'].value_counts(normalize=True).plot(kind = 'bar', title = "Source")


# In[35]:


df2['Language'].value_counts(normalize=True).plot(kind = 'bar', title = "Language")


# In[36]:


#only 20% people have done the payment
#around 70% of the source are Direct
#English language products are sold more than 50%


# In[37]:


data_group = sales_data.groupby(['Product Code', 'Source', 'Product Amount with GST']).size().reset_index().rename(columns ={0:'sales_count'})


# In[38]:


data_group


# In[39]:


import matplotlib
matplotlib.rcParams['figure.figsize']=(12,6)
sns.barplot(x = 'Product Code',y = 'sales_count', data = data_group)


# In[44]:


pip install dython


# In[45]:



from dython.nominal import associations


# In[47]:


from dython.nominal import identify_nominal_columns
categorical_features=identify_nominal_columns(sales_data)
categorical_features


# In[48]:


complete_correlation= associations(sales_data, filename= 'complete_correlation.png', figsize=(10,10))


# In[ ]:




