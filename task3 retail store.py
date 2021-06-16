#!/usr/bin/env python
# coding: utf-8

# #      The Sparks Foundation (Graduate Rotational Internship Program)
# 

# #      Data Science& Business Analytics Tasks

# # Exploratory Data Analysis - Retail   (Level - Beginner) 
#          Author: Dhanya Vangalapudi

# In[2]:


get_ipython().system('pip install plotnine')


# In[3]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import plotnine as p9
from plotnine import *
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt


# # Data exploration

# In[4]:


data = pd.read_csv(r'C:\Users\dhany\Desktop\SampleSuperstore.csv')
data.head()


# In[5]:


data.info()


# In[6]:


data.describe()


# In[7]:


data.duplicated().sum()


# In[8]:


data.drop_duplicates(inplace = True)


# In[9]:


data.head()


# In[10]:


data.nunique()


# In[11]:


col=['Postal Code']
data=data.drop(columns=col,axis=1)
data


# In[14]:


data.corr()


# In[15]:


data.cov()


# # DATA ANALYSIS

# In[12]:


#To know the contribution of each segment
data["Segment"].value_counts()


# In[13]:


#Inorder to get percentage of each segment 
data["Segment"].value_counts()/len(data["Segment"])*100


# In[16]:


Z=(data["Segment"].value_counts()/len(data["Segment"])*100).plot(kind="bar",color="g")
Z


# In[17]:


plt.figure(figsize=(15,10))
plt.bar('Sub-Category','Category', data=data)
plt.title('Category vs Sub Category')
plt.xlabel('Sub-Catgory')
plt.ylabel('Category')
plt.xticks(rotation=45)
plt.show()


# In[81]:


sns.countplot(x=data["Segment"])
plt.title("Segment")
plt.xticks()
plt.show()
sns.countplot(x=data["Ship Mode"])
plt.title("Ship Mode")
plt.xticks(rotation=45)
plt.show()


# In[21]:


plt.figure(figsize=(25,10))
sns.countplot(x=data["State"])

plt.title("State",fontsize="15")
plt.xticks(rotation=45)
plt.show()


# In[22]:


data['State'].value_counts()


# California has more number of dealing
# wyoming has least number of dealings

# In[23]:


data["State"].value_counts().mean()


# In[24]:


data.hist(bins=50 ,figsize=(15,15))
plt.show()


# In[26]:


plt.figure(figsize=(10,4))
sns.lineplot('Discount','Profit', data=data , color='g',label='Discount')
plt.legend()
plt.show()


# In[27]:


Profit_plot = (ggplot(data, aes(x='Sub-Category', y='Profit', fill='Sub-Category')) + geom_col() + coord_flip()
+ scale_fill_brewer(type='div', palette="Spectral") + theme_classic() + ggtitle('Pie Chart'))

display(Profit_plot)


# In[80]:


sns.set(style="whitegrid")
plt.figure(2, figsize=(15,10))
sns.barplot(x='Sub-Category',y='Profit', data=data, palette='Spectral')
plt.suptitle(' Consumption Patterns in the United States', fontsize=16)
plt.show()


# In[29]:


ggplot(data, aes(x='Ship Mode', fill = 'Category')) + geom_bar(stat = 'count')


# In[30]:


#shipmode vs segment
fig, axs = plt.subplots(ncols =2,figsize=(20,15))
ax=sns.countplot(x="Ship Mode",hue="Region",data=data, ax=axs[0])
ax=sns.countplot(x="Ship Mode",hue="Segment",data=data, ax=axs[1])
ax[0].set_title("Ship Mode vs Region" ,fontsize=20)
ax[1].set_title("Ship Mode vs Segment" ,fontsize=20)
plt.show()


# In[31]:


plt.subplots(figsize=(20,15))
ax=sns.countplot(x="Quantity",hue="Ship Mode",data=data)
plt.title("Quantity vs Ship Mode " ,fontsize=20)

plt.show()


# In[32]:


#region
data["Region"].value_counts()


# In[33]:


fig, axs = plt.subplots(ncols =2,figsize=(20,15))
ax=sns.countplot(x="Region",hue="Category",data=data, ax=axs[0])
ax=sns.countplot(x="Region",hue="Sub-Category",data=data, ax=axs[1])
ax[0].set_title(" Region vs Category " ,fontsize=20)
ax[1].set_title(" Region vs Sub-Category" ,fontsize=20)
plt.show()


# #region vs segment and quatity

# In[74]:



fig, axs = plt.subplots(ncols =2,figsize=(15,15))
ax=sns.countplot(x="Region",hue="Segment",data=data, ax=axs[0])
ax=sns.countplot(x="Region",hue="Quantity",data=data, ax=axs[1])
ax[0].set_title(" Region vs Segment" ,fontsize=20)
ax[1].set_title(" Region vs Quantity" ,fontsize=20)
plt.show()


# # sales analysis citywise

# In[75]:



data1=data["City"].value_counts()
data1


# In[79]:


data["City"].value_counts().head(50).plot(kind="bar",figsize= (15,10),color="red")
plt.xlabel("Cities")
plt.ylabel("Frequency/Number of deals")
plt.title("city wise dealings",fontsize=20)
plt.show()


# In[34]:


data["City"].value_counts().mean()


# In[77]:


data1[data1<data["City"].value_counts().mean()].index#all this cities need to improve the number of dealings


# In[78]:


#list of cities
Citynames=list(data1[data1==1].index.values)
data1[data1==1]#total 70 citis have number of deals equal to 1


# # segment analysis of sales,discount and profit

# In[37]:



data["Segment"].value_counts()


# In[38]:


segment_data=data.groupby(["Segment"])[["Sales","Discount","Profit"]].mean()
segment_data


# In[39]:


plot=segment_data.plot(kind="pie", subplots=True,figsize=(15,15),autopct='%1.1f%%',labels=segment_data.index)


# # ship mode wise analysis of ssales ,discoutnt and profit

# In[40]:



data["Ship Mode"].value_counts()


# In[41]:


data_shipmode=data.groupby(["Ship Mode"])[["Sales","Discount","Profit"]].mean()


# In[42]:


plot=data_shipmode.plot(kind="pie", subplots=True,figsize=(15,15),autopct='%1.1f%%',labels=data_shipmode.index)
#discount AND PROFIT are high in ffirst class ship mode
#sales is more on same day ship mode


# # state wise analysis of sales ,discount and profit

# In[43]:



data["State"].value_counts()


# In[44]:


data_state=data.groupby(["State"])[["Sales","Discount","Profit"]].mean()
data_state


# In[45]:



plt.figure(figsize=(15,15))
plt.pie(data_state["Sales"],labels=data_state.index,autopct='%1.1f%%')
plt.title("state wise sales analysis",fontsize=20)
plt.legend()
plt.xticks(rotation=90)
plt.show()
#highest amount(i.e is 11.8%) of sales is in wyoming state
#the lowest amount (0.8%) of sales is in south dakota state


# In[46]:


data_state.sort_values("Profit")[["Profit"]].plot(kind="bar",figsize= (15,10),color="red")
plt.xlabel("states")
plt.ylabel("profit per sale")
plt.title("state wise profit analysis",fontsize=20)
plt.show()
#vermont at top
#ohio at the bottom


# In[47]:


data_state.sort_values("Discount")[["Discount"]].plot(kind="bar",figsize= (15,10),color="green")
plt.xlabel("states")
plt.ylabel("Discount per sale")
plt.title("state wise Discount analysis",fontsize=20)
plt.show()
#illinos at the top


# # city wise sales,discount,profit

# In[48]:



data_city=data.groupby(["State"])[["Sales","Discount","Profit"]].mean()
data_city=data_city.sort_values(["Profit"])
data_city


# In[49]:


data_city["Profit"].tail(20).plot(kind="bar",figsize=(15,10),color="blue")
plt.title("Top 20 cities cities with higher profits",fontsize=20)
plt.show()


# In[70]:


data_city["Profit"].head(20).plot(kind="bar",figsize=(15,10),color="green")
plt.title("Top 20 cities  with lowerprofits",fontsize=20)
plt.show()


# In[ ]:


from the above graphs, we can conclude that vemont city has higher profits
chio city has getting more losses.so inorder to get more dealings from ohio city and the cities which are getting losses need to 
update the items or other actors that are responsible for plant losses


# # Region wise sales discounts and profit analysis

# In[51]:



data_region=data.groupby(["Region"])[["Sales","Discount","Profit"]].mean()
data_region


# In[52]:


plot=data_region.plot(kind="pie", subplots=True,figsize=(15,15),autopct='%1.1f%%',labels=data_region.index)


# # category wise sales discounts and profit analysis

# In[53]:



data_category=data.groupby(["Category"])[["Sales","Discount","Profit"]].mean()
data_category


# In[54]:


plot=data_category.plot(kind="pie", subplots=True,figsize=(15,15),autopct='%1.1f%%',labels=data_category.index)


# # sub category wise sales, discounts and profit analysis

# In[55]:



data_subcategory=data.groupby(["Sub-Category"])[["Sales","Discount","Profit"]].mean()
data_subcategory


# In[56]:


plt.figure(figsize=(15,15))
plt.pie(data_subcategory["Sales"],labels=data_subcategory.index,autopct='%1.1f%%')
plt.title("Subcategory wise sales analysis",fontsize=20)
plt.legend()
plt.xticks(rotation=90)
plt.show()


# In[ ]:


1)maximun sales copiers
2)minimum sales fasteners


# In[65]:


#based on profit
data_subcategory.sort_values("Profit")[["Sales","Profit"]].plot(kind="bar",figsize= (15,10),label=["AVG SALES PRICE"])


# In[58]:


#BASED ON DISCOUNT
plt.figure(figsize=(15,15))
plt.pie(data_subcategory["Discount"],labels=data_subcategory.index,autopct='%1.1f%%')
plt.title("Subcategory wise Discount analysis",fontsize=20)
plt.legend()
plt.xticks(rotation=90)
plt.show()
#max discount is given on binders
#min discount i sgiven on labels


# # data_quantity wise analysis on sales ,discounts and profit

# In[59]:


data_quantity=data.groupby(["Quantity"])[["Sales","Discount","Profit"]].mean()
data_quantity["Discount"]=data_quantity["Discount"]*100
data_quantity


# In[60]:


#based on discount
plt.figure(figsize=(15,15))
plt.pie(data_quantity["Discount"],labels=data_quantity.index,autopct='%1.1f%%')
plt.title("Quantity wise Discount analysis",fontsize=20)
plt.legend()
plt.xticks(rotation=90)
plt.show()


# In[ ]:


1)Quantity 10 getting higher discount
2)Quantiy 14 getting lower discount


# In[61]:


#besed on sales
plt.figure(figsize=(15,15))
plt.pie(data_quantity["Sales"],labels=data_quantity.index,autopct='%1.1f%%')
plt.title("Quantity wise Sales analysis",fontsize=20)
plt.legend()
plt.xticks(rotation=90)
plt.show()


# In[ ]:


1)on an average 13 quanties are sold
2)minimum one item is getting sold


# In[62]:


#based on profit
plt.figure(figsize=(15,15))
plt.pie(data_quantity["Profit"],labels=data_quantity.index,autopct='%1.1f%%')
plt.title("Quantity wise Profit analysis",fontsize=20)
plt.legend()
plt.xticks(rotation=90)
plt.show()


# In[ ]:


1)when they  bought 13 quantities,we are getting higher profit.
2)when they bought 1 quantity we are getting lower profit.


# In[64]:


data_quantity.sort_values("Profit")[["Sales","Profit"]].plot(kind="bar",figsize= (15,10),label=["AVG SALES PRICE","Profit"])
plt.show()


# In[ ]:


1)we are getting more profit on technology items.so we can have varaties of technology objects in our retail.
2)Increasing the discounts on lowest selling objects like labels,fasteners and envelops.
3)Offering discounts on bulk objects purchase will book sales.

4)shuting down some retail shops in cities having a losses is a better option.


# In[ ]:





# In[ ]:





# In[ ]:




