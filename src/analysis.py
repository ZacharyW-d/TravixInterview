#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
import pandas as pd
import os
import datetime 
import re
import math
import copy 

from currency_formatter import Currency


# In[ ]:


# read in data

data_save = pd.read_csv('combined_data.csv')

data = data_save.copy()


# In[ ]:


# change bedrag to float

data.iloc[:,4] = Currency(data.iloc[:,4], 'euro').to_int()


# In[ ]:


# change order date to datetime

data.iloc[:,3] = pd.to_datetime(data.iloc[:,3], format='%d-%m-%Y')


# In[ ]:


# substract cancelled or changed orders within time range

data1 = data[data.iloc[:,15] != 'N']

start_date = '2013-12-14'
end_date = '2014-01-13'
data1 = data1[(data.iloc[:,3] >= start_date) & (data.iloc[:,3] <= end_date)]


# In[ ]:


# calculate avg by airline

airline_avg = data1.groupby('Luchtvaartmaatschappij')['Bedrag'].mean().reset_index().sort_values(by='Bedrag')


# In[ ]:


# calculate sum by airline

airline = data1.groupby('Luchtvaartmaatschappij')['Bedrag'].sum().reset_index()


# In[ ]:


# normalize sum by log

airline_log = [math.log(_+1) if _ >= 0 else -math.log(-_) for _ in airline.Bedrag]
airline['log'] = airline_log


# In[ ]:


airline = airline.sort_values(by='Bedrag').reset_index(drop=True)


# In[ ]:


# create plot of total bedrag

fig, ax = plt.subplots()
airline.iloc[:7,].plot.bar(x='Luchtvaartmaatschappij', y='Bedrag', ax=ax)
ax.text(6.6, -26069, 'average')
ax.axhline(y=-26069.407373737384, linestyle='--')
plt.title('Loss by Airline')


# In[ ]:


airline = airline.merge(airline_avg, on='Luchtvaartmaatschappij', how='left')


# In[ ]:


airline_ct = data1.groupby('Luchtvaartmaatschappij')['Bedrag'].count().reset_index().sort_values(by='Bedrag')


# In[ ]:


airline = airline.merge(airline_ct, on = 'Luchtvaartmaatschappij', how='left')


# In[ ]:


airline = airline.rename(columns={"Bedrag_x": "Bedrag_sum", "Bedrag_y": "Bedrag_avg", 'Bedrag': 'count'})


# In[ ]:


fig, ax = plt.subplots()
airline.iloc[:7,].plot.bar(x='Luchtvaartmaatschappij', y='Bedrag_avg', ax=ax)
ax.text(6.6, -1752.119029192125, 'average')
ax.axhline(y=-1752.119029192125, linestyle='--')
plt.title('Averge Loss per Order by Airline')


# In[ ]:


fig, ax = plt.subplots()
airline.iloc[:7,].plot.bar(x='Luchtvaartmaatschappij', y='rate', ax=ax)
ax.text(6.6, 0.02927120669056153, 'median')
ax.axhline(y=0.02927120669056153, linestyle='--')
plt.title('Change&Cancel Rate by Airline')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


# channel analysis (incomplete)


# In[ ]:


data1.groupby(['Boekingskanaal', 'Luchtvaartmaatschappij']).count()


# In[ ]:


channel_ = data1.groupby('Boekingskanaal')['index'].count().reset_index()


# In[ ]:


channel = data.groupby('Boekingskanaal')['index'].count().reset_index()


# In[ ]:


channel_comp = channel.merge(channel_, how='left', on='Boekingskanaal').fillna(0)


# In[ ]:


channel_comp['rate'] = channel_comp['index_y']/channel_comp['index_x']


# In[ ]:


channel_comp[channel_comp.rate > 0.05]


# In[ ]:





# In[ ]:




