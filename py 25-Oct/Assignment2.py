import csv # imports the needed csv functions
from copy import deepcopy # imports deepcopy function

######################################
## ISYS90088 - Assignment 2         ##
## Student ID:      814072          ##
## Student Name:    Yang Xiuqi      ##
## Submission date: 25/10/2017      ##
######################################

# Q1
# Invalid data values be replaced by 0
def clean_data(data):
    # Deepcopy, did not modify the argument dictionary, data
    data_copy = deepcopy(data)
    clean_count = 0
    for i in data_copy:
        for j in range(2002, 2013):
            if not data_copy[i][str(j)].isdigit():
                data_copy[i][str(j)] = '0'
                clean_count += 1
    data_copy_clean = data_copy
    return data_copy_clean, clean_count

# Q2
# countCrimes returns the sum value of the key year 
def countCrimes(data, key):
    sum_crime_year = 0
    for i in data:
        sum_crime_year += int(data[i][str(key)])
    return sum_crime_year

# The year with the maximum total crimes
def worstYear(data):
    # Dict, key is year, value is crime num
    year_num = {}
    for i in range(2002, 2013):
        year_num[i] = countCrimes(data, i)
    # Find the year with the highest crime num
    worst_year_tie = []
    for key, value in year_num.items():
        if year_num[key] == max(year_num.values()):
            worst_year_tie += [str(key)]
    worst_year_tie = ', '.join(worst_year_tie)
    max_year_num = max(year_num.values())
    return worst_year_tie, max_year_num

# Q3
# countAreaCrimes returns the sum value of the area
def countAreaCrimes(data, area):
    sum_crime_area = 0
    for i in data:
        if data[i]['Statistical Division or Subdivision'] == area:
            for j in range(2002, 2013):
                sum_crime_area += int(data[i][str(j)])
    return sum_crime_area

# Return a dict, key is area, value is crime num
def worstCrime(data):
    area_num = {}
    for i in data:
        if data[i]['Statistical Division or Subdivision'] not in area_num.keys():
            area_num[data[i]['Statistical Division or Subdivision']] = countAreaCrimes(data, data[i]['Statistical Division or Subdivision'])
    return area_num

# Find the area with the highest crime num
def worstArea(data):
    area_num = worstCrime(data)
    sub_num = 0
    worst_area_tie = []
    for key, value in area_num.items():
        if area_num[key] == max(area_num.values()):
            worst_area_tie += [str(key)]
        sub_num += 1 # Count the num of Subdivisions
    worst_area_tie = ', '.join(worst_area_tie)
    max_area_num = max(area_num.values())
    return sub_num, worst_area_tie, max_area_num
    
# Q4
# countTypeCrimes returns the sum value of the type
def countTypeCrimes(data, type):
    sum_crime_type = 0
    for i in data:
        if data[i]['Offence category'] == type:
            for j in range(2002, 2013):
                sum_crime_type += int(data[i][str(j)])
    return sum_crime_type

# Return a dict, key is type, value is crime num
def mostActive(data):
    type_num = {}
    for i in data:
        if data[i]['Offence category'] not in type_num.keys():
            type_num[data[i]['Offence category']] = countTypeCrimes(data, data[i]['Offence category'])
    return type_num        

# Find the type with the highest crime num
def worstType(data):
    type_num = mostActive(data)
    worst_type_tie = []
    for key, value in type_num.items():
        if type_num[key] == max(type_num.values()):
            worst_type_tie += [str(key)]
    worst_type_tie = ', '.join(worst_type_tie)
    max_type_num = max(type_num.values())
    return worst_type_tie, max_type_num

##########################
## Supportive functions ##
##########################  

# read_data reads the data from the CSV file
def read_data(filename):
    data = {}
    new_data = {}
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ID = row["ID"]
            del row["ID"]
            for key in row:
                if not row[key]:
                    row[key] = None
            data[ID]=row
            new_data[ID] = dict(list(row.items()))
    return new_data

# count_type returns the num of crime type
def count_type(data):
    type_num = mostActive(data)
    type_count = 0
    for i in type_num:
        type_count += 1
    return type_count 

# Q5
######################################### 
## Main method, to call functions etc. ##
#########################################
def main(datafile):
    # read_data returns a dictionary of dictionaries.  
    data = read_data(datafile) 
    
    # Q1 Clean data
    print('-' * 10 + 'Q1' + '-' * 10)
    # clean_data returns a dict without invalid data value, and clean num
    data_copy_clean, clean_count = clean_data(data)
    # Display the clean num
    print(clean_count, 'data sample(s) cleaned', '\n')

    # Q2 Worst year
    print('-' * 10 + 'Q2' + '-' * 10) 
    # countCrimes returns the sum value of the key year
    # Display the worst year
    worst_year_tie, max_year_num = worstYear(data_copy_clean)
    print(worst_year_tie, 'is/are the worst year(s), and total sum of crimes is', max_year_num, '\n')
    
    # Q3 Worst area
    print('-' * 10 + 'Q3' + '-' * 10)
    # worstCrime returns a dict
    # Display the worst area
    sub_num, worst_area_tie, max_area_num = worstArea(data_copy_clean)
    print(sub_num, 'Subdivision(s) found. The worst area(s) is /are', worst_area_tie + ', and the crime number is', max_area_num, '\n')
    
    # Q4 Most active criminal activity
    print('-' * 10 + 'Q4' + '-' * 10)
    # mostActive returns a dict
    # Display the worst type
    worst_type_tie, max_type_num = worstType(data_copy_clean)
    print('Most active Crime overall:', worst_type_tie + ', and the summated value:', max_type_num, '\n')

    # Q5 Tying it all together
    print('-' * 10 + 'Q5' + '-' * 10)
    Name = 'Yang Xiuqi' # Student name
    row_num = len(data)
    type_count = count_type(data_copy_clean)

    print('On behalf of the MUC (Made Up Company), '
          'I, {0}, ' 
          'have analysed {1} units of the crime statistics data. '
          'This data covered {2} Subdivisions '
          'and found {3} types of crimes. '
          'I conclude that the worst area for crime is {4}, '
          'and that the most active category of crime is {5}. '
          .format(Name, row_num, sub_num, type_count, worst_area_tie, worst_type_tie))

############################
## Begins the application ##
############################
datafile ='CrimeDataSetDirty.csv' # Point to the location of the csv file

main(datafile)
