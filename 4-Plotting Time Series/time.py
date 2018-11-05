
# coding: utf-8

# In[ ]:





# In[8]:


# Making a Bokeh graph to dsiplay financial data over time
# Originally from a web link
# However, link now results in 403 forbidden. Loading file instead.

from bokeh.plotting import output_notebook, output_file, figure, show
import pandas
import sys

df = pandas.read_csv("adbe.csv", parse_dates=["Date"])
p = figure(width=500, height=500, x_axis_type="datetime")#, sizing_mode="stretch_both")
p.line(df["Date"], df["Close"], color="Orange", alpha=0.5)
p.xaxis.axis_label = "Date"
p.yaxis.axis_label = "Close"

# Prepare the output
if sys.stdin.isatty():
    output_file("finance_graph.html")
else:
    output_notebook()

# Display
show(p)


# In[ ]:




