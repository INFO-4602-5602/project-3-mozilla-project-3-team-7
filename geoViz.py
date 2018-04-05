#Project 3
#Information Visualization
#Group 7
#Joshua Griffiths
#Spring 2018

#Heat map of average importance of privacy by country
#Based on a 1-10 Scale

from bokeh.io import show
from bokeh.models import (
    ColumnDataSource,
    HoverTool,
    LogColorMapper
)
from bokeh.palettes import Viridis6 as palette
from bokeh.plotting import figure

from bokeh.sampledata.us_counties import data as counties
from bokeh.sampledata.unemployment import data as unemployment

palette.reverse()



