# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 20:57:52 2024

@author: arefin
"""

import pandas as pd

# Read the CSV data
RH_data = pd.read_csv("C:\data\Algerian_forest_Modm (2).csv")

rdata=RH_data.sample(n=180, random_state=5279)
# Select the "RH" column
stat=rdata[["Temperature","RH","Ws","Rain","FFMC","DMC","DC","ISI","BUI","FWI"]]

print("Correlation Matrix: ", stat.corr()) # Creats correlation matrix of stat 
print("Coveriance Matrix: ", stat.cov())# Creats covariance matrix of stat 