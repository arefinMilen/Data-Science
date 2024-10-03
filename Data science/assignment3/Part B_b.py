# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:01:53 2024

@author: tanvir
"""
#import random
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV data
T_data = pd.read_csv("E:\SPRING 2024\Introduction to Data Science\Algerian_forest_Modm.csv")

rdata=T_data.sample(n=180, random_state=4925)
# Select the "Temperature" column
F = rdata["Temperature"]


# Extract temperature values as a NumPy array
temperature_values = F.to_numpy()  # or F.values

# Create the histogram
plt.hist(temperature_values)
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.title("Distribution of Temperature")
plt.show()