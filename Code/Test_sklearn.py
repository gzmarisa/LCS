# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 10:16:10 2024

@author: u23993376
"""

# merge_timestamp
# merge_PA_PM
# merge_PA_RH 
# merge_PA_TEMP_C 
# merge_SAAQIS_PM 

import csv
import csv
import glob
import os
import numpy as np 
import matplotlib.pyplot as plt
import datetime
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


independent_variable1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
independent_variable2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

dependent_variable = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

independent_variables = [independent_variable1, independent_variable2]
independent_variables = np.array(independent_variables).T 

dependent_variable = np.array(dependent_variable)

X_train, X_test, y_train, y_test = train_test_split(independent_variables, dependent_variable, test_size=0.3, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

coefficients = model.coef_
print(coefficients)
print(independent_variables.columns)