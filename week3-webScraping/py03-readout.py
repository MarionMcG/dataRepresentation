import requests
from bs4 import BeautifulSoup


with open("../week2/lab02.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')


print()
print("-------------------")
print()

#print (soup.tr)
rows = soup.findAll("tr")
for row in rows:
    print("------")
    print(rows)


print()
print("-------------------")
print()

for row in rows:
     #print(row)
    cols = row.findAll("td")
    dataList = []
    for col in cols:
        dataList.append(col.text)
    print (dataList)

# I made this task easier on myself without realising it as I only have one row in my table
#Need to add the additional rows to lab02.html

import csv
employee_file = open('employee_file.csv', mode='w')
employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
employee_writer.writerow(['John Smith', 'Accounting', 'November'])
employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
employee_file.close()
