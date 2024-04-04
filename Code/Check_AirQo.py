# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:39:56 2024

@author: u23993376
"""
# Import relevent libraries
import csv
import glob
import os
import matplotlib.pyplot as plt
from datetime import datetime

# ## Define functions
# def empty(parameter):
#     return len(parameter) == 0

# def  not_available(parameter):
#     return parameter == 'N/A'

# def negative(parameter):
#     return float(parameter) < 0

# # Data paths 
# path_2BTech = '../Data/2BTech/'


list_PM25_hourly = []
list_date = []
list_time = []
list_timestamp = []

##  
with open('../Data/AirQo/Test/20240403_airquality-data_oneweek.txt', newline='') as txt_file:
    reader = csv.reader(txt_file, delimiter=',')
    
    previous_row = None
    for i,row in enumerate(reader):
        if i > 0:
            PM25 = row[3]
            timestamp = row[5]
            date = timestamp.split(' ')[0]
            list_PM25_hourly.append(float(PM25))

            
            list_date.append(date)
            list_timestamp.append(timestamp)
                
                
            previous_row = row   


plt.scatter(list_timestamp, list_PM25_hourly)
plt.xticks(range(len(list_PM25_hourly)), list_date)
#plt.xticks(rotation=45)
#plt.ylim(0, 200)
plt.xlabel("Date")
plt.ylabel("PM$_{25}$ ($\mu$g/m$^3$)")
plt.xticks(rotation=45, ha='right')
plt.locator_params(axis='x', nbins=8)
#plt.xticks(['2024-03-26', '2024-03-27', '2024-03-28', '2024-03-29', '2024-03-30', '2024-03-31', '2024-04-01','2024-04-02'])
plt.grid()
