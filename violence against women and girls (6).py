#!/usr/bin/env python
# coding: utf-8

# In[4]:


#for manipulation
import pandas as pd
import numpy as np
#for visualization
import matplotlib.pyplot as plt
import seaborn as sns
from ipywidgets import interact
import plotly.express    as px


# # Data Loading,Storage.

# In[5]:


#Lets read the dataset
data=pd.read_csv('dataset.zip')
data.count()


# In[6]:


data.head(5)


# In[7]:


data.tail(5)


# In[8]:


#Lets check the shape of the dataset
print("shape of the dataset:",data.shape)


# In[9]:


#lets check the dimension of dataframe
print("dimension of dataset:",data.ndim)


# In[10]:


print("size of dataset:",data.size)


# In[11]:


type(data)


# In[12]:


#column type
type(data['Country'])


# In[13]:


#if we acces the single column by there name
data['Gender'] 


# In[14]:


data.iloc[0:3]


# In[15]:


data.axes


# In[16]:


#attribute style (it have some restriction)
data.Country


# In[17]:


data.values   #dataframe as 2D array


# In[18]:


data.Country.unique()


# In[19]:


data['Country'].unique()


# In[20]:


data.Question.unique()


# In[21]:


data['Demographics Question'].unique().tolist()


# In[22]:


data[data.Gender=='F']


# In[23]:


data[data.Gender=='M']


#  # Data Cleaning

# In[24]:


data.info()


# In[25]:


#Check Duplicates
data.duplicated().sum()


# In[26]:


# lets check if there is any missing value in the dataset
data.isna()


# In[27]:


data.isnull().sum()


# In[28]:


dn = pd.DataFrame({
    'Unique':data.nunique(),
    'Null':data.isna().sum(),
    'NullPercent':data.isna().sum() / len(data),
    'Type':data.dtypes.values
})
print(dn)


# In[29]:


#DROP ROWs
dn=data.dropna()
dn


# In[30]:


dn.isna()


# In[31]:


dn.isnull().sum()


# #   Mean,Median.

# In[32]:


demographics_dn = dn.groupby(["Demographics Question", "Demographics Response"])["Value"].agg(["median", "max", "min", "mean"]).reset_index()
demographics_dn.columns = ["Question", "Response", "Median", "Max", "Min", "Mean"]
print("Violence % median, min, max, and mean per demographic group")
demographics_dn.sort_values(["Question", "Median"])


# # Data Visualization

# In[33]:


sns.catplot(
    data=dn, y="Country", x="Value",
    kind="bar", height=12,aspect=.6,errorbar=None,
)


# In[34]:


g = sns.catplot(x='Demographics Response',y='Value',col='Gender',hue='Question',
                order=['No education','Primary','Secondary','Higher'],
                data=dn,kind='bar',errorbar=None)
g.set_axis_labels('Education Level','Percentage (%)')
g.fig.suptitle('India agreeing a husband is justified in hitting his wife',y=1.05)


# In[35]:


g = sns.catplot(x='Gender',y='Value',
                data=dn,kind='bar',errorbar=None)
g.set_axis_labels('Gender','Percentage (%)')
g.fig.suptitle(' a husband is justified in hitting his wife',y=1.05)


# In[36]:


g = sns.catplot(x='Question',y='Value',data=dn,kind='bar',errorbar=None, height=4,
    aspect=1,)
g.set_axis_labels('Questions Asked','Percentage (%)',)
g.fig.suptitle('A husband is justified in hitting his wife',y=1.05)
plt.xticks(rotation=90);


# In[38]:


g = sns.catplot(x='Demographics Response',y='Value',
                order=['No education','Primary','Secondary','Higher'],
                data=dn,kind='bar',errorbar=None)
g.set_axis_labels('Education Level','Percentage (%)')
g.fig.suptitle('A husband is justified in hitting his wife',y=1.05)


# In[40]:


g = sns.catplot(x='Demographics Response',y='Value',
                order=['No education','Higher'],
                data=dn,kind='bar',errorbar=None)
g.set_axis_labels('Education Level','Percentage (%)')
g.fig.suptitle('A husband is justified in hitting his wife',y=1.05)


# In[50]:


g = sns.catplot(x='Demographics Response',y='Value',
                order=['Employed for cash','Unemployed','Employed for kind'],aspect=.9,
                data=dn,kind='bar',errorbar=None)
g.set_axis_labels('Employment','Percentage (%)')
g.fig.suptitle('Indian agreeing a husband is justified in hitting his wife',y=1.05)


# # INDIA

# In[51]:


India = dn[dn.Country == 'India']
India.head()


# In[52]:


graph = India[(India['Demographics Question'] == 'Age')]

g = sns.catplot(x='Demographics Response',y='Value',col="Gender",aspect=.6,
                data=graph,kind='bar',errorbar=None)
g.set_axis_labels('Age','Percentage (%)')
g.fig.suptitle('Indian  agreeing a husband is justified in hitting his wife',y=1.05)


# In[53]:


graph = India[(India['Demographics Question'] == 'Employment')]

g = sns.catplot(x='Demographics Response',y='Value',col="Gender",
                order=['Employed for cash','Employed for kind','Unemployed'],aspect=.9,
                data=graph,kind='bar',errorbar=None)
g.set_axis_labels('Employment','Percentage (%)')
g.fig.suptitle('Indian agreeing a husband is justified in hitting his wife',y=1.05)


# In[54]:


graph = India[India['Demographics Question'] == 'Age']

g = sns.catplot(x='Demographics Response',y='Value',col='Gender',hue='Question',
                order=['15-24','25-34','35-49'],
                data=graph,kind='bar',errorbar=None)
g.set_axis_labels('Age','Percentage (%)')
g.fig.suptitle('India agreeing a husband is justified in hitting his wife',y=1.05)


# In[55]:


graph = India[India['Demographics Question'] == 'Education']

g = sns.catplot(x='Demographics Response',y='Value',col='Gender',hue='Question',
                order=['No education','Primary','Secondary','Higher'],
                data=graph,kind='bar',errorbar=None)
g.set_axis_labels('Education Level','Percentage (%)')
g.fig.suptitle('India agreeing a husband is justified in hitting his wife',y=1.05)


# In[56]:


graph = India[(India['Demographics Question'] == 'Education')]

g = sns.catplot(x='Demographics Response',y='Value',col="Gender",
                order=['Higher','No education',],aspect=.9,
                data=graph,kind='bar',errorbar=None)
g.set_axis_labels('Education','Percentage (%)')
g.fig.suptitle('Indian agreeing a husband is justified in hitting his wife',y=1.05)


# In[57]:


graph = India[(India['Demographics Question'] == 'Employment')]

g = sns.catplot(x='Demographics Response',y='Value',col="Gender",
                order=['Employed for cash','Unemployed'],aspect=.9,
                data=graph,kind='bar',errorbar=None)
g.set_axis_labels('Employment','Percentage (%)')
g.fig.suptitle('Indian agreeing a husband is justified in hitting his wife',y=1.05)


# In[58]:


graph = India[(India['Demographics Question'] == 'Residence')]

g = sns.catplot(x='Demographics Response',y='Value',col="Gender",
                order=['Rural','Urban'],aspect=.9,
                data=graph,kind='bar',errorbar=None)
g.set_axis_labels('Residence','Percentage (%)')
g.fig.suptitle('Indian agreeing a husband is justified in hitting his wife',y=1.05)


# In[59]:


graph = India[(India['Demographics Question'] == 'Marital status')]

g = sns.catplot(x='Demographics Response',y='Value',col="Gender",
                order=['Never married','Married or living together'],aspect=.9,
                data=graph,kind='bar',errorbar=None)
g.set_axis_labels('Marital status','Percentage (%)')
g.fig.suptitle('Indian agreeing a husband is justified in hitting his wife',y=1.05)


# In[60]:


dn['year'] = pd.DatetimeIndex(dn['Survey Year']).year
dn['year']
dn


# In[61]:


sns.lineplot(data=dn, x="year", y="Value",hue="Gender")
plt.xticks(rotation=10);


# In[62]:


@interact
def summary(vis= list(dn['Question'].value_counts().index)):
    x=dn[dn['Question']==vis]
    print("-------------------------------")
    print("Statistics for Violence")
    print("Minimum violence occured: ",x['Value'].min() )
    print("Average violence occured:",x['Value'].mean())
    print("Maximum violence occured:",x['Value'].max())


# In[63]:


@interact
def summary(vis= list(dn['Demographics Question'].value_counts().index)):
    x=dn[dn['Demographics Question']==vis]
    print("-------------------------------")
    print("Statistics for Violence")
    print("Minimum violence occured: ",x['Value'].min() )
    print("Average violence occured:",x['Value'].mean())
    print("Maximum violence occured:",x['Value'].max())


# In[64]:


@interact
def summary(vis= list(dn['Gender'].value_counts().index)):
    x=dn[dn['Gender']==vis]
    print("-------------------------------")
    print("Minimum violence occured: ",x['Value'].min() )
    print("Average violence occured:",x['Value'].mean())
    print("Maximum violence occured:",x['Value'].max())


# In[65]:


demographics_df = dn.groupby(["Demographics Question", "Demographics Response"])["Value"].agg(["median", "max", "min", "mean"]).reset_index()
demographics_df


# In[66]:


question_dn=dn.groupby(["Question"])["Value"].agg(["median","max","min","mean"]).reset_index()
question_dn


# In[67]:


dn['year']=pd.DatetimeIndex(dn["Survey Year"]).year
survey_dn=dn.groupby(["year"])["Value"].agg(["median","max","min","mean"]).reset_index()
survey_dn


# In[68]:


country_dn=dn.groupby(["Country"])["Value"].agg(["median","max","min","mean"]).reset_index()
country_dn.sort_values(['Country','max'])


# In[69]:


response_dn=dn.groupby(["Gender"])["Value"].agg(["median","max","min","mean"]).reset_index()
response_dn


# In[70]:


demoresponse_dn=dn.groupby(["Demographics Response"])["Value"].agg(["median","max","min","mean"]).reset_index()
demoresponse_dn


# In[71]:


female=India[India.Gender == 'F']
female


# In[72]:


arguing=female[female.Question == '... if she argues with him']
arguing


# In[73]:


dataframe_arg = arguing.groupby(["Demographics Response"])["Value"].agg(["mean"]).reset_index()
dataframe_arg


# In[74]:


burn=female[female.Question == '... if she burns the food']
burn


# In[75]:


dataframe_burn = burn.groupby(["Demographics Response"])["Value"].agg(["mean"]).reset_index()
dataframe_burn


# In[76]:


neglect=female[female.Question == '... if she neglects the children']
neglect


# In[77]:


dataframe_neglect = neglect.groupby(["Demographics Response"])["Value"].agg(["mean"]).reset_index()
dataframe_neglect


# In[78]:


goesout=female[female.Question == '... if she goes out without telling him']
goesout


# In[79]:


dataframe_goesout = goesout.groupby(["Demographics Response"])["Value"].agg(["mean"]).reset_index()
dataframe_goesout


# In[80]:


refuses=female[female.Question == '... if she refuses to have sex with him']
refuses


# In[81]:


dataframe_refuses = refuses.groupby(["Demographics Response"])["Value"].agg(["mean"]).reset_index()
dataframe_refuses


# In[82]:


specific=female[female.Question == '... for at least one specific reason']
specific


# In[83]:


dataframe_specific = specific.groupby(["Demographics Response"])["Value"].agg(["mean"]).reset_index()
dataframe_specific


# In[84]:


male=India[India.Gender == 'M']
male


# In[85]:


arguing1=male[male.Question == '... if she argues with him']
arguing1


# In[86]:


dataframe_arg1 = arguing1.groupby(["Demographics Response"])["Value"].agg(["mean"]).reset_index()
dataframe_arg1


# In[87]:


burn1=male[male.Question == '... if she burns the food']
dataframe_burn1 = burn1.groupby(["Demographics Response"])["Value"].agg(["mean"]).reset_index()
dataframe_burn1


# In[88]:


neglect1=male[male.Question == '... if she neglects the children']
dataframe_neglect1 = neglect1.groupby(["Demographics Response"])["Value"].agg(["mean"]).reset_index()
dataframe_neglect1


# In[89]:


goesout1=male[male.Question == '... if she goes out without telling him']
dataframe_goesout1 = goesout1.groupby(["Demographics Response"])["Value"].agg(["mean"]).reset_index()
dataframe_goesout1


# In[90]:


refuses1=male[male.Question == '... if she refuses to have sex with him']
dataframe_refuses1 = refuses1.groupby(["Demographics Response"])["Value"].agg(["mean"]).reset_index()


# In[91]:


dataframe_refuses1


# In[92]:


specific1=male[male.Question == '... for at least one specific reason']
dataframe_specific1 = specific1.groupby(["Demographics Response"])["Value"].agg(["mean"]).reset_index()
dataframe_specific1


# # Data Analysis

# a) 2018 was the year that recorded with the most agreed key questions that were asked
# 
# b) The country which had the highest % average of people who agreed with the key question was Eritrea with an average of 46.19%
# 
# c) The most agreeable question was that the husband is justified in beating his wife for at least one specific reason with the highest % average being in 2018 for females at 70.39% and males at 48.84%
# 
# d) We can also see that females have the highest % of responses compared to males across all key question this could be due to some socioeconomic factors affecting the communities across the world
# 
# e) In the demographic age we can also see that ages 15-24 has the highest % average of agreement with the key question husband is justified in beating his wife for at least one specific reason coming to 35.88% which is the highest across other age groups
# 
# f) In the demographic Education group we can see that for females those who have received no education agree to the key question that a husband is justified to beating his wife for at least one specific reason with a percentage of 45.45% compares to males in the same education category where there average % was 32.81%
# 
# g) In the demographic group of residence we see that those who live in rural areas have a highest % responses of the key question that husband is justified in beating his wife for at least one specific reason coming to 42.24% for both genders and the ones in urban at 30.94%

# # CONCLUSIONS FROM THE ANALYSIS

# b The key question that a husband is justified in hitting his wife for any reason has the highest % of agreed responses from both male and female, we can conclude this could be because of the social construct that a man is the head of the house so they do not need to explain themsleves when it comes to abuse or violence in their homes, the way forward is to start teaching equality in homes that a wife is as important in the household as a husband, changing the view of what is commonly known as household heirarchy
# 

# In[ ]:




