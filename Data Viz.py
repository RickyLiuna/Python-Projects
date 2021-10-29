#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd
import matplotlib as plt
import csv
import matplotlib.pyplot as plt


# In[40]:


df=pd.read_csv('SDG_goal3_clean.csv')
df.head()


# In[70]:


#selecting variables of interests (subsetting columns)
df1=df[["Year","Region","Proportion of births attended by skilled health personnel (%)","Neonatal mortality rate (deaths per 1,000 live births)"]]


# In[71]:


df2=df1[df1["Year"]==2015]
df3=df2.groupby("Region")
df4=df3["Neonatal mortality rate (deaths per 1,000 live births)"].max()
last=df4.to_dict()
for keys in last:
  print("{} : {:.1F}".format(keys,last[keys]))


# In[72]:


df5=df1[df1["Region"]=='Africa']
df6=df5.groupby("Year")
df7=df6["Proportion of births attended by skilled health personnel (%)"].min()
#df7=df6["Neonatal mortality rate (deaths per 1,000 live births)"].max()
last2=df7.to_dict()
for keys in last2:
  print("{} : {:.1F}".format(keys,last2[keys]))


# In[73]:


print("Overall aggregate of Neonatal mortality rate accross 5 regions:",round(df4.agg("mean"),2))
print("Overall aggregate of Proportion of births attended by skilled health personnel in Africa for several years:",round(df7.agg("mean"),2))


# In[108]:


df8=df[["Year","Region",
        "Neonatal mortality rate (deaths per 1,000 live births)",
        "Infant mortality rate (deaths per 1,000 live births):::BOTHSEX",
        "Under-five mortality rate, by sex (deaths per 1,000 live births):::BOTHSEX"]]
df9=df8[df8["Year"]==2015]
df10=df9.groupby("Region")
df11=df10["Neonatal mortality rate (deaths per 1,000 live births)",
         "Infant mortality rate (deaths per 1,000 live births):::BOTHSEX",
         "Under-five mortality rate, by sex (deaths per 1,000 live births):::BOTHSEX"
        ].max()


# In[110]:


ax = df11.plot(kind="bar")
plt.title("HIghest Mortality rate among neonatal, infant & under five kid accross 5 different regions in 2015")
plt.ylabel("deaths per 1,000 live births")
plt.legend(["Neonatal", "Infant", "Under-five"], loc='center left', bbox_to_anchor=(1, 0.5))
plt.xticks(rotation=360, horizontalalignment="center")


# In[123]:


df12=df[["Year","Region",
        "Health worker density, by type of occupation (per 10,000 population)::PHYSICIAN",
        "Health worker density, by type of occupation (per 10,000 population)::NURSEMIDWIFE",
         "Proportion of births attended by skilled health personnel (%)"
        ]]
df13=df12[df12["Region"]=='Africa']
df14=df13.groupby("Year")
df15=df14["Health worker density, by type of occupation (per 10,000 population)::PHYSICIAN",
          "Health worker density, by type of occupation (per 10,000 population)::NURSEMIDWIFE",
          "Proportion of births attended by skilled health personnel (%)"
        ].agg("mean")


# In[125]:


ax2 = df15.plot(kind="line")
plt.title("Average Health Profesionals Available in Africa from 2005 to 2015")
plt.ylabel("Density and %")
plt.legend(["Physician", "Nurse", "Birth Attendees"], loc='center left', bbox_to_anchor=(1, 0.5))
plt.xticks(rotation=360, horizontalalignment="center")


# In[ ]:




