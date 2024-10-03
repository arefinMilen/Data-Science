# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:12:11 2024

@author: tanvir
"""

import pandas as pd

x=[30, 29, 33, 31, 27]
xd=pd.DataFrame(x)

# Calculate the descriptive statistics
print("Minimum:", xd.min())
print("First quartile (Q1):", xd.quantile(0.25))
print("Median:", xd.median())
print("Third quartile (Q3):", xd.quantile(0.75))
print("Maximum:", xd.max())