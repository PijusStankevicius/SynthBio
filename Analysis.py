import pandas as pd
import plotly as pl
import statsmodels as sm

data = pd.read_csv("bacteria.csv")
data = data.iloc[:,1:]
data.y.describe()
