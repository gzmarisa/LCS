
# Import relevent libraries
import csv
import glob
import os
import matplotlib.pyplot as plt

## Define functions
def empty(parameter):
    return len(parameter) == 0

def  not_available(parameter):
    return parameter == 'N/A'

def negative(parameter):
    return float(parameter) < 0

# Data paths 
path_2BTech = '../Data/2BTech/'

# Go throught all files in the directory 
# Use a wildcard pattern to match all CSV files in the directory
files_2BTech = glob.glob(path_2BTech + '*.txt')
files_2BTech.sort(key=os.path.getmtime)

# combined_data_2BTech = []
# for filename in files_2BTech:
#     filepath = filename
# #    print(filepath)
#     with open(filepath, newline='') as txt_file:
#         reader = csv.reader(txt_file, delimiter=',')

#         counter = 0
#         for row in reader:
#             if counter > 2:
#                 combined_data_2BTech.append(row)
                
#             counter += 1

# with open('data.csv', 'a', newline='') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerows(combined_data_2BTech)
    

list_N02_raw = []
list_C0_raw = []
list_PM1_raw = []
list_PM25_raw = []
list_C02_raw = []
list_Ozone_raw = []
list_date = []
list_time = []
list_timestamp = []

list_N02_avg = []
list_C0_avg = []
list_PM1_avg = []
list_PM25_avg = []
list_C02_avg = []
list_Ozone_avg = []
list_date_avg = []

sumN02 = 0
valid_N02 = 0

sumC0 = 0
valid_C0 = 0

sumPM1 = 0
valid_PM1 = 0

sumPM25 = 0
valid_PM25 = 0

sumC02 = 0
valid_C02 = 0

sumOzone = 0
valid = 0

## Test how to go through one 2BTech File 
with open('data.csv', newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    
    previous_row = None
    for row in reader:
            if previous_row is not None:
                #print(row)
                current_value = float(row[16].split("-")[2])
                previous_value = float(previous_row[16].split("-")[2])
                diff = current_value - previous_value
                #print(i, difference, row) 
                N02 = row[1]
                C0 = row[2]
                PM1 = row[3]
                PM25 = row[4]
                C02 = row[6]
                Ozone = row[10]
                date = row[16]
                previous_date = previous_row[16]
                time = row[17]
                timestamp = date + " " + time
                hour = time.split(':')[0]
                minute = time.split(':')[1]
                second = time.split(':')[2]
                #print(time, hour, minute, second)
                
                # list_N02_raw.append(float(N02))
                # list_PM1_raw.append(float(PM1))
                # list_PM25_raw.append(float(PM25))
                # list_C02_raw.append(float(C02))
                # list_Ozone_raw.append(float(Ozone))
                
                list_date.append(date)
                list_timestamp.append(timestamp)
                
                if not_available(N02): 
                    N02 = None
                    
                if diff > 0 or diff < 0:
                    avgN02 = sumN02/valid_N02
                    #print(avgN02, previous_date)
                    #list_averages.append(previous_date)
                    list_date_avg.append(previous_date)
                    list_N02_avg.append(avgN02)
                    sumN02 = 0 #resart after the 24 hours
                    valid_N02 = 0
                    if N02 == None:
                        sumN02 += 0
                    if N02 != None:
                        sumN02 += float(N02) 
                elif diff == 0 and N02 == None:
                    pass
                elif diff == 0 and N02 != None:
                    sumN02 += float(N02)        
                    valid_N02 += 1
                 
                if not_available(C0): 
                    C0 = None
                if diff > 0 or diff < 0:
                    avgC0 = sumC0/valid_C0
                    #print(avgC0)
                    list_C0_avg.append(avgC0)
                    sumC0 = 0 #resart after the 24 hours
                    # if C0 == None:
                    #     sumC0 = 0
                    # if C0 != None:
                    #     sumC0 += float(C0)   
                elif diff == 0 and C0 == None:
                      pass
                elif diff == 0 and C0 != None:
                        sumC0 += float(C0)        
                        valid_C0 += 1

               
                if not_available(PM1): 
                    PM1 = None
                if diff > 0 or diff < 0:
                    avgPM1 = sumPM1/valid_PM1
                    #print(avgPM1)
                    list_PM1_avg.append(avgPM1)
                    sumPM1 = 0 #resart after the 24 hours
                    # if PM1 == None:
                    #     sumPM1 = 0
                    # if PM1 != None:
                    #     sumPM1 += float(PM1)  
                elif diff == 0 and PM1 == None:
                    pass
                elif diff == 0 and PM1 != None:
                      sumPM1 += float(PM1)        
                      valid_PM1 += 1
               
                if not_available(PM25): 
                    PM25 = None
                if diff > 0 or diff < 0:
                    avgPM25 = sumPM25/valid_PM25
                    #print(avgPM25)
                    list_PM25_avg.append(avgPM25)
                    sumPM25 = 0 #resart after the 24 hours
                    # if PM25 == None:
                    #     sumPM25 = 0
                    # if PM25 != None:
                    #     sumPM25 += float(PM25)   
                elif diff == 0 and PM25 == None:
                    pass
                elif diff == 0 and PM25 != None:
                      sumPM25 += float(PM25)        
                      valid_PM25 += 1
                
                if not_available(C02): 
                    C02 = None
                if diff > 0 or diff < 0:
                    avgC02 = sumC02/valid_C02
                    #print(avgC02)
                    list_C02_avg.append(avgC02)
                    sumC02 = 0 #resart after the 24 hours
                    # if C02 == None:
                    #     sumC02 = 0
                    # if C02 != None:
                    #     sumC02 += float(C02)  
                elif diff == 0 and C02 == None:
                    pass
                elif diff == 0 and C02 != None:
                      sumC02 += float(C02)        
                      valid_C02 += 1
                
                if not_available(Ozone): 
                    Ozone = None
                if diff > 0 or diff < 0:
                    avgOzone = sumOzone/valid
                    #print(previous_date, avgOzone)
                    list_Ozone_avg.append(avgOzone)
                    sumOzone = 0 #resart after the 24 hours
                    # if Ozone == None:
                    #     sumOzone = 0
                    # if Ozone != None:
                    #     sumOzone += float(Ozone)   
                elif diff == 0 and Ozone == None:
                    pass
                elif diff == 0 and Ozone != None:
                      sumOzone += float(Ozone)        
                      valid += 1
                
            previous_row = row                        

              
#plt.scatter(list_timestamp, list_N02_raw)
#plt.scatter(list_timestamp, list_PM25_raw)






### Notes 
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


                


                        