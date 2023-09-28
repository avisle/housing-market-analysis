#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


get_ipython().system('pip install pandas folium branca')


# In[2]:


import pandas as pd
import folium
from branca.colormap import LinearColormap

# Load the CSV data into a DataFrame
data = pd.read_csv("California_Houses.csv")

# Create a map with an initial view centered on the first data point's latitude and longitude
initial_latitude = data.loc[0, "Latitude"]
initial_longitude = data.loc[0, "Longitude"]
m = folium.Map(location=[initial_latitude, initial_longitude], zoom_start=10)

# Create a colormap for median house values (you can customize this)
colormap = LinearColormap(
    colors=["green", "yellow", "red"],
    vmin=data["Median_House_Value"].min(),
    vmax=data["Median_House_Value"].max()
)
colormap.caption = "Median House Price"

# Iterate through the data and add markers with colors based on median house prices
for index, row in data.iterrows():
    latitude, longitude, median_price = row["Latitude"], row["Longitude"], row["Median_House_Value"]
    color = colormap(median_price)
    folium.CircleMarker(
        [latitude, longitude],
        radius=5,
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.7,
        popup=f"Median Price: ${median_price}""
    ).add_to(m)

# Add the colormap to the map
colormap.add_to(m)

# Save the map to an HTML file
m


# In[ ]:





# In[ ]:




