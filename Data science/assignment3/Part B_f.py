# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:16:47 2024

@author: tanvi
"""

import pandas as pd

# Read the CSV data
T_data = pd.read_csv("E:\SPRING 2024\Introduction to Data Science\Algerian_forest_Modm.csv")

rdata=T_data.sample(n=180, random_state=4925)
# Select the "Temperature" column
F = rdata["Temperature"]

xd=pd.DataFrame(F)

print("Coefficient of Skewness: ", xd.skew())
print("Coefficient of Kurtosis: ", xd.kurt())