# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 11:13:28 2024

@author: u23993376
"""
import pandas as pd

# merge_timestamp
# merge_PA_PM
# merge_PA_RH 
# merge_PA_TEMP_C 
# merge_SAAQIS_PM  
# merge_PA_PM_correction

df_merge_PA_PM_correction = pd.DataFrame(list(zip(merge_timestamp, merge_PA_PM_correction)), columns = ["time", "PM"])
df_merge_PA_PM_correction.set_index('time', inplace=True)
df_PA_daily = df_merge_PA_PM_correction.resample('D').mean()


df_merge_SAAQIS_PM = pd.DataFrame(list(zip(merge_timestamp, merge_SAAQIS_PM)), columns = ["time", "PM"])
df_merge_SAAQIS_PM.set_index('time', inplace=True)
df_SAAQIS_daily = df_merge_SAAQIS_PM.resample('D').mean()

cent_over_who = []
cent_over_SA = []
for element in df_PA_daily.PM:
    if element > 25:
        #print(element)
        cent_over_who.append(element)
    if element > 40:
        cent_over_SA.append(element)
    
tm_over_who = []
tm_over_SA = []
for element in df_SAAQIS_daily.PM:
    if element > 25:
    #print(element)
        tm_over_who.append(element)
    if element > 40:
        tm_over_SA.append(element)