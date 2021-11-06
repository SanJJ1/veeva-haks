import pandas as pd

df = pd.read_csv("./Prescriber_Data.csv")

total_nrx = []
total_trx = []
for i in range(df.shape[0]):
    sum1 = 0
    sum2 = 0
    for j in range(1, 6):
        sum1 += df[str('NRx_Month_' + str(j))][i]
        sum2 += df[str('TRx_Month_' + str(j))][i]
        print(sum1)
    total_nrx.append(sum1)
    total_trx.append(sum2)

df["NRx_all"] = total_nrx
df["TRx_all"] = total_trx

df.to_csv('out.csv', index=False)


