#!/usr/bin/env python
# coding: utf-8

# In[78]:


import pandas as pd
import numpy as np
import csv


# In[79]:


#uploading & joining datasets
df1=pd.read_csv('Dongsi.csv')
df2=pd.read_csv('Changping.csv')
df3=pd.read_csv('Guanyuan.csv')
df4=df1.append(df2)
df5=df4.append(df3)


# In[80]:


#exporting joined raw dataset
df5.to_csv('Beijing.csv', index = False)


# In[81]:


#selecting variables of interests (subsetting columns)
df6=df5[["station","year","month","day", "hour", "PM2.5", "PM10", "NO2", "O3"]]


# In[82]:


#filtering 2017 data only (subsetting rows)
df7=df6[df6["year"] == 2017]


# In[83]:


#dropping & checking sum of missing values
df8=df7.dropna()
df8.isnull().sum()


# In[84]:


#Checking duplication
duplicateRowsDF = df8[df8.duplicated()]
print(duplicateRowsDF)


# In[85]:


#cleaning the dates
cols=["day","month","year"]
df8['date'] = df8[cols].apply(lambda x: '/'.join(x.values.astype(str)), axis="columns")
#df8['date']=pd.to_datetime(df8['date'])
df8.dtypes


# In[86]:


#Exporting cleaned data for integration
df8=df8[["date","hour","station","PM2.5", "NO2", "O3", "PM10"]]
df8.to_csv('Beijing_cleaned.csv', index = False)


# In[65]:


#Maximum value of PM2.5 in at 2AM
df9=df8[["hour","PM2.5"]]
df10=df9[df9["hour"] < 2]
df11=df10["PM2.5"].max(axis = 0)
print("Maximum value of PM2.5 at 2 AM: ", df11)


# In[66]:


#Average NO2 at 10 AM 2017 in Dongsi
df12=df8[["hour","NO2"]]
df13=df8[(df8["hour"] == 10) & (df8["station"] =="Dongsi") ]
df14=df13["NO2"].mean(axis = 0)
print("Average NO2 at 10 AM in Dongsi: ", round(df14,2))

