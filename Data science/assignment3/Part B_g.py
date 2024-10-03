# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:18:37 2024

@author: tanvir
"""

import pandas as pd

# Read the CSV data
T_data = pd.read_csv("E:\SPRING 2024\Introduction to Data Science\Algerian_forest_Modm.csv")

rdata=T_data.sample(n=180, random_state=4925)
# Select the "Temperature" column
stat=rdata[["Temperature","RH","Ws","Rain","FFMC","DMC","DC","ISI","BUI","FWI"]]

print("Correlation Matrix: ", stat.corr()) # Creats correlation matrix of stat 
print("Coveriance Matrix: ", stat.cov())# Creats covariance matrix of stat 