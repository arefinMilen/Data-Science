# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 23:30:11 2024

@author: arefin
"""

import pandas as pd

x=[79, 81, 83, 87, 88]
xd=pd.DataFrame(x)

# Calculate the descriptive statistics
print("Minimum:", xd.min())
print("First quartile (Q1):", xd.quantile(0.25))
print("Median:", xd.median())
print("Third quartile (Q3):", xd.quantile(0.75))
