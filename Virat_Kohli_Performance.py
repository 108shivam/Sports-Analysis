#!/usr/bin/env python
# coding: utf-8

# # Virat Kohli Performace Analysis

# ### Virat Kohli is one of the most famous cricketers in the world. So it will be a great data science project if we analyze the batting performance of Virat Kohli over the years.

# ### Here you are given a dataset of all the ODI matches played by Virat Kohli from 18 August 2008 to 22 January 2017. 

# # Below is the complete information about all the columns in the dataset:
# 
# * Runs: Runs in the match
# * BF: Balls faced in the match
# * 4s: number of 4s in a match
# * 6s: number of 6s in a match
# * SR: Strike Rate in the match
# * Pos: Batting Position in the match
# * Dismissal: How Virat Kohli got out in the match
# * Inns: 1st and 2nd innings
# * Opposition: Who was the opponent of India
# * Ground: Venue of the match
# * Start Date: Date of the match

# Importing Useful Libraries to analyze the dataset.

# In[9]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("Virat_kohli.csv")


# In[12]:


data.head()


# Let's have a look at whether this dataset contains any null values or not before moving forward.

# In[13]:


data.isnull().sum()


# The dataset contains matches played by Virat Kohli between 18 August 2008 and 22 January 2017. So let's have a look at the total runs scored by Virat Kohli.

# In[14]:


# Total Runs between 18-Aug-2008 - 22-Jan-2017
data["Runs"].sum()


# Now let’s have a look at the average of Virat Kohli during the same period:

# In[15]:


# Average Runs Between 18-Aug-08 - 22-Jan-17
data["Runs"].mean()


# In ODIs, the batting average of 35-37 is considered a good average. So Virat Kohl’s batting average is good. Now let’s have a look at the trend of runs scored by Virat Kohli in his career from 18 August 2008 to 22 January 2017:

# In[16]:


matches = data.index
figure = px.line(data,x=matches, y="Runs",title = 'Runs scored by Virat Kohli Between 18-Aug-2008 - 22-Jan-2017')
figure.show()


# In so many innings played by Virat Kohli, he scored over 100 or close to it. That is a good sign of consistency. Now let’s see all the batting positions played by Virat Kohli:

# In[17]:


# Batting Positions
data["Pos"] = data["Pos"].map({3.0: "Batting At 3", 4.0: "Batting At 4", 2.0: "Batting At 2", 
                               1.0: "Batting At 1", 7.0:"Batting At 7", 5.0:"Batting At 5", 
                               6.0: "batting At 6"})

Pos = data["Pos"].value_counts()
label = Pos.index
counts = Pos.values
colors = ['gold','lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Number of Matches At Different Batting Positions')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# In more than 68% of all the innings played by Virat Kohli, he batted in the third position. Now let’s have a look at the total runs scored by Virat Kohli in different positions:

# In[18]:


label = data["Pos"]
counts = data["Runs"]
colors = ['gold','lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Runs By Virat Kohli At Different Batting Positions')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# More than 72% of the total runs scored by Virat Kohli are while batting at 3rd position. So we can say batting at 3rd position is perfect for Virat Kohli.
# 
# Now let’s have a look at the number of centuries scored by Virat Kohli while batting in the first innings and second innings:

# In[19]:


centuries = data.query("Runs >= 100")
figure = px.bar(centuries, x=centuries["Inns"], y = centuries["Runs"], 
                color = centuries["Runs"],
                title="Centuries By Virat Kohli in First Innings Vs. Second Innings")
figure.show()


# So most of the centuries are scored while batting in the second innings. By this, we can say that Virat Kohli likes chasing scores. Now let’s have a look at the kind of dismissals Virat Kohli faced most of the time:

# In[20]:


# Dismissals of Virat Kohli
dismissal = data["Dismissal"].value_counts()
label = dismissal.index
counts = dismissal.values
colors = ['gold','lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Dismissals of Virat Kohli')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# So most of the time, Virat Kohli gets out by getting caught by the fielder or the keeper. Now let’s have a look at against which team Virat Kohli scored most of his runs:

# In[21]:


figure = px.bar(data, x=data["Opposition"], y = data["Runs"], color = data["Runs"],
            title="Most Runs Against Teams")
figure.show()


# According to the above figure, Virat Kohli likes batting against Sri Lanka, Australia, New Zealand, West Indies, and England. But he scored most of his runs while batting against Sri Lanka. Now let’s have a look at against which team Virat Kohli scored most of his centuries:

# In[22]:


figure = px.bar(centuries, x=centuries["Opposition"], y = centuries["Runs"], 
                color = centuries["Runs"],
                title="Most Centuries Against Teams")
figure.show()


# So, most of the centuries scored by Virat Kohli were against Australia. Now let’s analyze Virat Kohli’s strike rate. To analyze Virat Kohli’s strike rate, I will create a new dataset of all the matches played by Virat Kohli where his strike rate was more than 120:

# In[23]:


strike_rate = data.query("SR >= 120")
strike_rate


# Now let’s see whether Virat Kohli plays with high strike rates in the first innings or second innings:

# In[24]:


figure = px.bar(strike_rate, x = strike_rate["Inns"], 
                y = strike_rate["SR"], 
                color = strike_rate["SR"],
            title="Virat Kohli's High Strike Rates in First Innings Vs. Second Innings")
figure.show()


# So according to the above figure, Virat Kohli likes playing more aggressively in the first innings compared to the second innings. Now let’s see the relationship between runs scored by Virat Kohli and fours played by him in each innings:

# In[25]:


figure = px.scatter(data_frame = data, x="Runs",
                    y="4s", size="SR", trendline="ols", 
                    title="Relationship Between Runs Scored and Fours")
figure.show()


# There is a linear relationship. It means that Virat Kohli likes playing fours. The more runs he scores in the innings, the more fours he plays. Let’s see if there is some relationship with the sixes:

# In[26]:


figure = px.scatter(data_frame = data, x="Runs",
                    y="6s", size="SR", trendline="ols", 
                    title= "Relationship Between Runs Scored and Sixes")
figure.show()


# There is no strong linear relationship here. It means Virat Kohli likes playing fours more than sixes. So this is how you can analyze the performance of Virat Kohli or any other cricketer in the world.

# # Summary
# So this is how I have perform Virat Kohli performance analysis using the Python programming language. Analyzing a player’s performance is one of the use cases of Data Science in sports analytics.

# In[ ]:




