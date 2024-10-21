
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
#path_2BTech = '../Data/2BTech/'
path_2BTech = '../Data/20241010_SD_Exact'

# Go throughall files in the directory 
#Use a wildcard pattern to match all CSV files in the directory
files_2BTech = glob.glob(path_2BTech + '*.txt')
files_2BTech.sort(key=os.path.getmtime)

combined_data_2BTech = []
for filename in files_2BTech:
    filepath = filename
#    print(filepath)
    with open(filepath, newline='') as txt_file:
        reader = csv.reader(txt_file, delimiter=',')

        counter = 0
        for row in reader:
            if counter > 2:
                combined_data_2BTech.append(row)
                
            counter += 1

with open('20241021_2BTech_Data.csv', 'a', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(combined_data_2BTech)
    

# list_N02_raw = []
# list_C0_raw = []
# list_PM1_raw = []
# list_PM25_raw = []
# list_C02_raw = []
# list_Ozone_raw = []
# list_date = []
# list_time = []
# list_timestamp = []
# list_dt_timestamp = []

# list_N02_avg = []
# list_C0_avg = []
# list_PM1_avg = []
# list_PM25_avg = []
# list_C02_avg = []
# list_Ozone_avg = []
# list_date_avg = []

# list_N02_min = []
# list_C0_min = []
# list_PM1_min = []
# list_PM25_min = []
# list_C02_min = []
# list_Ozone_min = []
# #list_date_min = []

# list_N02_max = []
# list_C0_max = []
# list_PM1_max = []
# list_PM25_max = []
# list_C02_max = []
# list_Ozone_max = []

# sumN02 = 0
# valid_N02 = 0

# sumC0 = 0
# valid_C0 = 0

# sumPM1 = 0
# valid_PM1 = 0

# sumPM25 = 0
# valid_PM25 = 0

# sumC02 = 0
# valid_C02 = 0

# sumOzone = 0
# valid_Ozone = 0

# large_N02 = -float('inf')
# small_N02 = float('inf')

# large_C0 = -float('inf')
# small_C0 = float('inf')

# large_PM1 = -float('inf')
# small_PM1 = float('inf')

# large_PM25 = -float('inf')
# small_PM25 = float('inf')

# large_C02 = -float('inf')
# small_C02 = float('inf')

# large_Ozone = -float('inf')
# small_Ozone = float('inf')

# ## Test how to go through one 2BTech File 
# with open('20241021_2BTech_Data.csv', newline='') as csv_file:
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
#                 previous_N02 = previous_row[1]
#                 N02 = row[1]
#                 #large_N02 = 
#                 #small_N02 = 
#                 C0 = row[2]
#                 PM1 = row[3]
#                 PM25 = row[4]
#                 C02 = row[6]
#                 Ozone = row[10]
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
                
#                 if not_available(N02): 
#                     N02 = None
                
#                 if N02 == None:
#                     list_N02_raw.append((N02))
#                 if N02 != None:
#                     list_N02_raw.append(float(N02))
#                     N02 = float(N02)
#                 if diff > 0 or diff < 0:
#                     avgN02 = sumN02/valid_N02
#                     minN02 = small_N02
#                     maxN02 = large_N02
#                     #print(avgN02, previous_date)
#                     #list_averages.append(previous_date)
#                     list_date_avg.append(previous_date)
#                     list_N02_avg.append(avgN02)
#                     list_N02_min.append(minN02)
#                     list_N02_max.append(maxN02)
#                     sumN02 = 0 #resart after the 24 hours
#                     valid_N02 = 0
#                     large_N02 = -float('inf')
#                     small_N02 = float('inf')
#                     if N02 == None:
#                         sumN02 += 0
#                     if N02 != None:
#                         sumN02 += float(N02) 
#                 elif diff == 0 and N02 == None:
#                     pass
#                 elif diff == 0 and N02 != None:
#                     sumN02 += float(N02)        
#                     valid_N02 += 1
                    
#                     if N02 < small_N02:
#                         small_N02 = N02
#                     elif N02 > large_N02:
#                         large_N02 = N02
                    
                
#                 #C0 if statements    
#                 if not_available(C0): 
#                     C0 = None
                
#                 if C0 == None:
#                     list_C0_raw.append((C0))
#                 if C0 != None:
#                     list_C0_raw.append(float(C0))
#                     C0 = float(C0)
                    
#                 if diff > 0 or diff < 0:
#                     avgC0 = sumC0/valid_C0
#                     minC0 = small_C0
#                     maxC0 = large_C0
#                     #print(avgN02, previous_date)
#                     #list_averages.append(previous_date)
#                     #list_date_avg.append(previous_date)
#                     list_C0_avg.append(avgC0)
#                     list_C0_min.append(minC0)
#                     list_C0_max.append(maxC0)
#                     sumC0 = 0 #resart after the 24 hours
#                     valid_C0 = 0
#                     large_C0 = -float('inf')
#                     small_C0 = float('inf')
#                     if C0 == None:
#                         sumC0 += 0
#                     if C0 != None:
#                         sumC0 += float(C0) 
#                 elif diff == 0 and C0 == None:
#                     pass
#                 elif diff == 0 and C0 != None:
#                     sumC0 += float(C0)        
#                     valid_C0 += 1
                    
#                     if C0 < small_C0:
#                         small_C0 = C0
#                     elif C0 > large_C0:
#                         large_C0 = C0

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
                      
#                 #C02 if statements
#                 if not_available(C02): 
#                     C02 = None
                
#                 if C02 == None:
#                     list_C02_raw.append((C02))
#                 if C02 != None:
#                     list_C02_raw.append(float(C02))
#                     C02 = float(C02)
                    
#                 if diff > 0 or diff < 0:
#                     if valid_C02 == 0:
#                         avg_C02 = None
#                     if valid_C02 != 0:
#                         avgC02 = sumC02/valid_C02
#                     minC02 = small_C02
#                     maxC02 = large_C02
#                         #print(avgN02, previous_date)
#                         #list_averages.append(previous_date)
#                         #list_date_avg.append(previous_date)
#                     list_C02_avg.append(avgC02)
#                     list_C02_min.append(minC02)
#                     list_C02_max.append(maxC02)
#                     sumC02 = 0 #resart after the 24 hours
#                     valid_C02 = 0
#                     large_C02 = -float('inf')
#                     small_C02 = float('inf')
                    
#                     if C02 == None:
#                         sumC02 += 0
#                     if C02 != None:
#                         sumC02 += float(C02) 
#                 elif diff == 0 and C02 == None:
#                     pass
#                 elif diff == 0 and C02 != None:
#                     sumC02 += float(C02)        
#                     valid_C02 += 1
                    
#                     if C02 < small_C02:
#                         small_C02 = C02
#                     elif C02 > large_C02:
#                         large_C02 = C02
                      
#                 #Ozone if statements 
#                 if not_available(Ozone): 
#                     Ozone = None
                
#                 if Ozone == None:
#                     list_Ozone_raw.append((Ozone))
#                 if Ozone != None:
#                     list_Ozone_raw.append(float(Ozone))
#                     Ozone = float(Ozone)
                    
#                 if diff > 0 or diff < 0:
#                     if valid_Ozone == 0:
#                         avgOzone = None
#                     if valid_Ozone != 0:
#                         avgOzone = sumOzone/valid_Ozone
#                     #avgOzone = sumOzone/valid_Ozone
#                     minOzone = small_Ozone
#                     maxOzone = large_Ozone
#                     #print(avgN02, previous_date)
#                     #list_averages.append(previous_date)
#                     #list_date_avg.append(previous_date)
#                     list_Ozone_avg.append(avgOzone)
#                     list_Ozone_min.append(minOzone)
#                     list_Ozone_max.append(maxOzone)
#                     sumOzone = 0 #resart after the 24 hours
#                     valid_Ozone = 0
#                     large_Ozone = -float('inf')
#                     small_Ozone = float('inf')
#                     if Ozone == None:
#                         sumOzone += 0
#                     if Ozone != None:
#                         sumOzone += float(Ozone) 
#                 elif diff == 0 and Ozone == None:
#                     pass
#                 elif diff == 0 and Ozone != None:
#                     sumOzone += float(Ozone)        
#                     valid_Ozone += 1
                    
#                     if Ozone < small_Ozone:
#                         small_Ozone = Ozone
#                     elif Ozone > large_Ozone:
#                         large_Ozone = Ozone
                      
                     
                
#             previous_row = row                        

## NO2 Plots 
## N02 Raw Data     
plt.scatter(list_dt_timestamp, list_N02_raw, alpha=0.5, marker="x")
#plt.xticks(range(len(list_N02_raw)), list_date_avg)
# #plt.xticks(rotation=45)
#plt.ylim(-200, 200)
plt.xticks(rotation=45, ha='right')
plt.xlabel("Date")
plt.ylabel("NO$_{2}$ (ppb)")
plt.title("NO$_{2}$ Raw Data")

#plt.locator_params(axis='x', nbins=12)
plt.grid()


## NO2 Daily average
#plt.scatter(list_timestamp, list_N02_raw, alpha=0.5, marker="x")
# plt.scatter(list_date_avg, list_N02_min)
# plt.scatter(list_date_avg, list_N02_avg, color="red")
# plt.scatter(list_date_avg, list_N02_max, color="green")
# #plt.xticks(range(len(list_N02_raw)), list_timestamp)
# plt.xticks(range(len(list_N02_avg)), list_date_avg)
# #plt.xticks(rotation=45)
# plt.ylim(-200, 200)
# plt.xlabel("Date")
# plt.ylabel("NO$_{2}$ (ppb)")
# plt.title("NO$_{2}$ Daily Data")
# plt.xticks(rotation=45, ha='right')
# plt.locator_params(axis='x', nbins=12)
# plt.grid()
# plt.legend(['Miniumum', 'Average', "Maximum"])

## Co Plots
## CO Raw Data     
## plot with C0
# plt.scatter(list_dt_timestamp, list_C0_raw, alpha=0.5, marker="x")
# #plt.xticks(range(len(list_C0_raw)), list_date_avg)
# # #plt.xticks(rotation=45)
# plt.ylim(-2, 2)
# plt.xticks(rotation=45, ha='right')
# plt.xlabel("Date")
# plt.ylabel("CO$ (ppm)")
# plt.title("CO Raw Data")
# #plt.locator_params(axis='x', nbins=12)
# plt.grid()


## CO Daily Data
# #plt.scatter(list_timestamp, list_C0_raw, alpha=0.5, marker="x")
# plt.scatter(list_date_avg, list_C0_min)
# plt.scatter(list_date_avg, list_C0_avg, color="red")
# plt.scatter(list_date_avg, list_C0_max, color="green")
# #plt.xticks(range(len(list_C0_raw)), list_timestamp)
# plt.xticks(range(len(list_C0_avg)), list_date_avg)
# #plt.xticks(rotation=45)
# plt.ylim(-2, 2)
# plt.xlabel("Date")
# plt.ylabel("CO (ppm)")
# plt.title("CO Daily Data")
# plt.xticks(rotation=45, ha='right')
# plt.locator_params(axis='x', nbins=12)
# plt.grid()
# plt.legend(['Miniumum', 'Average', "Maximum"])

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

## C02 Data
## C02 Raw Data
# plt.scatter(list_dt_timestamp, list_C02_raw, alpha=0.5, marker="x")
# #plt.xticks(range(len(list_C0_raw)), list_date_avg)
# # #plt.xticks(rotation=45)
# #plt.ylim(-2, 2)
# plt.xticks(rotation=45, ha='right')
# plt.xlabel("Date")
# plt.ylabel("CO$_{2}$ (ppm)")
# plt.title("CO$_{2}$ Raw Data")
# #plt.locator_params(axis='x', nbins=12)
# plt.grid()

## C02 Daily Data 
# plt.scatter(list_date_avg, list_C02_min)
# plt.scatter(list_date_avg, list_C02_avg, color="red")
# plt.scatter(list_date_avg, list_C02_max, color="green")
# plt.xticks(range(len(list_C0_avg)), list_date_avg)
# # #plt.ylim(0, 100)
# plt.xlabel("Date")
# plt.ylabel("CO2 (ppm)")
# plt.title("CO$_{2}$ Daily Data")
# plt.xticks(rotation=45, ha='right')
# plt.locator_params(axis='x', nbins=12)
# plt.grid()
# plt.legend(['Miniumum', 'Average', "Maximum"])

## Ozone Data
## Ozone Raw Data
# plt.scatter(list_dt_timestamp, list_Ozone_raw, alpha=0.5, marker="x")
# #plt.ylim(0, 100)
# plt.xticks(rotation=45, ha='right')
# plt.xlabel("Date")
# plt.ylabel("Ozone (ppb)")
# plt.title("Ozone Raw Data")
# #plt.locator_params(axis='x', nbins=12)
# plt.grid()

## Ozone Daily Data 
# plt.scatter(list_date_avg, list_Ozone_min)
# plt.scatter(list_date_avg, list_Ozone_avg, color="red")
# plt.scatter(list_date_avg, list_Ozone_max, color="green")
# plt.xticks(range(len(list_Ozone_avg)), list_date_avg)
# #plt.ylim(0, 100)
# plt.xlabel("Date")
# plt.ylabel("Ozone (ppb)")
# plt.title("Ozone Daily Data")
# plt.xticks(rotation=45, ha='right')
# plt.locator_params(axis='x', nbins=12)
# plt.grid()
# plt.legend(['Miniumum', 'Average', "Maximum"])


## Subplot with all PM1, PM25, N02, C0, C02, Ozone
# fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(6)
# ax1.scatter(list_date_avg, list_N02_avg)
# ax1.set_ylim(-200, 200)
# ax1.set_ylabel("NO$_{2}$")

# #ax2.subplot(6, 2)
# ax2.scatter(list_date_avg, list_C0_avg)
# ax2.set_ylabel("CO")

# #plt.subplot(6, 1, 3)
# ax3.scatter(list_date_avg, list_C02_avg)
# ax3.set_ylabel("CO$_{2}$")

# #plt.subplot(6, 1, 4)
# ax4.scatter(list_date_avg, list_Ozone_avg)
# ax4.set_ylabel("O$_{3}$")

# #plt.subplot(6, 1, 5)
# ax5.scatter(list_date_avg, list_PM1_avg)
# ax5.set_ylabel("PM$_{1}$ (ppb)")

# #plt.subplot(6, 1, 6)
# ax6.scatter(list_date_avg, list_PM25_avg)
# ax6.set_ylabel("PM$_{25}$ (ppb)")

# ax6.set_xlabel("Date")
# ax6.tick_params(axis='x', rotation=45)
# ax6.locator_params(axis='x', nbins=12)

### Code 
# =============================================================================
# ## Test how to go through one 2BTech File 
# with open('../Data/2BTech/1284_2023-12-1.txt', newline='') as txt_file:
#     reader = csv.reader(txt_file, delimiter=',')
    
#     started = False
#     counter = 0
#     sumN02 = 0
#     sumPM1 = 0
#     valid = 0
    

#     for row in reader:
#         if counter > 2:
#             N02 = row[1]
#             CO = row[2]
#             PM1 = row[3]
#             PM25 = row[4]
#             CO2 = row[6]
#             Ozone = row[10]
#             date = row[16]
#             time = row[17]
#             timestamp = date + " " + time
#             hour = time.split(':')[0]
#             minute = time.split(':')[1]
#             second = time.split(':')[2]
#             print(time, hour, minute, second)
#             list_N02_raw.append(float(N02))
#             list_PM1_raw.append(PM1)
#             list_PM25_raw.append(float(PM25))
#             list_date.append(date)
#             list_timestamp.append(timestamp)

# #            print(row)

#                 # #print(date, pms)
#             if not_available(N02): 
#                 N02 = None
#                 #print(row)
#             if int(hour) == 23 and int(minute) == 59 and int(second) == 59 and N02 != None:
#                 sumN02 += float(N02)
#                 avgN02 = sumN02/valid
#                 valid = 0
#                 print(date, avgN02, sumN02)
#                 sumN02 = 0 #resart after the 24 hours
#             elif int(hour) == 23 and int(minute) == 59 and int(second) == 59 and valid == 0:
#                 print(date, 0)
#                 sumN02 = 0
#             elif int(hour) == 23 and int(minute) == 59  and int(second) == 59 and  N02 == None:
#                 avgN02 = sumN02/valid
#                 valid = 0
#                 print(date, avgN02, sumN02)
#                 sumN02 = 0
             
#             elif int(hour) < 23 and int(minute) < 59 and  N02 != None:
#                 sumN02 += float(N02)        
#                 valid += 1
#                 #print(date, avgN02)

#         counter += 1
# =============================================================================
## How to split up the date and time in the row loop   
## if counter > 2 and counter < 10:
#            print(row)
            # print(i, counter, row)
            # date = row[16]
            # day = date.split("-")[2]
            # #print(date, day)
            # time = row[17]
            # hour = time.split(':')[0]
            # minute = time.split(':')[1]
            # second = time.split(':')[2]
            # timestamp = date + " " + time
# =============================================================================
  ## Different if/elif statement versions using the difference between day method 
#          if diff == 0 and Ozone != None:
  #               sumOzone += float(Ozone)        
  #               valid += 1
  #            #   print(date, avgN02)
  #            #   print(date, avgN02)
  #               print(i, SumOzone, valid)  
  #           elif diff == 0 and Ozone == None:
  #               pass
  # #             avgOzone = sumOzone/valid
  # #              valid = 0
  #              # print(date, avgN02, sumN02)
  # #              sumOzone = 0
  #           elif diff == 1:
  #               avgOzone = sumOzone/valid
  #               print(avgOzone)
  #          #     sumOzone = 0 #resart after the 24 hours
                
  #           # elif diff == 1 and  N02 == None:
  #           #     avgN02 = sumN02/valid
  #           #     valid = 0
  #           #     print(date, avgN02, sumN02)
  #           #     sumN02 = 0
  #           # elif diff == 1 and valid == 0:
  #           #       print(date, 0)
  #           #       sumN02 = 0
# =============================================================================
## Version of code where the taking the average of the day using the difference between the day 
## and if/elif statements 
## Test how to go through one 2BTech File 
# with open('../Data/2BTech/1284_2023-12-1.txt', newline='') as txt_file:
#     reader = csv.reader(txt_file, delimiter=',')
    
#     previous_row = None
#     for i,row in enumerate(reader):
#         if i > 2:
#             if previous_row is not None:
#                 #print(row)
#                 current_value = float(row[16].split("-")[2])
#                 previous_value = float(previous_row[16].split("-")[2])
#                 diff = current_value - previous_value
# #                print(i, difference, row) 
#                 N02 = row[1]
#                 CO = row[2]
#                 PM1 = row[3]
#                 PM25 = row[4]
#                 CO2 = row[6]
#                 Ozone = row[10]
#                 date = row[16]
#                 time = row[17]
#                 timestamp = date + " " + time
#                 hour = time.split(':')[0]
#                 minute = time.split(':')[1]
#                 second = time.split(':')[2]
             
#                 if not_available(Ozone): 
#                    Ozone = None
                
#                 if diff == 1:
#                    avgOzone = sumOzone/valid
#                    print(avgOzone)
#                    sumOzone = 0 #resart after the 24 hours
#                    sumOzone += float(Ozone)  
#                 elif diff == 0 and Ozone == None:
#                    pass
#                 elif diff == 0 and Ozone != None:
#                       sumOzone += float(Ozone)        
#                       valid += 1
#                    #   print(date, avgN02)
#                    #   print(date, avgN02)
                
#             previous_row = row                        

# =============================================================================
# How to iterate through the rows and elements using csv.reader()
#      for i,row in enumerate(reader):
#         for j,element in enumerate(row): 

# =============================================================================
# # Go throught all files in the directory 
# Use a wildcard pattern to match all CSV files in the directory
# files_2BTech = glob.glob(path_2BTech + '*.txt')
# files_2BTech.sort(key=os.path.getmtime)
# #files_2BTech =os.path.getmtime


# combined_data_2BTech = []
# for filename in files_2BTech:
#     filepath = filename
#     #print(filepath)
#     with open(filepath, newline='') as txt_file:
#         csv_reader = csv.reader(txt_file, delimiter=',')
    
#             #started_2BTech = False
#         counter_2BTech = 0
#             #SumPms_2BTech = 0
#             #valid_2BTech = 0
#         for row in csv_reader:
#             if counter_2BTech > 2:
#                 combined_data_2BTech.append(row)
                
#             counter_2BTech += 1

# =============================================================================
# ## Test how to go through one 2BTech File 
# with open('../Data/2BTech/1284_2023-12-1.txt', newline='') as txt_file:
#     reader = csv.reader(txt_file, delimiter=',')
    
#     previous_row = None
#     for i,row in enumerate(reader):
#         if i > 2:
#             if previous_row is not None:
#                 #print(row)
#                 current_value = float(row[16].split("-")[2])
#                 previous_value = float(previous_row[16].split("-")[2])
#                 diff = current_value - previous_value
#                 #print(i, difference, row) 
#                 N02 = row[1]
#                 C0 = row[2]
#                 PM1 = row[3]
#                 PM25 = row[4]
#                 C02 = row[6]
#                 Ozone = row[10]
#                 date = row[16]
#                 previous_date = previous_row[16]
#                 time = row[17]
#                 timestamp = date + " " + time
#                 hour = time.split(':')[0]
#                 minute = time.split(':')[1]
#                 second = time.split(':')[2]
#                 #print(time, hour, minute, second)
#                 list_N02_raw.append(float(N02))
#                 list_C0_raw.append(float(C0))
#                 list_PM1_raw.append(float(PM1))
#                 list_PM25_raw.append(float(PM25))
#                 list_C02_raw.append(float(C02))
#                 list_Ozone_raw.append(float(Ozone))
                
#                 list_date.append(date)
#                 list_timestamp.append(timestamp)
                
#                 if not_available(N02): 
#                     N02 = None
#                 if diff > 0 or diff < 0:
#                     avgN02 = sumN02/valid_N02
#                     print(avgN02)
#                     #list_averages.append(previous_date)
#                     list_date_avg.append(previous_date)
#                     list_N02_avg.append(avgN02)
#                     sumN02 = 0 #resart after the 24 hours
#                     sumN02 += float(N02)  
#                 elif diff == 0 and N02 == None:
#                     pass
#                 elif diff == 0 and N02 != None:
#                     sumN02 += float(N02)        
#                     valid_N02 += 1
                 
#                 if not_available(C0): 
#                     C0 = None
#                 if diff > 0 or diff < 0:
#                     avgC0 = sumC0/valid_C0
#                     #print(avgC0)
#                     list_C0_avg.append(avgC0)
#                     sumC0 = 0 #resart after the 24 hours
#                     sumC0 += float(C0)  
#                 elif diff == 0 and C0 == None:
#                      pass
#                 elif diff == 0 and C0 != None:
#                        sumC0 += float(C0)        
#                        valid_C0 += 1

               
#                 if not_available(PM1): 
#                     PM1 = None
#                 if diff > 0 or diff < 0:
#                     avgPM1 = sumPM1/valid_PM1
#                     #print(avgPM1)
#                     list_PM1_avg.append(avgPM1)
#                     sumPM1 = 0 #resart after the 24 hours
#                     sumPM1 += float(PM1)  
#                 elif diff == 0 and PM1 == None:
#                     pass
#                 elif diff == 0 and PM1 != None:
#                       sumPM1 += float(PM1)        
#                       valid_PM1 += 1
               
#                 if not_available(PM25): 
#                     PM25 = None
#                 if diff > 0 or diff < 0:
#                     avgPM25 = sumPM25/valid_PM25
#                     #print(avgPM25)
#                     list_PM25_avg.append(avgPM25)
#                     sumPM25 = 0 #resart after the 24 hours
#                     sumPM25 += float(PM25)  
#                 elif diff == 0 and PM25 == None:
#                     pass
#                 elif diff == 0 and PM25 != None:
#                       sumPM25 += float(PM25)        
#                       valid_PM25 += 1
                
#                 if not_available(C02): 
#                     C02 = None
#                 if diff > 0 or diff < 0:
#                     avgC02 = sumC02/valid_C02
#                     #print(avgC02)
#                     list_C02_avg.append(avgC02)
#                     sumC02 = 0 #resart after the 24 hours
#                     sumPM25 += float(C02)  
#                 elif diff == 0 and C02 == None:
#                     pass
#                 elif diff == 0 and C02 != None:
#                       sumC02 += float(C02)        
#                       valid_C02 += 1
                
#                 if not_available(Ozone): 
#                     Ozone = None
#                 if diff > 0 or diff < 0:
#                     avgOzone = sumOzone/valid
#                     #print(previous_date, avgOzone)
#                     list_Ozone_avg.append(avgOzone)
#                     sumOzone = 0 #resart after the 24 hours
#                     sumOzone += float(Ozone)  
#                 elif diff == 0 and Ozone == None:
#                     pass
#                 elif diff == 0 and Ozone != None:
#                       sumOzone += float(Ozone)        
#                       valid += 1
                
#             previous_row = row   

### Notes
## how to convert a string in a specific format to a datetime object
## Link: https://www.datacamp.com/tutorial/converting-strings-datetime-objects             
## date_obj = datetime.strptime(date_str, date_format)

                        