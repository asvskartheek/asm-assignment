import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('demographics_responses.csv')

column_name = 'Stream'
# arr = np.array(df[column_name])
# arr = [x if x<=100 else 100 for x in arr]

# mean = np.mean(arr)
# std = np.std(arr)
# std /= np.sqrt(8)
# std *= 2.365
# print('mean:',mean)
# print('std:',std)
# print('lower limit:',mean-std)
# print('upper limit:',mean+std)

labels = df[column_name].unique()
frequencies = [0]*len(labels)

for index,row in df.iterrows():
    for index,j in enumerate(labels):
        if row[column_name]==j:
            frequencies[index] +=1

plt.pie(frequencies,labels=labels,autopct='%1.1f%%')
plt.show()
# plt.savefig('./Pie Charts/vs_location_pie.png')