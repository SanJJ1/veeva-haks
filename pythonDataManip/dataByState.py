import pandas as pd
import numpy as np

import csv

states = {}
states["header"] = ["lat", "lon",
                    "CountT", "NRxT", "TRxT", [0] * 6,
                    "CountC", "NRxC", "TRxC", [0] * 6,
                    "CountNa", "NRxNa", "TRxNa", [0] * 6,
                    "CountNo", "NRxNo", "TRxNo", [0] * 6,
                    "CountZ", "NRxZ", "TRxZ", [0] * 6,
                    ]
with open('states.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        states[row[0]] = [0] * len(states["header"])
        states[row[0]][0] = row[1]
        states[row[0]][1] = row[2]


x = []
with open('Prescriber_Data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        x += [row]

h = x[0]
x = x[1:]

for i in x:
    NRxT = sum([int(j) for j in i[5:11]])
    TRxT = sum([int(j) for j in i[11:]])
    state = i[3]
    states[state][2] += 1
    states[state][3] += NRxT
    states[state][4] += TRxT
    if i[4] == "Cholecap":
        states[state][5] += 1
        states[state][6] += NRxT
        states[state][7] += TRxT
    elif i[4] == "Nasalclear":
        states[state][8] += 1
        states[state][9] += NRxT
        states[state][10] += TRxT
    if i[4] == "Nova-itch":
        states[state][11] += 1
        states[state][12] += NRxT
        states[state][13] += TRxT
    if i[4] == "Zap-a-Pain":
        states[state][14] += 1
        states[state][15] += NRxT
        states[state][16] += TRxT
print(states)
# print(h)
# print(x[0])
# print(x[0][5:11])
# print(x[0][11:])

output = []
import json

# for state in states:


# with open("Prescriber_Data.csv", 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=',')
#     spamwriter.writerows(z)



