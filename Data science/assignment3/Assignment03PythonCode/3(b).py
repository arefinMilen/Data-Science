# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 19:54:31 2024

@author: arefin
"""

#import random
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV data
RH_data = pd.read_csv("C:\data\Algerian_forest_Modm (2).csv")

rdata=RH_data.sample(n=180, random_state=5279)
# Select the "RH" column
F = rdata["RH"]


# Extract temperature values as a NumPy array
RH_values = F.to_numpy()  # or F.values

# Create the histogram
plt.hist(RH_values)
plt.xlabel("Relative_Humidity")
plt.ylabel("Frequency")
plt.title("Distribution of Relative-Humidity")
plt.show()