import csv
import pandas as pd

df=pd.read_csv("total_stars.csv")
print(df.shape)

del df["Luminosity"]
print(list(df))

df.to_csv('main.csv')
print(df.shape)
