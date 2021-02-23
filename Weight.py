import plotly.figure_factory as ff
import csv
import pandas as pd
df = pd.read_csv("Weight.csv")
fig = ff.create_distplot([df["Weight(Pounds)"].tolist()], ["Weight"], show_hist = False)
fig.show()
