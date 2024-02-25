#!/usr/bin/env python
# coding: utf-8

# # Working on real Project with Python

# # Weather Dataset

# The Weather Dataset is time series data set with per hour information about the weather condition at particular location.
# It records Temperature,Dew PointTemperature,Relative ,Humidity,Wind Speed,Visibility,Pressure and Weather Condition.

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("file.csv")


# In[3]:


#It shows first N rows in the data (by default N=5)
df.head(5)


# In[4]:


#shape()-It shows the total no. of rows and no. of columns of the dataframe
df.shape


# In[5]:


# index()-:The attribute provide the index of the dataframe
df.index


# In[6]:


# It shows the name of each column
df.columns


# In[7]:


# It shows the data type of each columns
df.dtypes


# In[8]:


# It a column, it shows all the unique value.It shows all the unique value.It can applied on a single column only,
# not on the whole dataframe
df['Weather'].unique()


# In[9]:


# It shows the total no. of non-null in each column.IT can be applied on a single column as well as on whole dataframe
df.nunique()


# In[10]:


# It shows the total no. of non-null in each column.It can be applied on a single column as well as on whole dataframe
df.count()


# In[11]:


# In a column,it shows all the uniw values with their count.It can be applied on single columns only
df['Weather'].value_counts()


# In[12]:


# Provide basic information about dataframes
df.info()


# # Find all the unique "Wind Speed" value in the data.

# In[13]:


df.head(2)


# In[14]:


df["Wind Speed_km/h"].nunique()


# In[15]:


df["Wind Speed_km/h"].unique()


# # Find the number of times when the weather is exactky clear

# In[16]:


df.head(2)


# In[17]:


df.Weather.value_counts()


# In[18]:


df[df['Weather']=="Clear"]


# In[19]:


df.groupby('Weather').get_group('Clear')


# 
# # Find the column number of when wind speed was exactly 4km/h  

# In[20]:


df.head(2)


# In[21]:


df[df["Wind Speed_km/h"]==4]


# # Find out all the Null values in the data

# In[22]:


df.head(2)


# In[23]:


df.isnull().sum()


# In[24]:


df.notnull().sum()


# # Rename the column name "Weather" of the dataframe to Weather Condition

# In[25]:


df.rename(columns={"Weather":"Weather Condition"},inplace=True)
df


# # what is the mean "Visibility"  

# In[26]:


df.head(2)


# In[27]:


df.Visibility_km.mean()


# # What is the standard deviation of "Pressure"

# In[28]:


df.head(2)


# In[29]:


df.Press_kPa.std()


# # What is the varience of "Relative Humidity"

# In[30]:


df["Rel Hum_%"].var()


# # Find all instance when "Snow" was recorded

# In[31]:


df["Weather Condition"].value_counts()


# In[32]:


df[df["Weather Condition"]=="Snow"]


# In[33]:


df[df["Weather Condition"].str.contains("Snow")]


# # Find all instance when "Wind speed" is above 24 and Visibility is 25

# In[34]:


df[(df["Wind Speed_km/h"]>24 )& (df["Visibility_km"]==25)]


# # What is the min  and max value of each column against each"Weather Condition"?

# In[35]:


df.groupby('Weather Condition').min()


# In[36]:


df.groupby('Weather Condition').max()


# # Show all the records where weather condition is fog

# In[37]:


df[df["Weather Condition"]=="Fog"]


# # Find all the instance when "weather is clear" or "visibility is above 40"

# In[38]:


df[(df["Weather Condition"]=="Clear") | (df["Visibility_km"]>40)]


# # Find all the instance when:

# Weather is clear and Relative Humidity is greater than 50
# or
# Visibility is above 40

# In[39]:


df[((df["Weather Condition"]=="Clear") & (df["Rel Hum_%"]>50) | (df["Visibility_km"]>40))]


# In[ ]:




