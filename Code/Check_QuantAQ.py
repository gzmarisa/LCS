# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 12:12:58 2024

@author: u23993376
"""

# Import relevent libraries
import csv
import glob
import os
import matplotlib.pyplot as plt
from datetime import datetime

## Define functions
def empty(parameter):
    return len(parameter) == 0

def  not_available(parameter):
    return parameter == 'N/A'

def negative(parameter):
    return float(parameter) < 0

# Data paths 
path_QuantAQ = '../Data/QuantAQ/'



list_PM1_raw = []
list_PM25_raw = []
list_PM10_raw = []
list_timestamp_raw = []


# Go through CSV file with raw QuantAQ data
with open(path_QuantAQ + 'MOD-PM-00523-raw.csv', newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for i,row in enumerate(reader):
        if i > 0 and i < 10:
            timestamp = row[1]
            timestamp = timestamp.replace("T", " ").replace("Z", "")
            timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
            print(timestamp)
            PM1 = row[11]
            list_PM1_raw.append(float(PM1))
            print(PM1)
            PM25 = row[12]
            list_PM25_raw.append(float(PM25))
            print(PM25)
            PM10 = row[13]
            list_PM10_raw.append(float(PM10))
            print(PM10)
          

            
            #list_date.append(date)
            #list_timestamp.append(timestamp)
                
            


list_PM1_hour = []
list_PM25_hour = []
list_PM10_hour = []
list_timestamp_hour = []

# Go through CSV file with hourly QuantAQ data
# with open(path_QuantAQ + 'MOD-PM-00523-hour.csv', newline='') as csv_file:
#     reader = csv.reader(csv_file, delimiter=',')
#     for i,row in enumerate(reader):
#         if i > 0 and i < 10:
#             timestamp_hour = row[1]
#             #timestamp.datetime.toISOString().replace('Z', '').replace('T', '');
#             #date = timestamp.split(' ')[0]
#             print(timestamp)
#             PM1_hour = row[11]
#             list_PM1_hour.append(float(PM1_hour))
#             print(PM1)
#             PM25_hour = row[12]
#             list_PM25_hour.append(float(PM25_hour)
#             print(PM25_hour)
#             PM10_hour = row[13]
#             list_PM10_hour.append(float(PM10_hour))
#             print(PM10_hour)


list_PM1_day = []
list_PM25_day = []
list_PM10_day = []
list_timestamp_day = []

# Go through CSV file with hourly QuantAQ data
# with open(path_QuantAQ + 'MOD-PM-00523-day.csv', newline='') as csv_file:
#     reader = csv.reader(csv_file, delimiter=',')
#     for i,row in enumerate(reader):


## PM1 Plots
## PM1 Raw Data
# plt.scatter(list_dt_timestamp, list_PM1_raw, alpha=0.5, marker="x")
# #plt.ylim(0, 100)
# plt.xticks(rotation=45, ha='right')
# plt.xlabel("Date")
# plt.ylabel("PM$_{1}$ ($\mu$g/m$^3$)")
# plt.title("PM$_{1}$ Raw Data")

# #plt.locator_params(axis='x', nbins=12)
# plt.grid()

## PM1 Daily Data
# plt.scatter(list_date_avg, list_PM1_min)
# plt.scatter(list_date_avg, list_PM1_avg, color="red")
# plt.scatter(list_date_avg, list_PM1_max, color="green")
# #plt.xticks(range(len(list_C0_raw)), list_timestamp)
# plt.xticks(range(len(list_PM1_avg)), list_date_avg)
# #plt.xticks(rotation=45)
# #plt.ylim(0, 100)
# plt.xlabel("Date")
# plt.ylabel("PM$_{1}$ ($\mu$g/m$^3$)")
# # plt.title("PM$_{1}$ Daily Data")
# plt.xticks(rotation=45, ha='right')
# plt.locator_params(axis='x', nbins=12)
# plt.grid()
# plt.legend(['Miniumum', 'Average', "Maximum"])

## PM25 Plots
## PM25 Raw Data
# plt.scatter(list_dt_timestamp, list_PM25_raw, alpha=0.5, marker="x")
# #plt.ylim(0, 100)
# plt.xticks(rotation=45, ha='right')
# plt.xlabel("Date")
# plt.ylabel("PM$_{2.5}$ ($\mu$g/m$^3$)")
# plt.title("PM$_{2.5}$ Raw Data")
# #plt.locator_params(axis='x', nbins=12)
# plt.grid()

## PM25 Daily Data
# plt.scatter(list_date_avg, list_PM25_min)
# plt.scatter(list_date_avg, list_PM25_avg, color="red")
# plt.scatter(list_date_avg, list_PM25_max, color="green")
# plt.xticks(range(len(list_PM25_avg)), list_date_avg)
# #plt.ylim(0, 100)
# plt.xlabel("Date")
# plt.ylabel("PM$_{2.5}$ ($\mu$g/m$^3$)")
# plt.title("PM$_{2.5}$ Daily Data")
# plt.xticks(rotation=45, ha='right')
# plt.locator_params(axis='x', nbins=12)
# plt.grid()
# plt.legend(['Miniumum', 'Average', "Maximum"])

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
