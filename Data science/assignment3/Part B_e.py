# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:15:26 2024

@author: tanvir
"""

import pandas as pd
import statistics

# Read the CSV data
T_data = pd.read_csv("E:\SPRING 2024\Introduction to Data Science\Algerian_forest_Modm.csv")

rdata=T_data.sample(n=180, random_state=4925)
# Select the "Temperature" column
F = rdata["Temperature"]

# Calculate population standard deviation
population_std = statistics.pstdev(F)

# Calculate population coefficient of variation (CV)
population_cv = (population_std / statistics.mean(F)) * 100

# Print the results
print("Population stdv:", population_std)
print("Population CV:", population_cv, "%")
