import pandas as pd
import numpy as np

import csv

states = {}
states["header"] = ["lat", "lon",
                    "CountT", "NRxT", "TRxT", [0] * 6, [0] * 6,
                    "CountC", "NRxC", "TRxC", [0] * 6, [0] * 6,
                    "CountNa", "NRxNa", "TRxNa", [0] * 6, [0] * 6,
                    "CountNo", "NRxNo", "TRxNo", [0] * 6, [0] * 6,
                    "CountZ", "NRxZ", "TRxZ", [0] * 6, [0] * 6,
                    ]
print(states["header"])
with open('../state-data/states.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        states[row[0]] = [0] * len(states["header"])
        states[row[0]][0] = row[1]
        states[row[0]][1] = row[2]
        e = [5, 6, 10, 11, 15, 16, 20, 21, 25, 26]
        for i in e:
            states[row[0]][i] = [0] * 6


x = []
with open('../Prescriber_Data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        x += [row]

h = x[0]
x = x[1:]

for i in x:
    NRxs = [int(j) for j in i[5:11]]
    TRxs = [int(j) for j in i[11:]]
    NRxT = sum(NRxs)
    TRxT = sum(TRxs)
    state = i[3]
    states[state][2] += 1
    states[state][3] += NRxT
    states[state][4] += TRxT
    states[state][5] = [sum(x) for x in zip(states[state][5], NRxs)]
    states[state][6] = [sum(x) for x in zip(states[state][6], TRxs)]

    if i[4] == "Cholecap":
        states[state][7] += 1
        states[state][8] += NRxT
        states[state][9] += TRxT
        states[state][10] = [sum(x) for x in zip(states[state][10], NRxs)]
        states[state][11] = [sum(x) for x in zip(states[state][11], TRxs)]
    elif i[4] == "Nasalclear":
        states[state][12] += 1
        states[state][13] += NRxT
        states[state][14] += TRxT
        states[state][15] = [sum(x) for x in zip(states[state][15], NRxs)]
        states[state][16] = [sum(x) for x in zip(states[state][16], TRxs)]
    elif i[4] == "Nova-itch":
        states[state][17] += 1
        states[state][18] += NRxT
        states[state][19] += TRxT
        states[state][20] = [sum(x) for x in zip(states[state][20], NRxs)]
        states[state][21] = [sum(x) for x in zip(states[state][21], TRxs)]
    elif i[4] == "Zap-a-Pain":
        states[state][22] += 1
        states[state][23] += NRxT
        states[state][24] += TRxT
        states[state][25] = [sum(x) for x in zip(states[state][25], NRxs)]
        states[state][26] = [sum(x) for x in zip(states[state][26], TRxs)]

print(states)




# print(h)
# print(x[0])
# print(x[0][5:11])
# print(x[0][11:])

outputs = []
import json

for state in states:
    output = []

    output.append(state)
    output += states[state]
    outputs.append(output)

print(outputs)

with open("../state-data/Prescriber_Data_by_state.csv", 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerows(outputs)



