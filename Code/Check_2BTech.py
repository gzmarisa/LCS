
# Upload relevent libraries
import csv
import glob

# Data paths 
path_2BTech = '../Data/2BTech/'

# Upload 2B Tech Files into one csv 

## Use a wildcard pattern to match all CSV files in the directory
files_2BTech = glob.glob(path_2BTech + '*.txt')
## Intialize an empty list to store rows from each file
combined_data_2BTech = []
## Read and append rows from each CSV file to the combined_data list
for file_2BTech in files_2BTech:
    with open(file_2BTech, 'r') as txt_file:
        reader = csv.reader(txt_file)
        if not combined_data_2BTech:  # Include header only once
            combined_data_2BTech.append(next(reader))
        else:
            next(reader)  # Skip header
            combined_data_2BTech.extend(row for row in reader)
## Write the combined data to a new CSV file
with open('combined.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(combined_data_2BTech)

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



