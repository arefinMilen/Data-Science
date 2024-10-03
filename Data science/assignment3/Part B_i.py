# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:23:05 2024

@author: tanvir
"""

import numpy as np
import pandas as pd
import scipy.linalg as la 

T_data = pd.read_csv("E:\SPRING 2024\Introduction to Data Science\Algerian_forest_Modm.csv")

rdata=T_data.sample(n=180, random_state=4925)
# Select the "Temperature" column

Z1=np.transpose(rdata[["RH","FWI"]])
Z2=Z1.copy()

S1=np.cov(Z1,bias=False);S1
S2=np.cov(Z2,bias=False);S2

X1b=np.mean(Z1,axis=1);X1b
X2b=np.mean(Z2,axis=1);X2b

n2=len(rdata); n1=len(rdata)

Sp=((n1-1)/((n1-1)+(n2-1)))*S1+((n2-1)/((n2-1)+(n2-1)))*S2;Sp

SpI = la.inv(Sp) 

X12=X1b-X2b;X12
yh=np.dot(X12,SpI);yh

U=X1b+X2b
mhat=np.dot((1/2)*yh,U)

v1 = float(input("Please provide 1st value: "));
v2 = float(input("Please provide 2nd value: "));
x0=[v1,v2]

rule=np.dot(yh,x0)-mhat;rule

if rule>0:
    print("Subject/individual belongs to Group 1")
else:
    print("Subject/individual belongs to Group 2")

#--------------------------------------#