#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary packages
import os 
import folium
from folium import plugins
import rioxarray as rxr
import earthpy as et
import earthpy.spatial as es
import pandas as pd
import json
import numpy
from flask import Flask


# In[2]:


#creates map w/ folium
m = folium.Map(location=[45.5152, -122.6784], tiles = 'Stamen Terrain')


# In[3]:


#pulls data from Google sheets 
sheet_url = "https://docs.google.com/spreadsheets/d/160hgu9P2nK3TSYUS694bKlwcg_bpNDWax1WJKLg-Ex8/edit#gid=0"
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')


data = pd.read_csv(url_1, dtype=str)
data


# In[4]:


# add marker one by one on the map
for i in range(0,len(data)):
   folium.Marker(
      location=[data.iloc[i]['Lat'], data.iloc[i]['Long']],
      popup=data.iloc[i]['Name'],
   ).add_to(m)


# In[6]:


#makes webapp
app = Flask(__name__)

@app.route("/")
def fullscreen():
    return m.get_root().render()

if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:





# In[ ]:




