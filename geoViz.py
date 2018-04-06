#Project 3
#Information Visualization
#Group 7
#Joshua Griffiths
#Spring 2018

#Heat map of average importance of privacy by country
#Based on a 1-10 Scale

import geopandas as gpd
import csv
import matplotlib.pyplot as plt
import pandas as pd

from bokeh.io import show
from bokeh.models import (
    ColumnDataSource,
    HoverTool,
    LogColorMapper
)
from bokeh.palettes import Viridis6 as palette
from bokeh.plotting import figure

from shapely.geometry import Point
palette.reverse()

#Gets all countries with lats and longs
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
#Parses just the names and the longs,lats
countries = world[['name','geometry']]


#Appends the privacy rating for each country on to our dataset
privacy = pd.read_csv('geoData.csv')
countryPrivacy = countries.merge(privacy, on = 'name')

#Plot the dataset on to a HeatMap based on privacy rating
countryPrivacy.plot(column='privacy', cmap='OrRd',legend = True)
#gpd.title('Country vs Importance of Privacy')




#Show the plot
plt.show()
