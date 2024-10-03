# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 20:55:43 2024

@author: arefin
"""

import pandas as pd

# Read the CSV data
RH_data = pd.read_csv("C:\data\Algerian_forest_Modm (2).csv")

rdata=RH_data.sample(n=180, random_state=5279)
# Select the "RH" column
F = rdata["RH"]

xd=pd.DataFrame(F)

print("Coefficient of Skewness: ", xd.skew())
print("Coefficient of Kurtosis: ", xd.kurt())
