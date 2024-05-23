# Import
import csv
import random as r
import time
import re
# Main Code
data = []
with open('list.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)
element = data.pop(r.randint(0,26))
element = re.sub(r"(')|()|[\[-\]]","",str(element))
print(element)
time.sleep(5)
