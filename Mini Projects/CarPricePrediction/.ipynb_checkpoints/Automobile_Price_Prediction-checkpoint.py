#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


header_names = ['Symbol', 'Norm-Losses', 'Make', 'Fuel', 'aspiration', 'doors', 'body-style', 'drive-wheels', 'engine-loc', 'wheel-base', 'length', 'width', 'height', 'curb-weight', 'engine-type', 'no_of_cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke', 'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']


# In[3]:


df = pd.read_csv('imports-85.data', sep=',', header=None, names=header_names, index_col=None, na_values='?')


# In[4]:


pd.set_option('display.max_columns', len(df.columns))


# In[5]:


df.head(3)


# In[6]:


df.isna().sum(axis=0).sum()
# Total NaN values in our DataFrame


# In[7]:


df.isna().sum(axis=0)


# In[8]:


# Removing the rows which have NaN values for price
df = df.loc[df['price'].isna() == False]


# In[9]:


# Engine-loc - boolean - front engine? Done
# Fuel - boolean - gas? Done
# parse doors into int Done
# parse no_of_cylinders to int Done
# Rename Fuel to Gas? Done


# In[10]:


# This was something new for me, something I might have forgot to use when needed
df['engine-loc'].replace(to_replace=['front', 'rear'], value=[True, False], inplace=True)


# In[11]:


# Symbol to int
df['Symbol'] = df['Symbol'].astype(int)


# In[12]:


df.loc[:,'doors'].loc[df['doors'].isna()] = 'four'


# In[13]:


df.loc[:, 'doors'].replace(['four', 'two'], [4, 2], inplace=True)


# In[14]:


df.loc[:, 'Fuel'].replace(['gas', 'diesel'], [1, 0], inplace=True)


# In[15]:


df['no_of_cylinders'].value_counts()
# df['no_of_cylinders'].isna().sum()


# In[16]:


num_cylinders = {'four': 4, 'six': 6, 'five': 5, 'two': 2, 'three': 3, 'twelve': 12}
df.replace({'no_of_cylinders': num_cylinders}, inplace=True)


# In[17]:


# df['aspiration'].isna().sum()
df['aspiration'].value_counts()
df.loc[:, 'aspiration'].replace(['std', 'turbo'], [0, 1], inplace=True)


# In[18]:


import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[19]:


dropped_df = df.drop(['engine-size'], axis=1)


# In[20]:


# I am dropping compression ratio because particularly, petrol cars have lesser compression-ratio as 
# compared to diesel cars because of the presence of a spark plug. More on wikipedia and can also be shown here

fig, axs = plt.subplots(1,2, figsize=(12, 6), sharey=True)
axs[0].set_title('Gas Vehicles')
axs[1].set_title('Diesel Vehicles')
sns.boxplot(ax=axs[0], y=dropped_df['compression-ratio'][dropped_df['Fuel']==1], palette='rainbow')
sns.boxplot(ax=axs[1], y=dropped_df['compression-ratio'][dropped_df['Fuel']==0], palette='Set1')

# Because of this high correlation between gas-diesel and compression-ratio we can drop it


# In[21]:


dropped_df = df.drop(['engine-size', 'compression-ratio'], axis=1)


# In[22]:


# df
(dropped_df[['length', 'width', 'height', 'curb-weight', 'wheel-base']].corr())
# As shown there is a strong positive correlation between wheel-base and length
# As shown there is a strong positive correlation between length and width
# As shown there is a strong positive correlation between length and curb-weight and width

# So length, width, curb-weight and wheel-base share a strong positive correlation and is actually obvious

# Let's drop wheel-base and curb-weight
dropped_df.drop('wheel-base', inplace=True, axis=1)


# In[23]:


dropped_df.drop('curb-weight', axis=1, inplace=True)


# In[24]:


dropped_df['horsepower'].quantile(0.75)


# In[ ]:





# In[25]:


dropped_df


# In[26]:


cols = ['Symbol', 'Norm-Losses', 'Make', 'Gas?', 'std?', 'doors', 'body-style', 'drive-wheels', 'front-engine?', 'length', 'width', 'height', 'engine-type', '#cylinders', 'fuel-system', 'bore', 'stroke', 'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']


# In[33]:


dropped_df.rename(columns={'bore': 'bore_stroke_ratio'}, inplace=True)


# In[39]:


dropped_df['bore_stroke_ratio'] = dropped_df['bore_stroke_ratio']/dropped_df['stroke']


# In[41]:


dropped_df.drop('stroke', axis=1, inplace=True)


# In[42]:


# fuel_system categorical data
# horsepower classify
# peak rpm
# mpg

