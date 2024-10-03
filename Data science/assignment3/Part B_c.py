# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:08:36 2024

@author: tanvir
"""

import pandas as pd
import statistics

# Read the CSV data
T_data = pd.read_csv("E:\SPRING 2024\Introduction to Data Science\Algerian_forest_Modm.csv")

rdata=T_data.sample(n=180, random_state=4925)
# Select the "Temperature" column
F = rdata["Temperature"]


# Calculate descriptive statistics (excluding harmonic mean)
print("Mean:", statistics.mean(F))
print("Median:", statistics.median(F))
print("Mode:", statistics.mode(F))

if min(F) >= 0:  # Check if all values are non-negative
    print("Harmonic Mean:", statistics.harmonic_mean(F))
else:
    print("Harmonic Mean: Calculation not possible due to negative values")
          
print("Geometric Mean: ", statistics.geometric_mean(F))
