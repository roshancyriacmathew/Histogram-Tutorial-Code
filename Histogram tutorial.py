#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import required libraries
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import style


# In[2]:


age_men = 25,11,68,18,27,28,15,43,58,63,43,65,51,36,33,26,23,35,49,58


# In[5]:


plt.hist(age_men, bins=5)


# In[7]:


bins =[10,20,30,40,50,60,70]
plt.hist(age_men, bins=bins, edgecolor='black')


# In[3]:


#adding style to the plot
style.use('ggplot')
#plotting the histogram
plt.hist(age_men, bins=10, edgecolor='black',
         color='blue', rwidth=0.9)
#plotting the xlabel
plt.xlabel('age of people')
#plotting the ylabel
plt.ylabel('number of people')
#plotting the title of the graph
plt.title('Age vs number of people')


# In[5]:


age_men = 25,11,68,18,27,28,15,43,58,63,43,65,51,36,33,26,23,35,49,58
age_women = 48,57,59,25,19,37,18,56,22,25,56,25,14,49,53,45,46,19,28,70


# In[10]:


#set the figure size
plt.figure(figsize=(10,7))
#add style to the plot
style.use('ggplot')
#plot the histogram
plt.hist([age_men, age_women], bins=10, 
         color=['blue', 'orange'], histtype='barstacked',
         rwidth=0.9, label=['men', 'women'])
#add xlabel, ylabel and title
plt.xlabel('age of people')
plt.ylabel('number of people')
plt.title('Age vs number of people')
plt.legend(loc='upper right')


# In[7]:


style.use('ggplot')
plt.figure(figsize=(10,7))
plt.hist(age_men, bins=10, color='blue',
         histtype='step', rwidth=0.8, label='Men')
plt.hist(age_women, bins=10, color='orange',
         histtype='step', rwidth=0.8, label = 'Women')
plt.xlabel('Age of people')
plt.ylabel('No. of people')
plt.title('Age vs number of people')
plt.legend(loc='upper right')


# In[8]:


style.use('ggplot')
plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
plt.hist(age_men, bins=10, color='blue',
         histtype='bar', rwidth=0.8)
plt.xlabel('age of men')
plt.ylabel('No of people')
plt.title('Age vs number of people')
plt.subplot(1,2,2)
plt.hist(age_women, bins=10, color='blue',
         histtype='bar', rwidth=0.8)
plt.xlabel('age of women')
plt.ylabel('No of people')
plt.title('Age vs number of people')


# In[27]:


plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
plt.hist(age_men, bins=10, color='blue', histtype='bar', rwidth=0.8)
plt.xlabel('age of men')
plt.ylabel('No of people')
plt.title('Age vs number of people')
plt.subplot(2,2,4)
plt.hist(age_women, bins=10, color='blue', histtype='bar', rwidth=0.8)
plt.xlabel('age of women')
plt.ylabel('No of people')
plt.title('Age vs number of people')


# In[28]:


import pandas as pd
import os
os.chdir(r'D:\visualizations\histogram')


# In[29]:


age_data = pd.read_csv('age_csv.csv')
age_data.head()


# In[30]:


plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
plt.hist(age_data.Mens_age, bins=10, color='blue', histtype='bar', rwidth=0.8)
plt.xlabel('age of men')
plt.ylabel('No of people')
plt.title('Age vs number of people')
plt.subplot(1,2,2)
plt.hist(age_data.Womens_age, bins=10, color='blue', histtype='bar', rwidth=0.8)
plt.xlabel('age of women')
plt.ylabel('No of people')
plt.title('Age vs number of people')


# In[31]:


plt.figure(figsize=(10,7))
plt.hist(age_data.Mens_age, bins=10, color='blue',histtype='step', rwidth=0.8, label='Men')
plt.hist(age_data.Womens_age, bins=10, color='orange',histtype='step', rwidth=0.8, label = 'Women')
plt.xlabel('Age of people')
plt.ylabel('No. of people')
plt.title('Age vs number of people')
plt.legend(loc='upper right')

