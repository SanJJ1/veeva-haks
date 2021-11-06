import pandas as pd
import numpy as np

import csv
x = []
with open('Prescriber_Data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        x += [row]


h = x[0]
x = x[1:]
a = set([i[4] for i in x])

# print(a)
# print(set(a))
print(h)
fn = [i[3] for i in x]
print(len(fn), fn)


sn = {"Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut",
      "District of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois",
      "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota",
      "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey",
      "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island",
      "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont",
      "Washington", "Wisconsin", "West Virginia", "Wyoming"}


ufn = set(fn)
print(len(ufn), ufn)

print(sorted(list(ufn)))

print(sn - ufn)







