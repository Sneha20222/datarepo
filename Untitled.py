#!/usr/bin/env python
# coding: utf-8

# ## Question 1: Use yfinance to Extract Stock Data

# Reset the index, save, and display the first five rows of the tesla_data dataframe using the head function. Upload a screenshot of the results and code from the beginning of Question 1 to the result below.

# In[1]:


import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[24]:


def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data.Date, infer_datetime_format=True), y=stock_data.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data.Date, infer_datetime_format=True), y=revenue_data.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()


# In[2]:


Tesla = yf.Ticker('TSLA')


# In[3]:


tesla_data = Tesla.history(period = "max")


# In[4]:


tesla_data.reset_index(inplace = True)
tesla_data.head()


# ## Question 2: Use Webscraping to Extract Tesla Revenue Data

# Display the last five rows of the tesla_revenue dataframe using the tail function.Upload a screenshot of the results.

# In[7]:


url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data = requests.get(url).text


# In[8]:


soup = BeautifulSoup(html_data, "html.parser")
soup.find_all('title')


# In[9]:


tesla_revenue = pd.DataFrame(columns = ['Date', 'Revenue'])

for row in soup.find_all("tbody")[1].find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    revenue = col[1].text.replace("$", "").replace(",", "")
    
    tesla_revenue = tesla_revenue.append({"Date": date, "Revenue": revenue}, ignore_index = True)


# In[10]:


tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]


# In[11]:


tesla_revenue.tail()


# # Use yfinance to Extract Stock Data

# Reset the index,save and display the first five rows of the gme_data dataframe using the head function.Upload a screenshot of the results and code from the beginning of Question 1 to the results below.

# In[13]:


GameStop = yf.Ticker("GME")


# In[14]:


gme_data = GameStop.history(period = 'max')


# In[15]:


gme_data.reset_index(inplace = True)
gme_data.head()


# # Question 4: Use Webscraping to Extract GME Revenue Data

# Display the last five rows of the gme_revenue dataframe using tail function.Upload a screenshot of the results.

# In[18]:


url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_data = requests.get(url).text


# In[19]:


soup = BeautifulSoup(html_data, "html.parser")
soup.find_all('title')


# In[20]:


gme_revenue = pd.DataFrame(columns = ['Date', 'Revenue'])

for row in soup.find_all("tbody")[1].find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    revenue = col[1].text.replace("$", "").replace(",", "")
    
    gme_revenue = gme_revenue.append({"Date": date, "Revenue": revenue}, ignore_index = True)


# In[21]:


tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
gme_revenue.tail()


# # Question 5: Plot Tesla Stock Graph

# Use the make_graph function to graph the Tesla Stock Data, also provide a title for the graph.

# In[25]:


make_graph(tesla_data, tesla_revenue, 'Tesla')


# # Question 6: Plot GameStop Stock Graph

# Use the make_graph function to graph the GameStop Stock Data, also provide a title for the graph.

# In[26]:


make_graph(gme_data, gme_revenue, 'GameStop')


# In[ ]:




