# EDA - Exploratory Data Analysis

import pandas as pd 
df = pd.read_csv("placement.csv")

print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nInfo:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nFirst 5 Rows:")
print(df.head())