# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 20:50:13 2024

@author: arefin
"""

import pandas as pd
import statistics

# Read the CSV data
RH_data = pd.read_csv("C:\data\Algerian_forest_Modm (2).csv")

rdata=RH_data.sample(n=180, random_state=5279)
# Select the "RH" column
F = rdata["RH"]

# Calculate population standard deviation
population_std = statistics.pstdev(F)

# Calculate population coefficient of variation (CV)
population_cv = (population_std / statistics.mean(F)) * 100

# Print the results
print("Population stdv:", population_std)
print("Population CV:", population_cv, "%")
