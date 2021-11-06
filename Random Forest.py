#!/usr/bin/env python
# coding: utf-8

# In[83]:


import pandas as pd
from math import sqrt
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


# In[84]:


df=pd.read_csv('SDG_goal3_clean.csv')

df=df[["Region",
       "Mortality rate attributed to cardiovascular disease, cancer, diabetes or chronic respiratory disease (probability):::BOTHSEX",
       "Suicide mortality rate, by sex (deaths per 100,000 population):::BOTHSEX",
       "Death rate due to road traffic injuries, by sex (per 100,000 population):::BOTHSEX",
       "Under-five mortality rate, by sex (deaths per 1,000 live births):::BOTHSEX"]]


# In[85]:


def region_to_numeric(y):
    if y=='Asia': return 0
    if y=='Europe': return 1
    if y=='Oceania': return 2
    if y=='Americas': return 3
    if y=='Africa': return 4


# In[86]:


df['region_num'] = df['Region'].apply(region_to_numeric)


# In[103]:



X=df[["Mortality rate attributed to cardiovascular disease, cancer, diabetes or chronic respiratory disease (probability):::BOTHSEX",
      "Suicide mortality rate, by sex (deaths per 100,000 population):::BOTHSEX",
      "Death rate due to road traffic injuries, by sex (per 100,000 population):::BOTHSEX",
      "Under-five mortality rate, by sex (deaths per 1,000 live births):::BOTHSEX"]]  # Features
y=df['region_num']  # Labels

# Split dataset into training set and test set: 70% training and 30% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


# In[104]:


#Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)


# In[105]:


# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))


# In[106]:


# Run the code to view the classification report metrics
report = classification_report(y_test, y_pred)
print(report)


# In[108]:


#Make a prediction for a single item, for example:

print('----- Sample case -----')
print("Disease Mortality Rate: 7")
print("Suicide Mortality Rate: 9")
print("Road Traffic Injuries Mortality Rate: 10")
print("Under-five Mortality Rate: 13")
print("Predicted Region:", clf.predict([[7,9 ,10 ,13]]))





