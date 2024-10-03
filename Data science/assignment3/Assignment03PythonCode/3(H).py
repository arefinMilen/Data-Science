# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 20:59:24 2024

@author: arefin
"""

import pandas as pd

# Read the CSV data
RH_data = pd.read_csv("C:\data\Algerian_forest_Modm (2).csv")

rdata=RH_data.sample(n=180, random_state=5279)
# Select the "RH" column

data1=rdata["FWI"]
data2=rdata["RH"]

from scipy import stats
slope, intercept, r, p,  std_err = stats.linregress(data1, data2)

print(r)
slope
intercept
stats.linregress(data1, data2) # Returns b, a, r, pvalue, standard_error
