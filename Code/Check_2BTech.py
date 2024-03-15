
# Upload relevent libraries
import csv
import glob
import os

# Data paths 
path_2BTech = '../Data/2BTech/'

# Upload 2B Tech Files into one csv 

## Use a wildcard pattern to match all CSV files in the directory
files_2BTech = glob.glob(path_2BTech + '*.txt')
files_2BTech.sort(key=os.path.getmtime)
#files_2BTech =os.path.getmtime


combined_data_2BTech = []
for filename in files_2BTech:
    filepath = filename
    #print(filepath)
    with open(filepath, newline='') as txt_file:
        csv_reader = csv.reader(txt_file, delimiter=',')
    
            #started_2BTech = False
        counter_2BTech = 0
            #SumPms_2BTech = 0
            #valid_2BTech = 0
        for row in csv_reader:
            if counter_2BTech > 2:
                combined_data_2BTech.append(row)
                
            counter_2BTech += 1

## Intialize an empty list to store rows from each file
# combined_data_2BTech = []

# ## Read and append rows from each CSV file to the combined_data list
# for file_2BTech in files_2BTech:
#     with open(file_2BTech, 'r') as txt_file:
#         reader = csv.reader(txt_file)
        
#         if not combined_data_2BTech:  # Include header only once
#             combined_data_2BTech.append(next(reader))
#             #print(file_2BTech, os.path.getmtime(file_2BTech))
#         else:
#             next(reader)  # Skip header
#             combined_data_2BTech.extend(row for row in reader)
#             #print(file_2BTech, os.path.getmtime(file_2BTech))
            
# ## Write the combined data to a new CSV file
# with open('combined_updated.csv', 'w', newline='') as outfile:
#     writer = csv.writer(outfile)
#     writer.writerows(combined_data_2BTech)

## Upload 2B Tech Files 
# with open('../Code/combined.csv', newline='') as csv_file_2BTech:
#     csv_reader_2BTech = csv.reader(csv_file_2BTech, delimiter=',')
    
#     csv_reader_2BTech = csv.reader(csv_file_2BTech, delimiter=',')
    
#     started_2BTech = False
#     counter_2BTech = 0
#     SumPms_2BTech = 0
#     valid_2BTech = 0
#     for row in csv_reader_2BTech:
#         if counter_2BTech > 2 and counter_2BTech <10:
#             print(row)
        
#         counter_2BTech += 1



