# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:12:11 2024

@author: tanvir
"""

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV data
Main_data = pd.read_csv("E:\SPRING 2024\Introduction to Data Science\Algerian_forest_Modm.csv")

#select random data
random_data=Main_data.sample(n=180, random_state=4925)

#select a variable
df = random_data["FWI"]

# Calculate summary statistics
print("Summary statistics:")
print(df.describe())

# Create a box plot
plt.boxplot(df)
plt.title("Box Plot of the Data")
plt.xlabel("Data")
plt.ylabel("Value")
plt.grid(True)
plt.show()

# Identify outliers (based on IQR rule)
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df < lower_bound) | (df > upper_bound)]

# Check for outliers
if outliers.empty:
    print("No outliers detected.")
else:
    print("Outliers:", outliers.tolist())