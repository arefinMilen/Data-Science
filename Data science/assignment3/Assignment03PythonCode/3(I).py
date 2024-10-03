# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 21:01:53 2024

@author: arefin
"""

import numpy as np
import pandas as pd
import scipy.linalg as la 

RH_data = pd.read_csv("C:\data\Algerian_forest_Modm (2).csv")

rdata=RH_data.sample(n=180, random_state=5279)
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
