
## Upload relevant libraries
import csv

## Define functions
def empty(pm):
    return len(pm) == 0

def negative(pm):
    return float(pm) < 0

## Upload PA data
with open('../Data/PurpleAir/CSIR_wel_eb7e/CSIR_wel_eb7e.csv', newline='') as PA_csv_file:
    PA_csv_reader = csv.reader(PA_csv_file, delimiter=',')
    
    PA_started = False
    PA_counter = 0
    PA_SumPms = 0
    PA_valid = 0
    for row in PA_csv_reader:
        if PA_counter < 10:
            date = row[0].split(",")[0]
            date = date.split(" ")
            date = date.split(",")
            print(date)
        
        PA_counter += 1




## Upload SAAQIS data

with open('../Data/SAAQIS/Welgegund-NAQI/Welgegund.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    started = False
    counter = 0
    sumPms = 0
    valid = 0
    for row in csv_reader: #row is the row of csv file
        if counter > 6 and counter < 26285:       
            #hour = row[0].split(" ")[0]
            date = row[0].split(" ")[1]
            if date == "01/10/2018" or started: #start date
                started = True
                date = date.split("/") 
                hour = row[0].split(" ")[0].split(":")[0]
                pms = row[1]
                #print(date, pms)
                if empty(pms) or negative(pms): # add function for weird values
                    pms = None
                if int(hour) == 24 and pms != None:
                    sumPms += float(pms)
                    avgPms = sumPms/valid
                    valid = 0
                    print(date, avgPms)
                    
                    sumPms = 0 #resart after the 24 hours
                elif int(hour) == 24 and valid == 0:
                    print(date, 0)
                    SumPms = 0
                elif int(hour) == 24 and pms == None:
                    avgPms = sumPms/valid
                    valid = 0
                    print(date, avgPms)
                    SumPms = 0
              
                elif int(hour) < 24 and pms != None:
                    sumPms += float(pms)
                    valid += 1


                
               
        counter += 1
        

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



"""
Orginal code I don't want to lose
## Upload relevant libraries
import csv

## Upload PA data

## Upload SAAQIS data
#csv_file = open("Welgegund.csv")

## Define functions
def empty(pm):
    return len(pm) == 0

def negative(pm):
    return float(pm) < 0



with open('../Data/SAAQIS/Welgegund-NAQI/Welgegund.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    started = False
    counter = 0
    sumPms = 0
    valid = 0
    for row in csv_reader: #row is the row of csv file
        if counter > 6 and counter < 26285:       
            #hour = row[0].split(" ")[0]
            date = row[0].split(" ")[1]
            if date == "01/10/2018" or started: #start date
                started = True
                date = date.split("/") 
                hour = row[0].split(" ")[0].split(":")[0]
                pms = row[1]
                #print(date, pms)
                if empty(pms) or negative(pms): # add function for weird values
                    pms = None
                if int(hour) == 24 and pms != None:
                    sumPms += float(pms)
                    avgPms = sumPms/valid
                    valid = 0
                    print(date, avgPms)
                    
                    sumPms = 0 #resart after the 24 hours
                elif int(hour) == 24 and valid == 0:
                    print(date, 0)
                    SumPms = 0
                elif int(hour) == 24 and pms == None:
                    avgPms = sumPms/valid
                    valid = 0
                    print(date, avgPms)
                    SumPms = 0
              
                elif int(hour) < 24 and pms != None:
                    sumPms += float(pms)
                    valid += 1


                
               
        counter += 1




