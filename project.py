import pandas as pd
import plotly.express as px
import csv

df = pd.read_csv("prodata.csv")

sport = df["Sports"].tolist()
distance = df["Distance(km)"].tolist()



fig = px.bar(x=sport, y=distance)
fig.show()

