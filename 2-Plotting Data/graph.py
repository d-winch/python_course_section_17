# Making a basic Bokeh graph

from bokeh.models import HoverTool
from bokeh.plotting import figure
from bokeh.io import output_notebook, output_file, show
import pandas
import sys

df = pandas.read_csv("bachelors.csv")

# Prepare the output
# Check if running on command line or notebook
if sys.stdin.isatty():
    output_file("bachelors_graph.html")
else:
    output_notebook()

# Create figure object
f = figure(title="Percentage of women who have received a bachelor's degree in engineering by year",
           plot_width=900,
           plot_height=500)

# Create line plot
f.line(x=df["Year"], y=df["Engineering"], line_width=1)
f.add_tools(HoverTool(tooltips=[("Year", "@x"), ("Engineering %", "@y")]))

# Display
show(f)
