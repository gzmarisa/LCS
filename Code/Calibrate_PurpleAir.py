
## Upload relevant libraries
import csv
import csv
import glob
import os
import numpy as np 
import matplotlib.pyplot as plt
import datetime
#from datetime import datetime

## Define functions
def utc_to_sa(utc_dt):
  return utc_dt + datetime.timedelta(hours=2)

def  not_available(parameter):
    return parameter == ''

def empty(pm):
    return len(pm) == 0

def negative(pm):
    return float(pm) < 0


list_PA_PM25_raw = []
list_PA_timestamp_utc_raw = []
list_PA_timestamp_utc_raw = []

list_PA_PM25_avg_hour = []
list_PA_date_avg_hour = []
list_PA_timestamp_sast_hour = []

list_PA_PM25_avg_day = []
list_PA_date_avg_day = []
list_PA_timestamp_sast_day = []

sum_PM25_hour = 0
valid_PM25_hour = 0

sum_PM25_day = 0
valid_PM25_day = 0

with open('../Data/PurpleAir/CSIR_wel_eb7e/CSIR_wel_eb7e.csv', newline='') as PA_csv_file:
    PA_csv_reader = csv.reader(PA_csv_file, delimiter=',')
    
    #PA_started = False
    PA_counter = 0
    PA_SumPms = 0
    PA_valid = 0
    for row in PA_csv_reader:
        if PA_counter == 0:
            header = row
            #print(header)
        if PA_counter == 1:
            PM25 = row[3]
            if not_available(PM25): 
                PM25 = np.nan
            if PM25 == np.nan:    
                pass
            elif PM25 != np.nan:
                sum_PM25_day += float(PM25)      
                valid_PM25_day += 1

            previous_row = row
        if PA_counter > 1 and PA_counter < 2000:
            #print(row)
            previous_timestamp_utc_raw = previous_row[0]
            previous_timestamp_utc_raw = previous_timestamp_utc_raw.replace(" UTC", "")
            previous_timestamp_utc_raw = datetime.datetime.strptime(previous_timestamp_utc_raw, '%Y-%m-%d %H:%M:%S')
            previous_timestamp_sast_raw = utc_to_sa(previous_timestamp_utc_raw)
            
            previous_date = previous_timestamp_sast_raw.date()
            previous_hour = previous_timestamp_sast_raw.hour
            previous_day = previous_timestamp_sast_raw.day
            
            timestamp_utc_raw = row[0]
            timestamp_utc_raw = timestamp_utc_raw.replace(" UTC", "")
            timestamp_utc_raw = datetime.datetime.strptime(timestamp_utc_raw, '%Y-%m-%d %H:%M:%S')
            timestamp_sast_raw = utc_to_sa(timestamp_utc_raw)
            
            date = timestamp_sast_raw.date()
            hour = timestamp_sast_raw.hour
            day = timestamp_sast_raw.day
            
            diff_hour = hour - previous_hour
            diff_day = day - previous_day
            
            PM25 = row[3]
            list_PA_PM25_raw.append(float(PM25))

            
            if not_available(PM25): 
                PM25 = np.nan
            
            ## Hourly
            previous_timestamp_sast_hour  = previous_timestamp_sast_raw.strftime("%Y-%m-%d %H:00")
            previous_timestamp_sast_hour = datetime.datetime.strptime(previous_timestamp_sast_hour, "%Y-%m-%d %H:00")
            
            timestamp_sast_hour  = timestamp_sast_raw.strftime("%Y-%m-%d %H:00")
            timestamp_sast_hour = datetime.datetime.strptime(timestamp_sast_hour, "%Y-%m-%d %H:00")
            
            if diff_hour != 0:
                avg_PM25_hour = sum_PM25_hour/valid_PM25_hour
                #list_PA_date_avg_hour.append(previous_date)
                list_PA_timestamp_sast_hour.append(previous_timestamp_sast_hour)
                list_PA_PM25_avg_hour.append(avg_PM25_hour)
                print(timestamp_sast_hour)
                print(avg_PM25_hour)
                sumPM25_hour = 0 #resart after the 24 hours
                valid_PM25_hour = 0
            elif diff_hour == 0 and PM25 == np.nan:    
                pass
            elif diff_hour == 0 and PM25 != np.nan:
                sum_PM25_hour += float(PM25)      
                valid_PM25_hour += 1
        
            ## Daily
            if diff_day != 0:
                avg_PM25_day = sum_PM25_day/valid_PM25_day
                list_PA_date_avg_day.append(previous_date)
                list_PA_PM25_avg_day.append(avg_PM25_day)
                #print(previous_date)
                #print(avg_PM25_day)
                sumPM25_day = 0 #resart after the 24 hours
                valid_PM25_day = 0
            elif diff_day == 0 and PM25 == np.nan:    
                pass
            elif diff_day == 0 and PM25 != np.nan:
                sum_PM25_day += float(PM25)      
                valid_PM25_day += 1
                
            previous_row = row     
             
        PA_counter += 1



## Upload SAAQIS data

# with open('../Data/SAAQIS/Welgegund-NAQI/Welgegund.csv', newline='') as csvfile:
#     csv_reader = csv.reader(csvfile, delimiter=',')
    
#     started = False
#     counter = 0
#     sumPms = 0
#     valid = 0
#     for row in csv_reader: #row is the row of csv file
#         if counter > 6 and counter < 26285:       
#             #hour = row[0].split(" ")[0]
#             date = row[0].split(" ")[1]
#             if date == "01/10/2018" or started: #start date
#                 started = True
#                 date = date.split("/") 
#                 hour = row[0].split(" ")[0].split(":")[0]
#                 pms = row[1]
#                 #print(date, pms)
#                 if empty(pms) or negative(pms): # add function for weird values
#                     pms = None
#                 if int(hour) == 24 and pms != None:
#                     sumPms += float(pms)
#                     avgPms = sumPms/valid
#                     valid = 0
#                     print(date, avgPms)
                    
#                     sumPms = 0 #resart after the 24 hours
#                 elif int(hour) == 24 and valid == 0:
#                     print(date, 0)
#                     SumPms = 0
#                 elif int(hour) == 24 and pms == None:
#                     avgPms = sumPms/valid
#                     valid = 0
#                     print(date, avgPms)
#                     SumPms = 0
              
#                 elif int(hour) < 24 and pms != None:
#                     sumPms += float(pms)
#                     valid += 1


                
               
#         counter += 1
        

"""
if not negative(pm) and not nothing(pm) and not weird(pm)
x = None        
if int(hour) ==24 and pms != None
elif int(hour) < 24 and pms != None
"""
## Fix the 24:00 hour issue 

## Remove outliers from PA data
## Remove values from PM2.5 data

## Remove negative values
## Check for  high values 
## Remove high values
## Remove double values 

## Remove values from RH data
## Remove negative values
## Check for  high values 
## Remove high values
## Remove double values 

## Remove values from temperature data
## Remove negative values
## Check for  high values 
## Remove high values
## Remove double values 


## Remove outliers from SAAQIS data
## Remove values from PM2.5 data
## Remove negative values
## Check for  high values 
## Remove high values
## Remove double values 


# =============================================================================
# ## Upload PA data
# with open('../Data/PurpleAir/CSIR_wel_eb7e/CSIR_wel_eb7e.csv', newline='') as PA_csv_file:
#     PA_csv_reader = csv.reader(PA_csv_file, delimiter=',')
    
#     PA_started = False
#     PA_counter = 0
#     PA_SumPms = 0
#     PA_valid = 0
#     for row in PA_csv_reader:
#         if PA_counter < 10:
#             date = row[0].split(",")[0]
#             date = date.split(" ")
#             date = date.split(",")
#             print(date)
        
#         PA_counter += 1

# =============================================================================



