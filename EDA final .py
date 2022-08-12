#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

from matplotlib.pyplot import figure
import plotly.graph_objects as go
from pandas.plotting import parallel_coordinates


# In[2]:


#importing the dataset
data=pd.read_csv("C:/Users/Mural/OneDrive/Desktop/data.csv")
data


# In[3]:


#data cleaning
data.isnull()


# ### Observation:
# 1.We examine the null values in the imported dataset in the order of Boolean values (true / false) in this data cleaning stage.The null values are represented as true.false is the inverse of true.
# 
# 

# In[4]:


data.isnull().sum()


# ### Observation:-
# 1.This phase determines if our data set contains any null values and counts the null values.
# 

# In[5]:


data.duplicated()


# ### Observation:-
# 1.We gather information on recurring data in this stage, which aids in the removal of duplicate copies.

# In[6]:


data.info()


# ### Observation:-
# 1.The info() method prints information about the DataFrame. The information contains the number of columns, column labels, column data types, memory usage, range index, and the number of cells in each column (non-null values).

# In[7]:


data.describe()


# ### Observation:-
# 1.The describe() method returns description of the data in the DataFrame.
# If the DataFrame contains numerical data, the description contains these information for each column count,mean,standard deviation,min,quartile,max.

# In[8]:


#line chart of prices over the years
labels=data['Year']
x=data['Year']
y1=data['April']
y2=data['May']
y3=data['June']
y4=data['July']
y5=data['August']
y6=data['September']
y7=data['October']
y8=data['November']
y9=data['December']
y10=data['January']
y11=data['February']
y12=data['March']
f = plt.figure()
f.set_figwidth(15)
f.set_figheight(8)
plt.plot(x,y1,label="April")
plt.plot(x,y2,label="May")
plt.plot(x,y3,label="June")
plt.plot(x,y4,label="July")
plt.plot(x,y5,label="August")
plt.plot(x,y6,label="September")
plt.plot(x,y7,label="October")
plt.plot(x,y8,label="November")
plt.plot(x,y9,label="December")
plt.plot(x,y10,label="January")
plt.plot(x,y11,label="February")
plt.plot(x,y12,label="March")
plt.xticks(x,labels,rotation=40)
plt.legend()
plt.title("Line chart of crude prices over the years",color="red")
plt.xlabel("Year",color="red")
plt.ylabel("price",color="red")
plt.show()


# ### Observation:-
# 1.line plot: we have detailed information on crude oil prices for the past 20 years in our data set, and we can use the line plot to demonstrate how the frequency of price increases or decreases over a given month in the year.

# In[9]:


#bar graph of imports and exports in dollars
x=data['Import_in($)']
y=data['Export ($)']
year=data['Year']
f = plt.figure()
f.set_figwidth(15)
f.set_figheight(8)
plt.barh(year,x,color="red",label="import")
plt.barh(year,y,color="black",label="export")
plt.xlabel("price in $",color="red")
plt.title("bar graph of import and exports in dollars ",color="blue")
plt.ylabel("year",color="red")
plt.legend()
plt.show()


# ### Observation:
# 1..We present categorical data as rectangular bars with proportional heights or lengths in a bar graph.
# In our data, we used a bar graph to compare imports and exports (in dollars) and showed them horizontally.
# It shows  imports outnumber than  exports.

# In[10]:


#bar graph of imports and exports in rupees
x=data['Import(Rs)']
y=data['Export(Rs)']
year=data['Year']
f = plt.figure()
f.set_figwidth(15)
f.set_figheight(8)
plt.barh(year,x,color="red",label="import")
plt.barh(year,y,color="black",label="export")
plt.xlabel("price in rs",color="red")
plt.title("bar graph of import and exports in rupees ",color="blue")
plt.ylabel("year",color="red")
plt.legend()
plt.show()


# ### observation: 
# 1.We presents  categorical data as rectangular bars with proportional heights or lengths in a bar graph.
# In our data, we used a bar graph to compare imports and exports (in rupees) and showed them horizontally.
# It demonstrates that imports outnumber exports.
# 

# In[11]:


data.plot(x="Year", y=["Import_in($)", "Export ($)","Import(Rs)","Export(Rs)"], 
        kind="bar",figsize=(15,8))

# Show

plt.show()


# ### observation :
# 1.

# In[12]:


#pie chart of average price over the years
fig = px.pie(data, values='Average', names='Year', title='average price over the years')
fig.show()


# ### observation:-
# 1.

# In[13]:


#box plot
y1=data['April']
y2=data['May']
y3=data['June']
y4=data['July']
y5=data['August']
y6=data['September']
y7=data['October']
y8=data['November']
y9=data['December']
y10=data['January']
y11=data['February']
y12=data['March']
y13=data['Average']
data1 = [y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13]
f = plt.figure()
f.set_figwidth(12)
f.set_figheight(7) 

plt.boxplot(data1,patch_artist=True)
plt.xlabel("year",color="red")
plt.ylabel("price",color="red")
x_ticks = [1,2,3,4,5,6,7,8,9,10,11,12,13]

x_labels = ['April','May','June','July','August','September','October','November','December','January','February','March','Average'] 
plt.xticks(ticks=x_ticks, labels=x_labels,rotation=40)
plt.title("boxplot of prices over the years",color='blue')
plt.show()


# ### observation:
# 1.A boxplot is a standardized way of displaying the distribution of data based on a five number summary (“minimum”, 
# first quartile (Q1), median, third quartile (Q3), and “maximum”). It can tell you about your outliers and what their values are. It can also tell you if your data is symmetrical, how tightly your data is grouped, and if and how your data is skewed.

# In[14]:


#histogram of oil consumption over the years
x=data['Oil_consumption']
y=data['Year']
f = plt.figure()
f.set_figwidth(15)
f.set_figheight(8)
plt.barh(y,x,color="red")
plt.title("bar graph of oilconsumption over the years",color='blue')
plt.xlabel("litres in metric tonnes",color="red")
plt.ylabel("years",color="red")


# ### observation:
# 1..We presents  categorical data as rectangular bars with proportional heights or lengths in a bar graph.
# In our data, we constructed a bar graph to show the yearly oil consumption.

# In[15]:


#waterfall chart
a=data['Year']
b=data['Average']
ig=waterfall_chart.plot(a,b)
ig.show()


# ### observation:
# Since we use the yearly average price in the water fall chart, excessive increments and decrements might cause the cumulative total to dip above and below the axis at various times. Between floating columns, intermediate subtotals can be added to the graph as entire columns.

# In[16]:


y1=data['April']
y2=data['May']
y3=data['June']
y4=data['July']
y5=data['August']
y6=data['September']
y7=data['October']
y8=data['November']
y9=data['December']
y10=data['January']
y11=data['February']
y12=data['March']
x=data['Average']
plt.rcParams.update({'figure.figsize':(10,8), 'figure.dpi':100})
plt.scatter(x, y1, label=f'april and average price of Correlation = {np.round(np.corrcoef(x,y1)[0,1], 2)}')
plt.scatter(x, y2, label=f'may and average price of Correlation = {np.round(np.corrcoef(x,y2)[0,1], 2)}')
plt.scatter(x, y3, label=f'june and average price of Correlation = {np.round(np.corrcoef(x,y3)[0,1], 2)}')
plt.scatter(x, y4, label=f'july and average price of Correlation = {np.round(np.corrcoef(x,y4)[0,1], 2)}')
plt.scatter(x, y5, label=f'august and average price of Correlation = {np.round(np.corrcoef(x,y5)[0,1], 2)}')
plt.scatter(x, y6, label=f'september and average price of Correlation = {np.round(np.corrcoef(x,y6)[0,1], 2)}')
plt.scatter(x, y7, label=f'october and average price of Correlation = {np.round(np.corrcoef(x,y7)[0,1], 2)}')
plt.scatter(x, y8, label=f'november and average price of Correlation = {np.round(np.corrcoef(x,y8)[0,1], 2)}')
plt.scatter(x, y9, label=f'december and average price of Correlation = {np.round(np.corrcoef(x,y9)[0,1], 2)}')
plt.scatter(x, y10, label=f'january and average price of Correlation = {np.round(np.corrcoef(x,y10)[0,1], 2)}')
plt.scatter(x, y11, label=f'february and average price of Correlation = {np.round(np.corrcoef(x,y11)[0,1], 2)}')
plt.scatter(x, y12, label=f'march and average price of Correlation = {np.round(np.corrcoef(x,y12)[0,1], 2)}')


plt.title('Scatterplot and Correlations of prices and average',color="blue")
plt.legend()
plt.show()


# ### observation:-
# 1.A scatterplot is a graph made up of data points that shows the relationship between two variables. We see a strong correlation between monthly prices and yearly average prices

# In[17]:


y1=data['April']
y2=data['May']
y3=data['June']
y4=data['July']
y5=data['August']
y6=data['September']
y7=data['October']
y8=data['November']
y9=data['December']
y10=data['January']
y11=data['February']
y12=data['March']
y13=data['Average']
x=data['Oil_consumption']
plt.rcParams.update({'figure.figsize':(15,8), 'figure.dpi':80})
plt.scatter(x, y1, label=f'April price and Oil consumption correlation = {np.round(np.corrcoef(x,y1)[0,1], 2)}')
plt.scatter(x, y2, label=f'May price and Oil consumption correlation = {np.round(np.corrcoef(x,y2)[0,1], 2)}')
plt.scatter(x, y3, label=f'JUne price and Oil consumption correlation = {np.round(np.corrcoef(x,y3)[0,1], 2)}')
plt.scatter(x, y4, label=f'July price and Oil consumption correlation = {np.round(np.corrcoef(x,y4)[0,1], 2)}')
plt.scatter(x, y5, label=f'August price and Oil consumption correlation = {np.round(np.corrcoef(x,y5)[0,1], 2)}')
plt.scatter(x, y6, label=f'September price and Oil consumption correlation = {np.round(np.corrcoef(x,y6)[0,1], 2)}')
plt.scatter(x, y7, label=f'October price and Oil consumption correlation = {np.round(np.corrcoef(x,y7)[0,1], 2)}')
plt.scatter(x, y8, label=f'November price and Oil consumption correlation = {np.round(np.corrcoef(x,y8)[0,1], 2)}')
plt.scatter(x, y9, label=f'December price and Oil consumption correlation = {np.round(np.corrcoef(x,y9)[0,1], 2)}')
plt.scatter(x, y10, label=f'January price and Oil consumption correlation = {np.round(np.corrcoef(x,y10)[0,1], 2)}')
plt.scatter(x, y11, label=f'February price and Oil consumption correlation = {np.round(np.corrcoef(x,y11)[0,1], 2)}')
plt.scatter(x, y12, label=f'March price and Oil consumption correlation = {np.round(np.corrcoef(x,y12)[0,1], 2)}')
plt.scatter(x, y13, label=f'Aerage price and Oil consumption correlation = {np.round(np.corrcoef(x,y12)[0,1], 2)}')


plt.title('Scatterplot and Correlations of prices and Oil consumption',color="blue")
plt.legend()
plt.show()


# ### observation:-
# 1.A scatterplot is a graph made up of data points that shows the relationship between two variables. We see a strong correlation between monthly crude oil prices and yearly crude oil consumption.

# In[18]:


#sunburst graph
ig =px.sunburst(
 data_frame = data,
 path=['Year','Oil_consumption'],
 values = 'Average',
 title="OIL CONSUMPTION FROM 2000-2021",
 color='Average',color_continuous_scale=px.colors.diverging.BrBG,
                    
)
ig.show()


# ### observation:-
# 1.The sunburst chart is ideal for displaying hierarchical data. Each level of the hierarchy is represented by one ring or circle with the innermost circle as the top of the hierarchy. In our data oil consumption over 20 years is represented in hierarchy manner .

# In[19]:


y1=data['April']
y2=data['May']
y3=data['June']
y4=data['July']
y5=data['August']
y6=data['September']
y7=data['October']
y8=data['November']
y9=data['December']
y10=data['January']
y11=data['February']
y12=data['March']
y13=data['Average']
data1 = [y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13]
months=['April','May','June','July','August','September','October','November','December','January','February','March','Average']
#year=['2000-01','2001-02','2002-03','2003-04','2004-05','2005-06','2006-07','2007-08','2008-09','2009-10','2010-11','2011-12','2012-13','2013-14','2014-15','2015-16','2016-17','2017-18','2018-19','2019-20','2020-21']

fig = px.imshow(data1,text_auto=True, aspect="auto",
                labels=dict(x="years", y="months", color="prices",),
                y=months,color_continuous_scale='Bluered_r'
               )



fig.update_layout(
    title='prices over the years',
    xaxis_nticks=36)

fig.show()


# ### observation:-
# 1.We use a heatmap to display monthly crude oil prices and yearly average prices in a graphical format, with values represented by colour.

# In[20]:


data.corr()


# ### observation:-
# 1.dataframe.corr() is used to find the pairwise correlation of all columns in the dataframe. Any na values are automatically excluded. For any non-numeric data type columns in the dataframe it is ignored.

# In[21]:


fig = px.imshow(data.corr(),text_auto=True, aspect="auto",
                labels=dict(color="correlation of prices"),
                color_continuous_scale='viridis'
               )
fig.update_layout(
    title='correlation of dependent and independent variables',
    xaxis_nticks=36)
fig.show()


# ### observation:-
# 1.After using dataframe.corr() to obtain the correlation values of dependent and independent variables. The values are shown graphically, with colour heatmaps representing the values.
# 

# In[22]:


#area chart
plt.fill_between(data['Oil_consumption'],data['Average'], color="blue", alpha=0.2)
plt.plot(data['Oil_consumption'],data['Average'], color="black", alpha=0.6)
plt.title("Area chart of average and oil consumption of over the years", loc="left",color="blue")
plt.xlabel("litres in metric tonnes")
plt.ylabel("prices in $")

plt.show()


# ### observation:-
# Area chart displays graphically quantitative data. It is based on the line chart.In our data we represents the oil consumption and average crude oil prices over 20 years. 

# In[23]:


fig = go.Figure()
fig.add_trace(go.Scatter(x=data['Import_in($)'], y=data['Export ($)'], fill='tozeroy'))

fig.show()


# ### observation:-
# Area chart displays graphically quantitative data. It is based on the line chart .In our data we  represents the imports and expots (in dollar)  over 20 years. 

# In[24]:


fig = go.Figure()
fig.add_trace(go.Scatter(x=data['Import(Rs)'], y=data['Export(Rs)'], fill='tozeroy')) 
fig.show()


# ### observation:-
# Area chart displays graphically quantitative data. It is based on the line chart.In our data we  represents the imports and expots (in rupees)  over 20 years. 

# In[25]:


#Analysis of the year 2011-14
k=data.iloc[11:15]
k


# 

# In[26]:


f = plt.figure()
f.set_figwidth(15)
f.set_figheight(8)
plt.plot(k['Year'], k['April'], color='g', label='April')
plt.plot(k['Year'], k['May'], color='r', label='May')
plt.plot(k['Year'],k['June'],color='b',label='June')
plt.plot(k['Year'], k['July'], color='c', label='April')
plt.plot(k['Year'], k['August'], color='k', label='August')
plt.plot(k['Year'],k['September'],color='m',label='September')
plt.plot(k['Year'],k['October'],color='y',label='October')
plt.plot(k['Year'], k['November'], color='c', label='November')
plt.plot(k['Year'], k['December'], color='r', label='December')
plt.plot(k['Year'],k['January'],color='g',label='January')
plt.plot(k['Year'],k['February'],color='b',label='February')
plt.plot(k['Year'],k['March'],color='y',label='March')
plt.plot(k['Year'], k['Average'], color='c', label='Average')
plt.title("LIne plot of prices",color='Blue')
plt.xlabel("Years",color='red')
plt.ylabel("prices",color='red')
plt.legend()
plt.show()


# ### observation :-
# 1.The line plot is used to show how the frequency of pricing increase or decreases over time ( 2011-2014 )

# In[27]:


#bar graph of imports and exports in dollars
k.plot(x="Year", y=["Import_in($)", "Export ($)","Import(Rs)","Export(Rs)"], 
        kind="bar",figsize=(10,4))

# Show

plt.show()


# In[28]:


#pie chart of average price over the years
fig = px.pie(k, values='Average', names='Year', title='average price over the years')
fig.show()


# ### observation:

# In[29]:


#comparison of Decades
before_10=data.iloc[0:10]
before_10


# In[30]:


after_10=data.iloc[11:21]
after_10


# In[31]:


labels=before_10['Year']
x=before_10['Year']
y1=before_10['April']
y2=before_10['May']
y3=before_10['June']
y4=before_10['July']
y5=before_10['August']
y6=before_10['September']
y7=before_10['October']
y8=before_10['November']
y9=before_10['December']
y10=before_10['January']
y11=before_10['February']
y12=before_10['March']
f = plt.figure()
f.set_figwidth(15)
f.set_figheight(8)
plt.plot(x,y1,label="April")
plt.plot(x,y2,label="May")
plt.plot(x,y3,label="June")
plt.plot(x,y4,label="July")
plt.plot(x,y5,label="August")
plt.plot(x,y6,label="September")
plt.plot(x,y7,label="October")
plt.plot(x,y8,label="November")
plt.plot(x,y9,label="December")
plt.plot(x,y10,label="January")
plt.plot(x,y11,label="February")
plt.plot(x,y12,label="March")
plt.xticks(x,labels,rotation=40)
plt.legend()
plt.title("Line chart of crude prices from the 2000-2010",color="red")
plt.xlabel("Year",color="red")
plt.ylabel("price",color="red")
plt.show()


# ### observation:-
# 1.The line plot is used to show how the frequency of pricing increase or decreases over 10 years .we can clearly state there is increase in prices 2008-2009.

# In[32]:


labels=after_10['Year']
x=after_10['Year']
y1=after_10['April']
y2=after_10['May']
y3=after_10['June']
y4=after_10['July']
y5=after_10['August']
y6=after_10['September']
y7=after_10['October']
y8=after_10['November']
y9=after_10['December']
y10=after_10['January']
y11=after_10['February']
y12=after_10['March']
f = plt.figure()
f.set_figwidth(15)
f.set_figheight(8)
plt.plot(x,y1,label="April")
plt.plot(x,y2,label="May")
plt.plot(x,y3,label="June")
plt.plot(x,y4,label="July")
plt.plot(x,y5,label="August")
plt.plot(x,y6,label="September")
plt.plot(x,y7,label="October")
plt.plot(x,y8,label="November")
plt.plot(x,y9,label="December")
plt.plot(x,y10,label="January")
plt.plot(x,y11,label="February")
plt.plot(x,y12,label="March")
plt.xticks(x,labels,rotation=40)
plt.legend()
plt.title("Line chart of crude prices from the 2011-2020",color="red")
plt.xlabel("Year",color="red")
plt.ylabel("price",color="red")
plt.show()


# ### observation:-
# 1.The line plot is used to show how the frequency of pricing increase or decreases over 10 years .we can clearly state there is increase in prices over 2011-2013 and gradually decreased.

# In[33]:


my_color =['yellow', 'cyan','m','blue']
before_10.plot(x="Year", y=["Import_in($)", "Export ($)"], 
        kind="bar",figsize=(10,4),color=my_color)

# Show

plt.show()


# In[34]:


my_color =['yellow', 'cyan','m','blue']
after_10.plot(x="Year", y=["Import_in($)", "Export ($)"], 
        kind="bar",figsize=(10,4),color=my_color)

# Show

plt.show()


# In[35]:


my_color =['yellow', 'cyan','m','blue']
before_10.plot(x="Year", y=["Import(Rs)", "Export(Rs)"], 
        kind="bar",figsize=(10,4),color=my_color)

# Show

plt.show()


# In[36]:


my_color =['yellow', 'cyan','m','blue']
after_10.plot(x="Year", y=["Import(Rs)", "Export(Rs)"], 
        kind="bar",figsize=(10,4),color=my_color)

# Show

plt.show()


# In[37]:


fig = plt.figure()


labels=before_10['Year']
fracs=before_10['Average']
colors = sns.color_palette('pastel')[0:5]
ax1 = fig.add_axes([0, .8, .4, .8], aspect=1)
ax1.pie(fracs, labels = labels, colors = colors, radius = 1.2,autopct='%.0f%%')


plt.title("average prices over the years",color="blue")


labels1=after_10['Year']
fracs1=after_10['Average']
colors = sns.color_palette('pastel')[0:5]
ax2 = fig.add_axes([.6, .8, .9, .8], aspect=1)
ax2.pie(fracs1, labels = labels1, colors = colors, radius = 1.2,autopct='%.0f%%')


plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




