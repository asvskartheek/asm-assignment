import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("Pilot Questionnaire (Responses) consolidated 25.6.2019.xlsx")
column_name = 'Unnamed: 16'
types = df[column_name][1:].unique()
frequencies = [0]*len(types)
explodes = [0]*len(types)
# explodes = [0,0,0,0.2]
for index,row in df.iterrows():
    for index,j in enumerate(types):
        if row[column_name]==j:
            frequencies[index] +=1

plt.title('Highest Qualification Distribution')
# plt.figure(figsize=(13,5))
plt.pie(frequencies,labels=types,autopct='%1.1f%%',explode=explodes)
# plt.show()
plt.savefig('qualification_pie.png')