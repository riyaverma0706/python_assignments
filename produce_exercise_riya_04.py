'''
Filename: produce_exercise_riya_04.py
Author:   Riya Verma
Purpose:  DATA HANDLING EXERCISE using LIST COMPREHENSIONS
Revision:
      00 - Importing and reading Csv File.
      01 - 16 - Printing results of questions

'''


import csv

data = []
csvfile = open('produce_extra.csv','r')
reader = csv.reader(csvfile)
for row in reader:  # main loop reads one row at a time
    if reader.line_num == 1: # get the location names from row 1
        locations = row[2:]  # slice to remove commodity and date
    else:
        for location,value in zip(locations,row[2:]):  # iterate through locations and values
            row_num = len(data)     # index for the data row 
            data.append(row[:2])    # new data row: commodity and date
            data[row_num].append(location)  # append location
            data[row_num].append(float(value.replace('$','')))     # append value
csvfile.close()



# (1) make a list named comList of all commodities using list comprehension
comList = [l[0] for l in data]
####

# (2) make another list named uComList with the duplicates removed 
# (one source code statement) hint: use the set() and list() functions 
uComList = set(comList)
####

# (3) Print the number of unique commodities that are present in the data
# (one source code statement) hint: use the len() function
print("There are %d unique commodities" % len(uComList))
####

# (4) Use list comprehension compute a list named comNums where each item is a list 
# of this format: [commodity_name, number of records of that commodity]
# (one source code statement) hint: use the count() method
comNums = [[cname, comList.count(cname)] for cname in uComList]
####

# (5) for each item in comNums, print the number of records
# (two source code lines)
for cname, cnum in comNums:
    print("Found %d records for %s" % (cnum, cname))
####
    
####
# (6) Sort comNums according to number of records in ascending order 
# (one source code statement) hint: use the sort() method with a lambda
comNums.sort(key = lambda x: x[1])
####

# (7) print the commodity with the fewest number of records
# (one source code statement)
print("Least available commodity = %s" % comNums[0][0])
####

# (8) print the number of weeks the least available commodity was available for
# (one source code statement) hint: each commodity has 5 records for each week
print("%s were available for %d weeks." %(comNums[0][0], comNums[0][1]//5))
####

# (9) use a list comprehension to find the lowest price for nectarines in Chicago
# assign it to a variable called min1 hint: use the min() function
# (one source code statement) 
min1 = float(min([row[3] for row in data if row[0] == 'Nectarines' and row[2] == 'Chicago']))
####

# (10) use a list comprehension to find the date of the lowest price for nectarines 
# in Chicago and assign it to a variable named mind1
# (one source code statement) hint: one value at index=0
mind1 = [row[1] for row in data if row[0] == 'Nectarines' and row[2] == 'Chicago' and row[3] == min1][0]
####

# (11) print the lowest price for nectarines in Chicago and the date
# (one source code statement)
print("The lowest price for Nectarines in Chicago was $%s on %s." %(min1, mind1))
####

# (12) use a list comprehension to find the farm price for nectarines on the same 
# date and assign it to a variable named fp1
# (one source code statement) 
fp1 = float([row[3] for row in data if row[0] == 'Nectarines' and row[1] == mind1 and row[2] == 'Farm'][0])
####

# (13) print the farm price for nectarines on the date 
# of lowest price in Chicago and print the computed price difference
# (one source code statement)
print("Nectarine farm price on %s was $%s; $%s less then in Chicago" %(mind1, fp1, round(min1 - fp1, 2)))
####

# (14) Create a dictionary called comNumsDict where the keys are the commodities 
# and the values are the number of weeks each commodity was available for
# (one source code statement) hint: use a list comprehension and the dict() function
comNumsDict = dict([[cname, comList.count(cname)//5] for cname in uComList])
####

# (15) Use comNumDict to print the number of weeks peaches were available for
# (one source code statement)
print("Peaches were available for %d weeks" %(comNumsDict['Peaches']))
####

# (16) Use a list comprehension to calculate the average price of Peaches
# in Atlanta and assign it to a variable pAvg
# (one source code statement) hint use the sum() function and the dictionary
pAvg = sum(row[3] for row in data if row[0] == "Peaches" and row[2] == "Atlanta") / comNumsDict['Peaches']
####

# (17) Print the average price of Peaches in Atlanta
print("The average price of peaches in Atlanta was $%s." % round(pAvg, 2))
####

