import csv
import pandas as pd

data_1 = []
data_2 = []

with open('updated_dwarf_stars.csv','r') as f:
    temp_data = csv.reader(f)
    for i in temp_data:
        data_1.append(i)

with open('bright_stars.csv','r') as f:
    temp_data = csv.reader(f)
    for i in temp_data:
        data_2.append(i)

header_1 = data_1[0]
header_2 = data_2[0]

headers = header_1 + header_2

star_data_1 = data_1[1:]
star_data_2 = data_2[1:]
star_data = []

for i in star_data_1:
    star_data.append(i)

for i in star_data_2:
    star_data.append(i)

with open('total_stars.csv','w') as f:
    data = csv.writer(f)
    data.writerow(headers)
    data.writerows(star_data)