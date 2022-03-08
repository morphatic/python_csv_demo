"""
Playing with CSV data about US Military Bases
that use renewable energy
"""

import csv # library for working with CSV data

datafile = open('data.csv')
reader = csv.reader(datafile)

# read the headers, and advance the cursor to the first row of data
headers = next(reader)
print(headers)

total = 0
renewable = 0

# What percentage of the bases use renewables
for row in reader:
    if row[1] == 'True':
        renewable += 1
    total += 1

print(f'The total number of bases is: {total}')
print(f'The total number of bases with renewables is: {renewable}')
print(f'The percentage of bases with renewables is: {round(renewable / total * 100)}%')
