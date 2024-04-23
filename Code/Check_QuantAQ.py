# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 12:12:58 2024

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
path_QuantAQ = '../Data/QuantAQ/'



list_PM1_raw = []
list_PM25_raw = []
list_PM10_raw = []
list_timestamp_sast_raw = []


# Go through CSV file with raw QuantAQ data
with open(path_QuantAQ + 'MOD-PM-00523-raw.csv', newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for i,row in enumerate(reader):
        if i > 0:
            timestamp_sast_raw = row[1]
            timestamp_sast_raw = timestamp_sast_raw.replace("T", " ").replace("Z", "")
            timestamp_sast_raw = datetime.strptime(timestamp_sast_raw, '%Y-%m-%d %H:%M:%S')
            list_timestamp_sast_raw.append(timestamp_sast_raw)
            #print(timestamp_sast_raw)
            
            PM1_raw = row[10]
            if not_available(PM1_raw): 
                PM1_raw = np.nan
            list_PM1_raw.append(float(PM1_raw))
            #print(PM1_raw)
            
            PM25_raw = row[11]
            if not_available(PM25_raw): 
                PM25_raw = np.nan
            list_PM25_raw.append(float(PM25_raw))
            #print(PM25_raw)
            
            PM10_raw = row[12]
            if not_available(PM10_raw): 
                PM10_raw = np.nan
            list_PM10_raw.append(float(PM10_raw))
            #print(PM10_raw)

# Reverse the raw data 
list_PM1_raw.reverse()
list_PM25_raw.reverse()
list_PM10_raw.reverse()
list_timestamp_sast_raw.reverse()
                                            
list_PM1_hour = []
list_PM25_hour = []
list_PM10_hour = []
list_timestamp_sast_hour = []

# Go through CSV file with HOURLY QuantAQ data
with open(path_QuantAQ + 'MOD-PM-00523-hour.csv', newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for i,row in enumerate(reader):
        if i > 0:
            timestamp_sast_hour = row[0]
            timestamp_sast_hour = timestamp_sast_hour.replace("T", " ").replace("+02:00", "")
            timestamp_sast_hour = datetime.strptime(timestamp_sast_hour, '%Y-%m-%d %H:%M:%S')
            list_timestamp_sast_hour.append(timestamp_sast_hour)
            #print(timestamp_sast)
            
            PM1_hour = row[9]
            if not_available(PM1_hour): 
                PM1_hour = np.nan
            list_PM1_hour.append(float(PM1_hour))
            # print(PM1_hour)
            
            PM25_hour = row[10]
            if not_available(PM25_hour): 
                PM25_hour = np.nan
            list_PM25_hour.append(float(PM25_hour))
            #print(PM25_hour)
            
            PM10_hour = row[11]
            if not_available(PM10_hour): 
                PM10_hour = np.nan
            list_PM10_hour.append(float(PM10_hour))
            #print(PM10_hour)


list_PM1_day = []
list_PM25_day = []
list_PM10_day = []
list_timestamp_sast_day = []

## Go through CSV file with DAILY QuantAQ data
with open(path_QuantAQ + 'MOD-PM-00523-day.csv', newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for i,row in enumerate(reader):
        if i > 0:
            timestamp_sast_day = row[0]
            timestamp_sast_day = timestamp_sast_day.replace("T", " ").replace("+02:00", "")
            timestamp_sast_day = datetime.strptime(timestamp_sast_day, '%Y-%m-%d %H:%M:%S')
            list_timestamp_sast_day.append(timestamp_sast_day)
            #print(timestamp_sast)
            
            PM1_day = row[9]
            if not_available(PM1_day): 
                PM1_day = np.nan
            list_PM1_day.append(float(PM1_day))
            #print(PM1_day)
            
            PM25_day = row[10]
            if not_available(PM25_day): 
                PM25_day = np.nan
            list_PM25_day.append(float(PM25_day))
            #print(PM25_day)
            
            PM10_day = row[11]
            if not_available(PM10_day): 
                PM10_day = np.nan
            list_PM10_day.append(float(PM10_day))
            #print(PM10_day)


## PM1 Plots
## PM1 RAW Data
# plt.scatter(list_timestamp_sast_raw, list_PM1_raw, alpha=0.5, marker="x")
# #plt.ylim(0, 100)
# plt.xticks(rotation=45, ha='right')
# plt.xlabel("Date")
# plt.ylabel("PM$_{1}$ ($\mu$g/m$^3$)")
# plt.title("PM$_{1}$ Raw Data")
# #plt.locator_params(axis='x', nbins=12)
# plt.grid()


## PM1 HOURLY Data
# plt.scatter(list_timestamp_sast_hour, list_PM1_hour)
# #plt.ylim(0, 100)
# plt.xticks(rotation=45, ha='right')
# plt.xlabel("Date")
# plt.ylabel("PM$_{1}$ ($\mu$g/m$^3$)")
# plt.title("PM$_{1}$ Hourly Data")
# #plt.locator_params(axis='x', nbins=12)
# plt.grid()

## PM1 DAILY Data
# plt.scatter(list_timestamp_sast_day, list_PM1_day)
# #plt.ylim(0, 100)
# plt.xticks(rotation=45, ha='right')
# plt.xlabel("Date")
# plt.ylabel("PM$_{1}$ ($\mu$g/m$^3$)")
# plt.title("PM$_{1}$ Daily Data")
# #plt.locator_params(axis='x', nbins=12)
# plt.grid()


## PM25 Plots
## PM25 Raw Data
# plt.scatter(list_timestamp_sast_raw, list_PM1_raw, alpha=0.5, marker="x")
# #plt.ylim(0, 100)
# plt.xticks(rotation=45, ha='right')
# plt.xlabel("Date")
# plt.ylabel("PM$_{2.5}$ ($\mu$g/m$^3$)")
# plt.title("PM$_{2.5}$ Raw Data")
# #plt.locator_params(axis='x', nbins=12)
# plt.grid()


# # PM25 HOURLY Data
# plt.scatter(list_timestamp_sast_hour, list_PM1_hour)
# #plt.ylim(0, 100)
# plt.xticks(rotation=45, ha='right')
# plt.xlabel("Date")
# plt.ylabel("PM$_{2.5}$ ($\mu$g/m$^3$)")
# plt.title("PM$_{2.5}$ Hourly Data")
# #plt.locator_params(axis='x', nbins=12)
# plt.grid()

# # PM25 DAILY Data
# plt.scatter(list_timestamp_sast_day, list_PM1_day)
# #plt.ylim(0, 100)
# plt.xticks(rotation=45, ha='right')
# plt.xlabel("Date")
# plt.ylabel("PM$_{2.5}$ ($\mu$g/m$^3$)")
# plt.title("PM$_{2.5}$ Daily Data")
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


# ## PM10 HOURLY Data
# plt.scatter(list_timestamp_sast_hour, list_PM10_hour)
# #plt.ylim(0, 100)
# plt.xticks(rotation=45, ha='right')
# plt.xlabel("Date")
# plt.ylabel("PM$_{10}$ ($\mu$g/m$^3$)")
# plt.title("PM$_{10}$ Hourly Data")
# #plt.locator_params(axis='x', nbins=12)
# plt.grid()

# ## PM10 DAILY Data
# plt.scatter(list_timestamp_sast_day, list_PM10_day)
# #plt.ylim(0, 100)
# plt.xticks(rotation=45, ha='right')
# plt.xlabel("Date")
# plt.ylabel("PM$_{10}$ ($\mu$g/m$^3$)")
# plt.title("PM$_{10}$ Daily Data")
# #plt.locator_params(axis='x', nbins=12)
# plt.grid()


### Code
# =============================================================================
# list_PM1_raw = []
# list_PM25_raw = []
# list_date = []
# list_time = []
# list_timestamp = []
# list_dt_timestamp = []

# list_PM1_hour = []
# list_PM25_hour = []
# list_date_hour = []

# list_PM1_day = []
# list_PM25_day = []
# list_date_day = []

# list_PM1_min = []
# list_PM25_min = []

# list_PM1_max = []
# list_PM25_max = []

# sumPM1 = 0
# valid_PM1 = 0

# sumPM25 = 0
# valid_PM25 = 0


# large_PM1 = -float('inf')
# small_PM1 = float('inf')

# large_PM25 = -float('inf')
# small_PM25 = float('inf')

# ## Test how to go through one 2BTech File 
# with open('data.csv', newline='') as csv_file:
#     reader = csv.reader(csv_file, delimiter=',')
    
#     previous_row = None
#     #previous_N02 = None
#     for row in reader:
#             if previous_row is not None:
#                 #print(row)
#                 current_value = float(row[16].split("-")[2])
#                 previous_value = float(previous_row[16].split("-")[2])
#                 diff = current_value - previous_value
#                 #print(i, difference, row) 
#                 #large_N02 = 
#                 #small_N02 = 
#                 PM1 = row[3]
#                 PM25 = row[4]
#                 date = row[16]
#                 previous_date = previous_row[16]
#                 time = row[17]
#                 timestamp = date + " " + time
#                 dt_timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
#                 hour = time.split(':')[0]
#                 minute = time.split(':')[1]
#                 second = time.split(':')[2]
#                 #print(tifindme, hour, minute, second)
#                 #date_obj = datetime.strptime(date_str, date_format)
#                 # list_N02_raw.append(float(N02))
#                 # list_PM1_raw.append(float(PM1))
#                 # list_PM25_raw.append(float(PM25))
#                 # list_C02_raw.append(float(C02))
#                 # list_Ozone_raw.append(float(Ozone))
                
#                 list_date.append(date)
#                 #list_timestamp.append(timestamp)
#                 list_dt_timestamp.append(dt_timestamp)
                

#                 #PM1 if statements
#                 if not_available(PM1): 
#                     PM1 = None
                
#                 if PM1 == None:
#                     list_PM1_raw.append((PM1))
#                 if PM1 != None:
#                     list_PM1_raw.append(float(PM1))
#                     PM1 = float(PM1)
                    
#                 if diff > 0 or diff < 0:
#                     avgPM1 = sumPM1/valid_PM1
#                     minPM1 = small_PM1
#                     maxPM1 = large_PM1
#                     #print(avgN02, previous_date)
#                     #list_averages.append(previous_date)
#                     #list_date_avg.append(previous_date)
#                     list_PM1_avg.append(avgPM1)
#                     list_PM1_min.append(minPM1)
#                     list_PM1_max.append(maxPM1)
#                     sumPM1 = 0 #resart after the 24 hours
#                     valid_PM1 = 0
#                     large_PM1 = -float('inf')
#                     small_PM1 = float('inf')
#                     if PM1 == None:
#                         sumPM1 += 0
#                     if PM1 != None:
#                         sumPM1 += float(PM1) 
#                 elif diff == 0 and PM1 == None:
#                     pass
#                 elif diff == 0 and PM1 != None:
#                     sumPM1 += float(PM1)        
#                     valid_PM1 += 1
                    
#                     if PM1 < small_PM1:
#                         small_PM1 = PM1
#                     elif PM1 > large_PM1:
#                         large_PM1 = PM1
                      
#                 #PM25 if statements
#                 if not_available(PM25): 
#                     PM25 = None
                
#                 if PM25 == None:
#                     list_PM25_raw.append((PM25))
#                 if PM25 != None:
#                     list_PM25_raw.append(float(PM25))
#                     PM25 = float(PM25)
                    
#                 if diff > 0 or diff < 0:
#                     avgPM25 = sumPM25/valid_PM25
#                     minPM25 = small_PM25
#                     maxPM25 = large_PM25
#                     #print(avgN02, previous_date)
#                     #list_averages.append(previous_date)
#                     #list_date_avg.append(previous_date)
#                     list_PM25_avg.append(avgPM25)
#                     list_PM25_min.append(minPM25)
#                     list_PM25_max.append(maxPM25)
#                     sumPM25 = 0 #resart after the 24 hours
#                     valid_PM25 = 0
#                     large_PM25 = -float('inf')
#                     small_PM25 = float('inf')
#                     if PM25 == None:
#                         sumPM25 += 0
#                     if PM25 != None:
#                         sumPM25 += float(PM25) 
#                 elif diff == 0 and PM25 == None:
#                     pass
#                 elif diff == 0 and PM25 != None:
#                     sumPM25 += float(PM25)        
#                     valid_PM25 += 1
                    
#                     if PM25 < small_PM25:
#                         small_PM25 = PM25
#                     elif PM25 > large_PM25:
#                         large_PM25 = PM25
                     
#             previous_row = row      
# =============================================================================
