'''
File name : final_project_riya_03.py
Author    : Riya Verma
Purpose   : This program displays plot based on the average price vs product based on different locations.
Revisions :
            00: Importing and reading csv file
            01: Data Cleaning and formatting
            02: Replacing list of price with average value
            03: Using plotly to plot the graph between average price vs product in final-plot.html.          
'''


# Read produce_extra.csv file
import plotly.offline as py
import csv
from datetime import datetime
data = []
csvfile = open('produce_extra.csv','r')
reader = csv.reader(csvfile)
for row in reader:  ###! main loop reads one row at a time
    if reader.line_num == 1: ###! get the location names from row 1
        locations = row[2:]  ###! slice to remove commodity and date
    else:
        for location,value in zip(locations,row[2:]):  ###! iterate through locations and values
            row_num = len(data)     ###! index for the data row
            data.append(row[:1] + [datetime.strptime(row[1], '%m/%d/%Y')])  ###! new data row: commodity and date
            data[row_num].append(location)  ###! append location
            data[row_num].append(float(value.replace('$','')))     ###! convert price to float
csvfile.close()

# get unique product strings
comNames = sorted(list(set([r[0] for r in data])))
for i, name in enumerate(comNames):
  print("Index %d: %s" %(i, name))
comIndex = input("Enter product numbers separated by spaces: ")
comIndex = [int(c) for c in comIndex.split(' ')]
print("Selected products: ", *[comNames[i] for i in comIndex])

# get date range
comDates = sorted(list(set([r[1] for r in data])))
for i, date in enumerate(comDates):
  print("Index %d: %s" %(i, datetime.strftime(date, "%m/%d/%Y")))
comDate = input("Enter start/end date numbers separated by a space: ")
comDate = [int(d) for d in comDate.split(' ')]
print("Earliest Date: %s, Latest Date: %s" %(datetime.strftime(comDates[0], "%m/%d/%Y"), datetime.strftime(comDates[-1], "%m/%d/%Y")))
print("Selected Dates: %s to %s" %(datetime.strftime(comDates[comDate[0]], "%m/%d/%Y"), datetime.strftime(comDates[comDate[1]], "%m/%d/%Y")))

# select region
comLocs = sorted(list(set([r[2] for r in data])))
for i, loc in enumerate(comLocs):
  print("Index %d: %s" %(i, loc))
comLocInput = input("Enter location numbers separated by spaces: ")
comLocInput = [int(c) for c in comLocInput.split(' ')]
print("Selected locations: ", *[comLocs[l] for l in comLocInput])

# select date based on criteria
selected_names = [comNames[i] for i in comIndex]
selected_regions = [comLocs[l] for l in comLocInput]
def valid_date(date):
  f = comDates[comDate[0]]
  t = comDates[comDate[1]]
  if date >= f and date <= t:
    return True
  return False
select = list(filter(lambda x: x[0] in selected_names and valid_date(x[1]) and x[2] in selected_regions, data))

select_dict = {}
for s in select:
  key = (s[0], s[2])
  if key not in select_dict:
    select_dict[key] = [s[3]]
  else:
    select_dict[key].append(s[3])

# replace list of price with average value
for key in select_dict:
  prices = select_dict[key]
  avg_p = round(sum(prices)/len(prices), 2)
  select_dict[key] = avg_p

# ploting figure
import plotly.offline as py
import plotly.graph_objects as go
import collections
title = 'Produce prices from ' + datetime.strftime(comDates[comDate[0]], "%m/%d/%Y") + ' to ' + datetime.strftime(comDates[comDate[1]], "%m/%d/%Y")
traces = []
new_select = collections.defaultdict(dict)
for key in select_dict:
  new_select[key[1]][key[0]] = select_dict[key]
for key in new_select:
  traces.append(go.Bar(x = list(new_select[key].keys()), y = list(new_select[key].values()), name = key))

layout = go.Layout(title = title, barmode = 'group', yaxis = dict(title = 'Average Price in Dollars', tickformat = '$.2f'), xaxis = dict(title = 'Product'))
fig = go.Figure(data = traces, layout = layout)
py.plot(fig, filename = 'final-plot.html')
print("Plot saved in final-plot.html, view in browser")

