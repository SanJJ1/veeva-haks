import pandas as pd
from scipy import stats

df = pd.read_csv("./Prescriber_Data.csv")

total_nrx = []
total_trx = []
slope_n = []
slope_t = []
for i in range(len(df.index)):
    sum1 = 0
    sum2 = 0
    arr_n = []
    arr_t = []
    for j in range(1, 6):
        valn = df[str('NRx_Month_' + str(j))][i]
        valt = df[str('TRx_Month_' + str(j))][i]
        sum1 += valn
        sum2 += valt
        arr_n.append(valn)
        arr_t.append(valt)
    total_nrx.append(sum1)
    total_trx.append(sum2)
    res_n = stats.linregress(list(range(1, 6)), arr_n)
    res_t = stats.linregress(list(range(1, 6)), arr_t)
    slope_n.append(round(res_n.slope, 2))
    slope_t.append(round(res_t.slope, 2))

df["NRx_all"] = total_nrx
df["TRx_all"] = total_trx
df["NRx_linreg"] = slope_n
df["TRx_linreg"] = slope_t

df.to_csv('Prescriber_Data_Processed.csv', index=False)
