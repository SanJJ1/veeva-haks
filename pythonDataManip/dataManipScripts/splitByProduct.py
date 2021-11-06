import pandas as pd
import numpy as np

import csv
x = []
with open('../Prescriber_Data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        x += [row]
        # print(', '.join(row))
print(x)
h = x[0]
x = x[1:]
a = set([i[4] for i in x])

# print(a)

# print(set(a))

print(h)

for i in a:
    z = [h]
    for j in x:
        if j[4] == i:
            z += [j]
    with open(f"{i}.csv", 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerows(z)



