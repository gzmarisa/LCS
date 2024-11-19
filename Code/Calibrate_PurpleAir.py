
## Upload relevant libraries
import csv
import csv
import glob
import os
import numpy as np 
import matplotlib.pyplot as plt
import datetime
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

## Define functions
def utc_to_sa(utc_dt):
  return utc_dt + datetime.timedelta(hours=2)

def  not_available(parameter):
    return parameter == ''

def empty(parameter):
    return len(parameter) == 0

def negative(parameter):
    return float(parameter) < 0

# def lower_threshold_PA_RH(RH):
#     return float(RH) < [insert_value]

def upper_threshold_PA_RH(RH):
    return float(RH) > 99


def upper_threhold_PA_TEMP_F(TEMP_F):
    return float(TEMP_F) > 95

### 90 0r 95

def upper_threhold_PA_PM(PM): 
    return float(PM) > 200
    #return float(PM) > 1000

def upper_threhold_PM(PM):
    return float(PM) > 110


def f_to_c(temp_f):
    temp_f = float(temp_f)
    return (temp_f-32) * (5/9)

def PA_correction(PM, RH, TEMP_C):
    return (0.55936209*PM) + (-0.11083672*RH) + (-0.0922173*TEMP_C) + 10.182720629764873


def remove_nan_and_indices(list1, list2, list3, list4, list5):
    """Removes np.nan values from list1 and deletes corresponding indices in list2.

    Args:
        list1: The list containing np.nan values
        list2: The list whose indices will be deleted
        list3: the list whose indcides wil be deleted
        list4: the list whose indices will be delieted
        list5: the list whose indices will be delieved

    Returns:
        A tuple containing the modified list1 and list2.
    """

    indices_to_remove = []
    for i, value in enumerate(list1):
        if np.isnan(value):
            indices_to_remove.append(i)

    # Reverse the indices to avoid shifting during deletion
    indices_to_remove.reverse()

    for index in indices_to_remove:
        del list1[index]
        del list2[index]
        del list3[index]
        del list4[index]
        del list5[index]

    return list1, list2, list3, list4, list5


list_PA_PM25_raw = []
list_PA_RH_raw = []
list_PA_TEMP_F_raw = []
list_PA_TEMP_C_raw = []

list_PA_timestamp_utc_raw = []
list_PA_timestamp_sast_raw = []

list_PA_PM25_timestamp_sast_hour = []
list_PA_RH_timestamp_sast_hour = []
list_PA_TEMP_C_timestamp_sast_hour = []


list_PA_PM25_avg_hour = []
list_PA_RH_avg_hour = []
list_PA_TEMP_C_avg_hour = []

list_PA_date_avg_hour = []
list_PA_timestamp_sast_hour = []

list_PA_RH_date_avg_hour = []
list_PA_TEMP_C_date_avg_hour = []

list_PA_PM25_avg_day = []
list_PA_date_avg_day = []
list_PA_timestamp_sast_day = []

list_PA_RH_avg_day = []
list_PA_RH_date_avg_day = []
list_PA_RH_timestamp_sast_day = []

list_PA_TEMP_C_avg_day = []
list_PA_TEMP_C_date_avg_day = []
list_PA_TEMP_C_timestamp_sast_day = []

sum_PM25_hour = 0
sum_RH_hour = 0
sum_TEMP_C_hour = 0

valid_PM25_hour = 0
valid_RH_hour = 0
valid_TEMP_C_hour = 0

sum_PM25_day = 0
sum_RH_day = 0
sum_TEMP_C_day = 0

valid_PM25_day = 0
valid_RH_day = 0
valid_TEMP_C_day = 0

with open('../Data/PurpleAir/CSIR_wel_eb7e/CSIR_wel_eb7e.csv', newline='') as PA_csv_file:
    PA_csv_reader = csv.reader(PA_csv_file, delimiter=',')
    
    #PA_started = False
    PA_counter = 0
    #started_PM = False
    for row in PA_csv_reader:
        if PA_counter == 0:
            header = row
            #print(header)
        if PA_counter == 112880:
            PM25 = row[3]
            if not_available(PM25): 
                PM25 = np.nan
            if PM25 == np.nan:    
                pass
            elif PM25 != np.nan:
                sum_PM25_day += float(PM25)      
                valid_PM25_day += 1

            previous_row = row
        #if PA_counter > 1
        if PA_counter > 112880:
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
            list_PA_timestamp_sast_raw.append(timestamp_sast_raw)
            
            date = timestamp_sast_raw.date()
            hour = timestamp_sast_raw.hour
            day = timestamp_sast_raw.day
            
            diff_hour = hour - previous_hour
            diff_day = day - previous_day
            
            # start_date = datetime.date(2018, 10, 1)
            
            # if date == start_date or started_PM: #start date
            #     started_PM = True
            
            PM25 = row[3]
            TEMP_F = row[7]
            RH = row[8]
            
            # for PM25
            if not_available(PM25) or negative(PM25) or upper_threhold_PA_PM(PM25): 
                PM25 = np.nan
            

            # for RH
            if not_available(RH) or negative(RH) or upper_threshold_PA_RH(RH): 
                RH = np.nan
            
            #For TEMP_F
            if not_available(TEMP_F) or negative(TEMP_F) or upper_threhold_PA_TEMP_F(TEMP_F): 
                TEMP_F = np.nan
            
            list_PA_PM25_raw.append(float(PM25))
            list_PA_RH_raw.append(float(RH))
            list_PA_TEMP_F_raw.append(float(TEMP_F))
            
            TEMP_C = f_to_c(TEMP_F)
            list_PA_TEMP_C_raw.append(float(TEMP_F))
                
            ## Hourly
            previous_timestamp_sast_hour  = previous_timestamp_sast_raw.strftime("%Y-%m-%d %H:00")
            previous_timestamp_sast_hour = datetime.datetime.strptime(previous_timestamp_sast_hour, "%Y-%m-%d %H:00")
            
            timestamp_sast_hour  = timestamp_sast_raw.strftime("%Y-%m-%d %H:00")
            timestamp_sast_hour = datetime.datetime.strptime(timestamp_sast_hour, "%Y-%m-%d %H:00")
            
            if diff_hour != 0 and valid_PM25_hour != 0:
                avg_PM25_hour = sum_PM25_hour/valid_PM25_hour
                #list_PA_date_avg_hour.append(previous_date)
                list_PA_timestamp_sast_hour.append(previous_timestamp_sast_hour)
                list_PA_PM25_avg_hour.append(avg_PM25_hour)
                #print(timestamp_sast_hour)
                #print(avg_PM25_hour)
                sum_PM25_hour = 0 #resart after the 24 hours
                valid_PM25_hour = 0
            elif diff_hour != 0 and valid_PM25_hour == 0:
                avg_PM25_hour = np.nan
                #list_PA_date_avg_hour.append(previous_date)
                list_PA_timestamp_sast_hour.append(previous_timestamp_sast_hour)
                list_PA_PM25_avg_hour.append(avg_PM25_hour)
                #print(timestamp_sast_hour)
                #print(avg_PM25_hour)
                sum_PM25_hour = 0 #resart after the 24 hours
                #valid_PM25_hour = 0
            elif diff_hour == 0 and PM25 == np.nan:    
                pass
            elif diff_hour == 0 and PM25 != np.nan:
                sum_PM25_hour += float(PM25)      
                valid_PM25_hour += 1
            
            ## RH
            if diff_hour != 0 and valid_RH_hour != 0:
                avg_RH_hour = sum_RH_hour/valid_RH_hour
                list_PA_RH_timestamp_sast_hour.append(previous_timestamp_sast_hour)
                list_PA_RH_avg_hour.append(avg_RH_hour)
                
                sum_RH_hour = 0 #restart
                valid_RH_hour = 0
            elif diff_hour != 0 and valid_RH_hour == 0:
                avg_RH_hour = np.nan
                
                list_PA_RH_timestamp_sast_hour.append(previous_timestamp_sast_hour)
                list_PA_RH_avg_hour.append(avg_RH_hour)
                sum_RH_hour = 0 #resart 
                #valid_RG_hour = 0
            elif diff_hour == 0 and RH == np.nan:    
                pass
            elif diff_hour == 0 and RH != np.nan:
                sum_RH_hour += float(RH)      
                valid_RH_hour += 1
            
            ## TEMP_C
            if diff_hour != 0 and valid_TEMP_C_hour != 0:
                avg_TEMP_C_hour = sum_TEMP_C_hour/valid_TEMP_C_hour
                list_PA_TEMP_C_timestamp_sast_hour.append(previous_timestamp_sast_hour)
                list_PA_TEMP_C_avg_hour.append(avg_TEMP_C_hour)
                
                sum_TEMP_C_hour = 0 #restart
                valid_TEMP_C_hour = 0
            elif diff_hour != 0 and valid_TEMP_C_hour == 0:
                avg_TEMP_C_hour = np.nan
                
                list_PA_TEMP_C_timestamp_sast_hour.append(previous_timestamp_sast_hour)
                list_PA_TEMP_C_avg_hour.append(avg_TEMP_C_hour)
                sum_TEMP_C_hour = 0 #resart after the 24 hours
                valid_TEMP_C_hour = 0
            elif diff_hour == 0 and TEMP_C == np.nan:    
                pass
            elif diff_hour == 0 and TEMP_C != np.nan:
                sum_TEMP_C_hour += float(TEMP_C)      
                valid_TEMP_C_hour += 1
            
            
            ## Daily
            ## PM25
            if diff_day != 0 and valid_PM25_day != 0:
                avg_PM25_day = sum_PM25_day/valid_PM25_day
                list_PA_date_avg_day.append(previous_date)
                list_PA_PM25_avg_day.append(avg_PM25_day)

                sum_PM25_day = 0 #resart after the 24 hours
                valid_PM25_day = 0
            elif diff_day != 0 and valid_PM25_day == 0:
                avg_PM25_day = np.nan
                list_PA_date_avg_day.append(previous_date)
                list_PA_PM25_avg_hour.append(avg_PM25_hour)
                
                sum_PM25_day = 0 #resart after the 24 hours
                #valid_PM25_day  = 0
            elif diff_day == 0 and PM25 == np.nan:    
                pass
            elif diff_day == 0 and PM25 != np.nan:
                sum_PM25_day += float(PM25)      
                valid_PM25_day += 1
                
            ## RH
            if diff_day != 0 and valid_RH_day != 0:
                avg_RH_day = sum_RH_day/valid_RH_day
                list_PA_RH_date_avg_day.append(previous_date)
                list_PA_RH_avg_day.append(avg_RH_day)

                sum_RH_day = 0 #resart after the 24 hours
                valid_RH_day = 0
            elif diff_day != 0 and valid_RH_day == 0:
                avg_RH_day = np.nan
                list_PA_RH_date_avg_day.append(previous_date)
                list_PA_RH_avg_hour.append(avg_RH_hour)
                
                sum_RH_day = 0 #resart after the 24 hours
                #valid_PM25_day  = 0
            elif diff_day == 0 and RH == np.nan:    
                pass
            elif diff_day == 0 and RH != np.nan:
                sum_RH_day += float(RH)      
                valid_RH_day += 1
                
            ## TEMP_C
            if diff_day != 0 and valid_TEMP_C_day != 0:
                avg_TEMP_C_day = sum_TEMP_C_day/valid_TEMP_C_day
                list_PA_TEMP_C_date_avg_day.append(previous_date)
                list_PA_TEMP_C_avg_day.append(avg_TEMP_C_day)

                sum_TEMP_C_day = 0 #resart after the 24 hours
                valid_TEMP_C_day = 0
            elif diff_day != 0 and valid_TEMP_C_day == 0:
                avg_TEMP_C_day = np.nan
                list_PA_TEMP_C_date_avg_day.append(previous_date)
                list_PA_TEMP_C_avg_hour.append(avg_TEMP_C_hour)
                
                sum_TEMP_C_day = 0 #resart after the 24 hours
                #valid_PM25_day  = 0
            elif diff_day == 0 and TEMP_C == np.nan:    
                pass
            elif diff_day == 0 and TEMP_C != np.nan:
                sum_TEMP_C_day += float(RH)      
                valid_TEMP_C_day += 1
            
            
            previous_row = row     
        PA_counter += 1

### Check if two lists are the same
# if test_list1 == test_list2:
#     print("The lists are identical")
# else:
#     print("The lists are not identical")

## Check to see if the lists are the same 
# if list_PA_timestamp_sast_hour == list_PA_RH_timestamp_sast_hour:
#     print("The PM25 and RH are identical")
# else:
#     print("The PM25 and RH lists are not identical")
  
# if list_PA_timestamp_sast_hour == list_PA_TEMP_C_timestamp_sast_hour:
#     print("The PM25 and TEMP_C are identical")
# else:
#     print("The PM25 and TEMP_C lists are not identical")    

## Upload SAAQIS data
new_timestamp = []
list_PM = []
#list_PM_hourly =
# note: fix the beginnging of code for hourly data after SASAS

with open('../Data/SAAQIS/Welgegund-NAQI/Welgegund.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    started = False
    counter = 0
    sumPms = 0
    valid = 0
    for row in csv_reader: #row is the row of csv file
        if counter > 6 and counter < 26284:       
            #hour = row[0].split(" ")[0]
            date = row[0].split(" ")[1]
            if date == "01/10/2018" or started: #start date
                started = True
                date_list = date.split("/") 
                hour = row[0].split(" ")[0].split(":")[0]
                pms = row[1]
                #pms = float(pms)
                if not_available(pms) or negative(pms) or upper_threhold_PM(pms): # add function for weird values
                    pms = np.nan
                    
                list_PM.append(float(pms))
                
                
                
                new_hour = int(hour) - 1
                new_date = date + " "+ str(new_hour) + ":00"
                new_date = datetime.datetime.strptime(new_date, "%d/%m/%Y %H:00")
                new_timestamp.append(new_date)
                
                #print(date, new_date)
                
                #fix later
                #print(date, pms)
                #if empty(pms) or negative(pms): # add function for weird values
                    #pms = None
                if not_available(pms) or negative(pms):
                    pms = None
                if int(hour) == 24 and pms != None:
                    sumPms += float(pms)
                    avgPms = sumPms/valid
                    valid = 0
                    #print(date, avgPms)
                    
                    sumPms = 0 #resart after the 24 hours
                elif int(hour) == 24 and valid == 0:
                    #print(date, 0)
                    sumPms = 0
                elif int(hour) == 24 and pms == None:
                    avgPms = sumPms/valid
                    valid = 0
                    #print(date, avgPms)
                    sumPms = 0
              
                elif int(hour) < 24 and pms != None:
                    sumPms += float(pms)
                    valid += 1
      
        counter += 1

## NOTES
#list_PA_PM25_avg_hour - hourly PM data for PA
#list_PA_timestamp_sast_hour - timestamp data for PA
#list_PM - hourly PM data for PA 
#list_new_timestamp - timestamp for SAAQIS reference

#if new[i] in PA:
# merge_timestamp = []
# merge_PA_PM = [] 
# merge_SQ_PM = []   

# for i in len(list_new_timestamp):
#     if list_new_timestamp[i] in list_PA_timestamp_sast_hour:
#         merg_timestamp.append(list_new_timestamp[i]) #we need
#         list_PA_timestamp_sast_hour.index(list_new_timestamp[i]) 
          # index = sast_hour.index(new_timestamp[i])
          # avg_hour[index]
          # merge_PAappend.(avg_hour[index])
          # merge.SQ_PM.append(list_PM[i])


#list_PA_PM25_avg_hour - hourly PM data for PA
#list_PA_timestamp_sast_hour - timestamp data for PA
#list_PM - hourly PM data for PA 
#new_timestamp - timestamp for SAAQIS reference

merge_timestamp = []
merge_PA_PM = [] 
merge_PA_RH = []
merge_PA_TEMP_C = []
merge_SAAQIS_PM = []   

for i in range(len(new_timestamp)):
    if new_timestamp[i] in list_PA_timestamp_sast_hour:
        merge_timestamp.append(new_timestamp[i])
        list_PA_timestamp_sast_hour.index(new_timestamp[i]) 
        index = list_PA_timestamp_sast_hour.index(new_timestamp[i])
        merge_PA_PM.append(list_PA_PM25_avg_hour[index])
        merge_PA_RH.append(list_PA_RH_avg_hour[index])
        merge_PA_TEMP_C.append(list_PA_TEMP_C_avg_hour[index])
        merge_SAAQIS_PM.append(list_PM[i])
  
        
# merge_timestamp
# merge_PA_PM
# merge_PA_RH 
# merge_PA_TEMP_C 
# merge_SAAQIS_PM      

## Shorten the merge lists to get data range 
## # delete all elements from index 2 to the end 
## inclusize for including index 2 which in this case is 4
##del my_list_2[2:]

## 1/10/2018 to 30/6/2020
## 30/6/20 in merge_timestamp 13813
## 01/07/20 in merge_timestamp 13814


## how to splice lists 
del merge_timestamp[13814:]
del merge_PA_PM[13814:]
del merge_PA_RH[13814:] 
del merge_PA_TEMP_C[13814:] 
del merge_SAAQIS_PM[13814:]    



## Remove NaN
# PA_PM
merge_PA_PM, merge_timestamp, merge_PA_RH, merge_PA_TEMP_C, merge_SAAQIS_PM  = remove_nan_and_indices(
merge_PA_PM, merge_timestamp, merge_PA_RH, merge_PA_TEMP_C, merge_SAAQIS_PM)

# PA_RH
merge_PA_RH, merge_timestamp, merge_PA_PM, merge_PA_TEMP_C, merge_SAAQIS_PM  = remove_nan_and_indices(
merge_PA_RH, merge_timestamp, merge_PA_PM, merge_PA_TEMP_C, merge_SAAQIS_PM)

# ## PA_TEMP_C
merge_PA_TEMP_C, merge_timestamp, merge_PA_RH, merge_PA_PM, merge_SAAQIS_PM  = remove_nan_and_indices(
merge_PA_TEMP_C, merge_timestamp, merge_PA_RH, merge_PA_PM, merge_SAAQIS_PM)

# ## SAAQIS_PM
merge_SAAQIS_PM, merge_timestamp, merge_PA_RH, merge_PA_TEMP_C, merge_PA_PM  = remove_nan_and_indices(
merge_SAAQIS_PM, merge_timestamp, merge_PA_RH, merge_PA_TEMP_C, merge_PA_PM)


# # merge_timestamp
# # merge_PA_PM
# # merge_PA_RH 
# # merge_PA_TEMP_C 
# # merge_SAAQIS_PM    

independent_variable1 = merge_PA_PM
independent_variable2 = merge_PA_RH
independent_variable3 = merge_PA_TEMP_C


# ## PM2.5 
#independent_variables = [independent_variable1]

# # ## PM2.5 RH
##independent_variables = [independent_variable1, independent_variable2]
                         
# # ## PM2.5 T
#independent_variables = [independent_variable1, independent_variable3]

# # ## PM2.5 RH T
independent_variables = [independent_variable1, independent_variable2, independent_variable3]

# # ## Correction
dependent_variable = merge_SAAQIS_PM

independent_variables = np.array(independent_variables).T 

dependent_variable = np.array(dependent_variable)

X_train, X_test, y_train, y_test = train_test_split(independent_variables, dependent_variable, test_size=0.3, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

y_test_pred = model.predict(X_test)

y_train_pred = model.predict(X_train)

# ## apply correction to data set 
y_pred = model.predict(independent_variables)
y = model.predict(independent_variables)

# coefficients = model.coef_
# intercept = model.intercept_

# print(coefficients)
# print(intercept)

# plt.scatter(y_test, y_pred_test)
# plt.xlabel("True Values")
# plt.ylabel("Predicted Values")
# plt.title("True vs Predicted Values")

# # Add a line of best fit
# z = np.polyfit(y_test, y_pred_test, 1)
# p = np.poly1d(z)
# plt.plot(y_test, p(y_test), color='red')

# plt.show()

#import matplotlib.pyplot as plt
# plt.figure(figsize=(10, 6), dpi=300)
# plt.scatter(y_train, y_train_pred, color='blue', label='Training Data')
# plt.scatter(y_test, y_test_pred, color='red', label='Test Data')

# plt.xlabel("True Values")
# plt.ylabel("Predicted Values")
# plt.title("True vs Predicted Values")
# plt.legend()

# # Add a line of best fit (optional)
# plt.plot([min(y), max(y)], [min(y), max(y)], color='black', linestyle='--')

# plt.show()


# ## R2 for splits
# ## R2 Train
# r2_train = r2_score(y_train, y_pred_train)

# ## R2 Test (one to base off of)
# r2_test = r2_score(y_test, y_pred_test)

# ## apply R2 for entire data set
# r2_all = r2_score(dependent_variable, y_pred)


# ## Correction function
# # def PA_correction(PM, RH, TEMP_C):
# #     return (0.5591662*PM) + (-0.11213007*RH) + (-0.09515696*TEMP_C)

# merge_PA_PM_correction = []
# for i in range(len(merge_PA_PM)):
#     new_PA = PA_correction(merge_PA_PM[i], merge_PA_RH[i], merge_PA_TEMP_C[i])
#     merge_PA_PM_correction.append(new_PA)
    





# ## Plots
# # list_PA_PM25_raw = []
# # list_PA_RH_raw = []
# # list_PA_TEMP_F_raw = []
# # list_PA_TEMP_C_raw = []

# # list_PA_timestamp_utc_raw = []
# # list_PA_timestamp_sast_raw = []

# # list_PA_PM25_timestamp_sast_hour = []
# # list_PA_RH_timestamp_sast_hour = []
# # list_PA_TEMP_C_timestamp_sast_hour = []
# #list_PA_PM25_avg_hour - hourly PM data for PA
# # list_PA_timestamp_sast_hour - timestamp data for PA
# #list_PM - hourly PM data for PA 
# #list_new_timestamp - timestamp for SAAQIS reference

# ## PA data 
# ## PA PM2.5 data
# ## X-axis: 
# ## y-axis: 
# # plt.scatter(list_PA_timestamp_sast_raw, list_PA_PM25_raw, color='purple')
# # plt.xticks(rotation=45, ha='right')
# # plt.xlabel("Date")
# # plt.ylabel("PM$_{2.5}$ ($\mu$g/m$^3$)")
# # #plt.title("PM$_{2.5}$ Raw Data")
# # #plt.locator_params(axis='x', nbins=12)
# # plt.grid()
    
# ## PA RH data
# #X
# #Y
# # plt.scatter(list_PA_timestamp_sast_raw, list_PA_RH_raw, color='blue')
# # plt.xticks(rotation=45, ha='right')
# # plt.xlabel("Date")
# # plt.ylabel("RH (%)")
# # #plt.title("PM$_{2.5}$ Raw Data")
# # #plt.locator_params(axis='x', nbins=12)
# # plt.grid()
    

# ## PA TEMP_F data
# plt.scatter(list_PA_timestamp_sast_raw, list_PA_TEMP_F_raw, color='red')
# plt.xticks(rotation=45, ha='right')
# plt.xlabel("Date")
# plt.ylabel("Temperature (F)")
# #plt.title("PM$_{2.5}$ Raw Data")
# #plt.locator_params(axis='x', nbins=12)
# plt.grid()

# ## SAAQIS data 
# ## X-axis: new_timestamp
# ## y-axis: list_PM

# # plt.scatter(new_timestamp, list_PM, color='green')
# # plt.xticks(rotation=45, ha='right')
# # plt.xlabel("Date")
# # plt.ylabel("PM$_{2.5}$ ($\mu$g/m$^3$)")
# # #plt.title("PM$_{2.5}$ Raw Data")
# # #plt.locator_params(axis='x', nbins=12)
# # plt.grid()




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
# plt.scatter(list_PA_timestamp_sast_raw, list_PA_PM25_raw, alpha=0.5, marker="x")
#, 'o', color='green')
#plt.ylim(0, 100)
# plt.scatter(new_timestamp, list_PM, color='green')
# plt.xticks(rotation=45, ha='right')
# plt.xlabel("Date")
# plt.ylabel("PM$_{2.5}$ ($\mu$g/m$^3$)")
# #plt.title("PM$_{2.5}$ Raw Data")
# #plt.locator_params(axis='x', nbins=12)
# plt.grid()



