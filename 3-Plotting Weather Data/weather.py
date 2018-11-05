
# coding: utf-8

# In[8]:


# Making a Bokeh graph to dsiplay weather data from an excel file

from bokeh.models import HoverTool
from bokeh.plotting import figure
from bokeh.io import output_notebook, output_file, show
import pandas
import sys

df = pandas.read_excel("verlegenhuken.xlsx", sheet_name=0)
df["Temperature"] = df["Temperature"]/10
df["Pressure"] = df["Pressure"]/10

# Prepare the output
if sys.stdin.isatty():
    output_file("weather_graph.html")
else:
    output_notebook()

# Create figure object
f = figure(title="Temperature and Air Pressure",
           plot_width=500,
           plot_height=400)
f.xaxis.axis_label = "Temperature (C)"
f.yaxis.axis_label = "Pressure (hPa)"

# Create circle plot
f.circle(x=df["Temperature"], y=df["Pressure"], size=0.5)
f.add_tools(HoverTool(tooltips=[("Temperature", "@x"), ("Pressure", "@y")]))

# Display
show(f)


# In[ ]:




