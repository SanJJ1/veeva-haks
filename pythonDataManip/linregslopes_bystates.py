import pandas as pd
from scipy import stats

df = pd.read_csv("./Prescriber_Data_by_state.csv")

slopes = [[], [], [], [], []]
for i in range(len(df.index)):
    res = []
    for j in range(5):
        starr = df.iloc[i, 1+5*(j+1)][1:-1].split(',')
        starr = [int(k) for k in starr]
        res.append(stats.linregress(list(range(1, 7)), starr))
        slopes[j].append(round(res.pop().slope, 2))

df['T_NRx_Slope'] = slopes[0]
df['CC_NRx_Slope'] = slopes[1]
df['NC_NRx_Slope'] = slopes[2]
df['NI_NRx_Slope'] = slopes[3]
df['ZP_NRx_Slope'] = slopes[4]

df.to_csv('Prescriber_Data_Processed_by_state.csv', index=False)
