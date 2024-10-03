# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:20:59 2024

@author: tanvir
"""

import pandas as pd

# Read the CSV data
T_data = pd.read_csv("E:\SPRING 2024\Introduction to Data Science\Algerian_forest_Modm.csv")

rdata=T_data.sample(n=180, random_state=4925)
# Select the "Temperature" column

Select_var1=rdata["FWI"]
Select_var2=rdata["RH"]

from scipy import stats
slope, intercept, r, p,  std_err = stats.linregress(Select_var1, Select_var2)

print(r)
slope
intercept
stats.linregress(Select_var1, Select_var2) # Returns b, a, r, pvalue, standard_error
