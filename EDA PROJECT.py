#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
print('Libraries loaded sucessfully')


# In[2]:


#Loading dataset into DataFrame...for Analytical purpose

df = pd.read_csv('hotel_booking.csv')
print('Dataset loaded succesfully...!')


# In[3]:


#View top five rows from a dataframe
df.head()


# In[4]:


df.tail()


# In[5]:


#total no. of rows & columns
df.shape


# In[6]:


#to get column details
print(df.columns)


# In[7]:


#to find column details with nulls
df.info()


# In[8]:


#Changing type of 'reservation_status_date' column to datatime 
df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])


# In[9]:


df.info()


# In[10]:


df.describe(include = 'object')


# In[11]:


for col in df.describe(include = 'object').columns:
    print(col)
    print(df[col].unique())
    print('-'*50)


# In[12]:


#To fetch total null values in each column
df.isnull().sum()


# In[13]:


#deleting/droping multiple columns from a datafram
df.drop(['company','agent'],axis=1, inplace=True)
df.dropna(inplace = True)
print('company,agent column deleted successfully...!')


# In[14]:


#To fetch total null values in each column
df.isnull().sum()


# In[15]:


#To summarize the dataframe on 
df.describe()


# In[16]:


df['adr'].plot(kind = 'box')


# In[17]:


df = df[df['adr']<5000]


# In[18]:


canceled_perc = df['is_canceled'].value_counts(normalize=True)
print(canceled_perc)

plt.figure(figsize=(5,4))
plt.title('Reservation status count')
plt.bar(['Not canceled', 'Canceled'],df['is_canceled'].value_counts(), edgecolor='k', width=0.7)
plt.show()


# In[19]:


plt.figure(figsize = (8,4))
#df['is_canceled'] = df['is_canceled'].astype(str)
ax1 = sns.countplot(x = 'hotel', hue='is_canceled', data = df, palette='Blues')
legend_labels,_ = ax1. get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1,1))
plt.title('Reservation status in different hotels', size=20)
plt.xlabel('hotel')
plt.ylabel('no. of reservations')
plt.show()


# In[20]:


#Cancelation percentage ratio of 'City Hotel'
city_hotel_df = df[df['hotel']=='City Hotel']
city_hotel_df['is_canceled'].value_counts(normalize=True)


# In[21]:


#Cancelation percentage ratio of 'Resort Hotel'
resort_hotel_df = df[df['hotel']=='Resort Hotel']
resort_hotel_df['is_canceled'].value_counts(normalize=True)


# In[22]:


#finding mean of 'adr' using groupby 'reservation_status_date' column
resort_hotel_df = resort_hotel_df.groupby('reservation_status_date')[['adr']].mean()
resort_hotel_df


# In[23]:


#finding mean of 'adr' using groupby 'reservation_status_date' column
city_hotel_df = city_hotel_df.groupby('reservation_status_date')[['adr']].mean()
city_hotel_df


# In[24]:


plt.figure(figsize = (20,8))
plt.title('Average Daily Rate in City Hotel', fontsize=30)
plt.plot(resort_hotel_df.index,resort_hotel_df['adr'], label='Resort Hotel')
plt.plot(city_hotel_df.index,city_hotel_df['adr'], label='City Hotel')
plt.legend(fontsize = 20)
plt.show()


# In[25]:


#creating new column with name 'month' from column 'reservation_status_date' col value....
df['month'] = df['reservation_status_date'].dt.month


plt.figure(figsize=(16,8))
ax1 = sns.countplot(x = 'month', hue='is_canceled', data = df, palette='bright')
legend_labels,_ = ax1. get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1,1))
plt.title('Reservation status per month', size=20)
plt.xlabel('month')
plt.ylabel('number of reservation')
#plt.legend('not canceled','canceled')
plt.show()


# In[26]:


plt.figure(figsize = (12,6))
plt.title('ADR per month', fontsize=30)
sns.barplot(x ='month',y='adr', data=df[df['is_canceled']==1].groupby('month')[['adr']].sum().reset_index())
plt.legend(fontsize=20)
plt.show()


# In[27]:


#creating new dataframe with name 'canceled_data' which contains only canceled booking records
canceled_data = df[df['is_canceled']==1]

#creating new dataframe with name 'not canceled_data' which contains only not canceled booking records
not_canceled_data = df[df['is_canceled']==0]

top_10_country = canceled_data['country'].value_counts()[:10]
print(top_10_country)


plt.figure(figsize= (8,8))
plt.title('Top 10 countries with canceled reservation')
plt.pie(top_10_country, autopct = '%.2f', labels = top_10_country.index)


# In[28]:


df['market_segment'].value_counts()


# In[29]:


df['market_segment'].value_counts(normalize=True)


# In[30]:


print(canceled_data.shape)
print(canceled_data['market_segment'].value_counts())
canceled_data['market_segment'].value_counts(normalize=True)


# In[31]:


canceled_df_adr = canceled_data.groupby('reservation_status_date')[['adr']].mean()
canceled_df_adr.reset_index(inplace=True)
canceled_df_adr.sort_values('reservation_status_date', inplace = True)

not_canceled= df[df['is_canceled']==0]
not_canceled_df_adr = not_canceled_data.groupby('reservation_status_date')[['adr']].mean()
not_canceled_df_adr.reset_index(inplace=True)
not_canceled_df_adr.sort_values('reservation_status_date', inplace = True)

plt.figure(figsize =(20,6))
plt.title('Average Daily Rate')
plt.plot(not_canceled_df_adr['reservation_status_date'], not_canceled_df_adr['adr'], label='not canceled')
plt.plot(canceled_df_adr['reservation_status_date'], canceled_df_adr['adr'], label='canceled')
plt.legend()
plt.show()


# In[32]:


not_canceled_data = df[df['is_canceled']==0]
df


# In[ ]:




