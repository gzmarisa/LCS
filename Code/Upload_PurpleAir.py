# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 14:16:18 2024

@author: u23993376
"""

# Import relevent libraries
import csv
import glob
import os
import numpy as np 
import matplotlib.pyplot as plt
from datetime import datetime

## Define functions
def  not_available(parameter):
    return parameter == ''

# def empty(parameter):
#     return len(parameter) == 0

# def negative(parameter):
#     return float(parameter) < 0

# Data paths 
path_PA = '../Data/PurpleAir/'



list_PA_up202303_PM1_raw = []
list_PA_up202303_PM25_raw = []
list_PA_up202303_PM10_raw = []
list_PA_up202303_timestamp_utc_raw = []


# Go through CSV file with raw PurpleAir data
with open(path_PA + 'UP_2023_03/20240422_PurpleAir_UP202303_raw.csv', newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for i,row in enumerate(reader):
        if i > 0:
            PA_up202303_timestamp_utc_raw = row[0]
            PA_up202303_timestamp_utc_raw = PA_up202303_timestamp_utc_raw.replace("T", " ").replace("Z", "")
            PA_up202303_timestamp_utc_raw = datetime.strptime(PA_up202303_timestamp_utc_raw, '%Y-%m-%d %H:%M:%S')
            list_PA_up202303_timestamp_utc_raw.append(PA_up202303_timestamp_utc_raw)
            #print(PA_up202303_timestamp_utc_raw)
            
            PA_up202303_PM1_raw = row[4]
            if not_available(PA_up202303_PM1_raw): 
                PA_up202303_PM1_raw = np.nan
            list_PA_up202303_PM1_raw.append(float(PA_up202303_PM1_raw))
            #print(PA_up202303_PM1_raw)
            
            PA_up202303_PM25_raw = row[5]
            if not_available(PA_up202303_PM25_raw): 
                PA_up202303_PM25_raw = np.nan
            list_PA_up202303_PM25_raw.append(float(PA_up202303_PM25_raw))
            #print(PA_up202303_PM25_raw)
            
            PA_up202303_PM10_raw = row[6]
            if not_available(PA_up202303_PM10_raw): 
                PA_up202303_PM10_raw = np.nan
            list_PA_up202303_PM10_raw.append(float(PA_up202303_PM10_raw))
            #print(PA_up202303_PM10_raw)


## PM1 Plots
## PM1 RAW Data
# plt.scatter(list_PA_up202303_timestamp_utc_raw, list_PA_up202303_PM1_raw, alpha=0.5, marker="x")
# #plt.ylim(0, 100)
# plt.xticks(rotation=45, ha='right')
# plt.xlabel("Date")
# plt.ylabel("PM$_{1}$ ($\mu$g/m$^3$)")
# plt.title("PM$_{1}$ Raw Data")
# #plt.locator_params(axis='x', nbins=12)
# plt.grid()

## PM25 Plots
## PM25 Raw Data
plt.scatter(list_PA_up202303_timestamp_utc_raw, list_PA_up202303_PM25_raw, alpha=0.5, marker="x")
#plt.ylim(0, 100)
plt.xticks(rotation=45, ha='right')
plt.xlabel("Date")
plt.ylabel("PM$_{2.5}$ ($\mu$g/m$^3$)")
plt.title("PM$_{2.5}$ Raw Data")
#plt.locator_params(axis='x', nbins=12)
plt.grid()

## PM10 Plots 
## PM10 RAW Data
plt.scatter(list_PA_up202303_timestamp_utc_raw, list_PA_up202303_PM10_raw, alpha=0.5, marker="x")
plt.ylim(0, 1000)
plt.xticks(rotation=45, ha='right')
plt.xlabel("Date")
plt.ylabel("PM$_{10}$ ($\mu$g/m$^3$)")
plt.title("PM$_{10}$ Raw Data")
#plt.locator_params(axis='x', nbins=12)
plt.grid()            