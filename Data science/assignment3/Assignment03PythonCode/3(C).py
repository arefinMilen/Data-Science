# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 20:44:13 2024

@author: arefin
"""


import pandas as pd
import statistics

# Read the CSV data
RH_data = pd.read_csv("C:\data\Algerian_forest_Modm (2).csv")

rdata=RH_data.sample(n=180, random_state=5279)
# Select the "Temperature" column
F = rdata["RH"]


# Calculate descriptive statistics (excluding harmonic mean)
print("Mean:", statistics.mean(F))
print("Median:", statistics.median(F))
print("Mode:", statistics.mode(F))

if min(F) >= 0:  # Check if all values are non-negative
    print("Harmonic Mean:", statistics.harmonic_mean(F))
else:
    print("Harmonic Mean: Calculation not possible due to negative values")
          
print("Geometric Mean: ", statistics.geometric_mean(F))
