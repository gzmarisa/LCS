# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 11:35:05 2024

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
## Define functions
def  not_available(parameter):
    return parameter == ''

## Data path for AirQo
path_AirQo = '../Data/AirQo/Raw/'

# Data path for Airqo G5126
#path_AirQo_g5126 = 'C:/Users/u23993376/Documents/GitHub/LCS/Data/AirQo/Raw/g5126/'

# with open(path_AirQo + '20231212_airqo_g5126_raw.txt', newline='') as csv_file:
#     reader = csv.reader(csv_file, delimiter=',')
#     for i,row in enumerate(reader):
#         if i > 0 and i < 10:
#             print(row[1])

## Upload data from Airqo device g5126
### Go throught all files in the directory 
## Use a wildcard pattern to match all CSV files in the directory
# files_AirQo = glob.glob(path_AirQo + '*.txt')
# files_AirQo.sort(key=os.path.getmtime)

# combined_data_AirQo = []
# for filename in files_AirQo:
#     filepath = filename
#     with open(filepath, newline='') as txt_file:
#         reader = csv.reader(txt_file, delimiter=',')
#         counter = 0
#         for row in reader:
#             if counter > 0:
#                 combined_data_AirQo.append(row)
  
#             counter += 1

# with open('20240423_airqo_aqg5126_raw_combined.csv', 'a', newline='') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerows(combined_data_AirQo)


# Data path for Airqo G5113
# path_AirQo_g5113 = 'C:/Users/u23993376/Documents/GitHub/LCS/Data/AirQo/Raw/g5113/'

# # Upload data from Airqo device g5113
# ## Go throught all files in the directory 
# # Use a wildcard pattern to match all CSV files in the directory
# files_AirQo_g5113 = glob.glob(path_AirQo_g5113 + '*.txt')
# files_AirQo_g5113.sort(key=os.path.getmtime)

# combined_data_AirQo_g5113 = []
# for filename in files_AirQo_g5113:
#     filepath = filename
#     with open(filepath, newline='') as txt_file:
#         reader = csv.reader(txt_file, delimiter=',')
#         counter = 0
#         for row in reader:
#             if counter > 0:
#                 combined_data_AirQo_g5113.append(row)
  
#             counter += 1

# with open('20240423_airqo_aqg5113_raw_combined.csv', 'a', newline='') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerows(combined_data_AirQo_g5113)

# Data path for AirQo UP
# path_AirQo_g5113 = 'C:/Users/u23993376/Documents/GitHub/LCS/Data/AirQo/Raw/g5113/'

# # Upload data from Airqo device g5113
# ## Go throught all files in the directory 
# # Use a wildcard pattern to match all CSV files in the directory
# files_AirQo_g5113 = glob.glob(path_AirQo_g5113 + '*.txt')
# files_AirQo_g5113.sort(key=os.path.getmtime)

# combined_data_AirQo_g5113 = []
# for filename in files_AirQo_g5113:
#     filepath = filename
#     with open(filepath, newline='') as txt_file:
#         reader = csv.reader(txt_file, delimiter=',')
#         counter = 0
#         for row in reader:
#             if counter > 0:
#                 combined_data_AirQo_g5113.append(row)
  
#             counter += 1

# with open('20240423_airqo_aqg5113_raw_combined.csv', 'a', newline='') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerows(combined_data_AirQo_g5113)


list_airqo_g5126_PM25_raw = []
list_airqo_g5126_PM10_raw = []
list_airqo_g5126_timestamp_raw = []
#list_airqo_g5113_timestamp_sast_raw = []

# Go through CSV file with 
with open('20240423_airqo_aqg5126_raw_combined.csv', newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for i,row in enumerate(reader):
        if i > 0:
            #print(row)
            airqo_g5126_timestamp_raw = row[9]
            airqo_g5126_timestamp_raw = datetime.strptime(airqo_g5126_timestamp_raw, '%Y-%m-%d %H:%M:%S')
            list_airqo_g5126_timestamp_raw.append(airqo_g5126_timestamp_raw)
            #print(airqo_g5113_timestamp_raw)
            
            airqo_g5126_PM25_raw = row[7]
            if not_available(airqo_g5126_PM25_raw):
                airqo_g5126_PM25_raw = np.nan
            list_airqo_g5126_PM25_raw.append(float(airqo_g5126_PM25_raw))
            #print(airqo_g5126_PM25_raw)
            
            airqo_g5126_PM10_raw = row[5]
            if not_available(airqo_g5126_PM10_raw):
                airqo_g5126_PM10_raw = np.nan
            list_airqo_g5126_PM10_raw.append(float(airqo_g5126_PM10_raw))
            #print(airqo_g5126_PM10_raw)        


list_airqo_g5113_PM25_raw = []
list_airqo_g5113_PM10_raw = []
list_airqo_g5113_timestamp_raw = []
#list_airqo_g5113_timestamp_sast_raw = []
            
# Go through CSV file with 
# with open('20240423_airqo_aqg5113_raw_combined.csv', newline='') as csv_file:
#     reader = csv.reader(csv_file, delimiter=',')
#     for i,row in enumerate(reader):
#         if i > 0 and i < 10:
#             #print(row)
#             airqo_g5113_timestamp_raw = row[9]
#             airqo_g5113_timestamp_raw = datetime.strptime(airqo_g5113_timestamp_raw, '%Y-%m-%d %H:%M:%S')
#             list_airqo_g5113_timestamp_raw.append(airqo_g5113_timestamp_raw)
#             #print(airqo_g5113_timestamp_raw)
            
#             airqo_g5113_PM25_raw = row[7]
#             if not_available(airqo_g5113_PM25_raw):
#                 airqo_g5113_PM25_raw = np.nan
#             list_airqo_g5113_PM25_raw.append(float(airqo_g5113_PM25_raw))
#             #print(airqo_g5113_PM25_raw)
            
#             airqo_g5113_PM10_raw = row[5]
#             if not_available(airqo_g5113_PM10_raw):
#                 airqo_g5113_PM10_raw = np.nan
#             list_airqo_g5113_PM10_raw.append(float(airqo_g5113_PM10_raw))
#             #print(airqo_g5113_PM10_raw)                    

## PM25 Raw Data for AirQo G5126
plt.scatter(list_airqo_g5126_timestamp_raw, list_airqo_g5126_PM25_raw, alpha=0.5, marker="x")
#plt.ylim(0, 100)
plt.xticks(rotation=45, ha='right')
plt.xlabel("Date")
plt.ylabel("PM$_{2.5}$ ($\mu$g/m$^3$)")
plt.title("PM$_{2.5}$ Raw Data")
#plt.locator_params(axis='x', nbins=12)
plt.grid()

## PM10 Plots 
## PM10 RAW Data
# plt.scatter(list_timestamp_sast_raw, list_PM10_raw, alpha=0.5, marker="x")
# plt.ylim(0, 1000)
# plt.xticks(rotation=45, ha='right')
# plt.xlabel("Date")
# plt.ylabel("PM$_{10}$ ($\mu$g/m$^3$)")
# plt.title("PM$_{10}$ Raw Data")
# #plt.locator_params(axis='x', nbins=12)
# plt.grid()

## PM25 Raw Data
# plt.scatter(list_timestamp_sast_raw, list_PM1_raw, alpha=0.5, marker="x")
# #plt.ylim(0, 100)
# plt.xticks(rotation=45, ha='right')
# plt.xlabel("Date")
# plt.ylabel("PM$_{2.5}$ ($\mu$g/m$^3$)")
# plt.title("PM$_{2.5}$ Raw Data")
# #plt.locator_params(axis='x', nbins=12)
# plt.grid()

## PM10 Plots 
## PM10 RAW Data
# plt.scatter(list_timestamp_sast_raw, list_PM10_raw, alpha=0.5, marker="x")
# plt.ylim(0, 1000)
# plt.xticks(rotation=45, ha='right')
# plt.xlabel("Date")
# plt.ylabel("PM$_{10}$ ($\mu$g/m$^3$)")
# plt.title("PM$_{10}$ Raw Data")
# #plt.locator_params(axis='x', nbins=12)
# plt.grid()