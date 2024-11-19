# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 05:24:04 2024

@author: u23993376
"""
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

def f_to_c(temp_f):
    temp_f = float(temp_f)
    return (temp_f-32) * (5/9)

def remove_nan_and_indices(list1, list2):
    """Removes np.nan values from list1 and deletes corresponding indices in list2.

    Args:
        list1: The list containing np.nan values.
        list2: The list whose indices will be deleted.

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

    return list1, list2

# Example usage:
list1 = [1, np.nan, 3, 4, np.nan]
list2 = ['a', 'b', 'c', 'd', 'e']

list1, list2 = remove_nan_and_indices(list1, list2)

print(list1)  # Output: [1, 3, 4]
print(list2)  # Output: ['a', 'c', 'd']


list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_b = [1, np.nan, 3, 4, 5, 6, 7, 8, np.nan, 10]
list_c = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


list_b, list_c = remove_nan_and_indices(list_b, list_c)
print(list_b)
print(list_c)













# for element in list_b:
#     if element == np.nan:
#         print("you did it")
#         #list_b.pop(i)
#         #print(list_b)
#         #list_c.pop(i)
#         #print(list_c)
        
# for i in range(len(list_b)):
#     if list_b[i] == np.nan:
#         print("You did it")
#         print(i)
        
# new_list_b = []
# new_list_c = []
# for item in list:
#     if not np.isnan(item):
#         new_list_b.append(item)
#         new_list_c.

# print(new_list)   