import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_excel("Pilot Questionnaire (Responses) consolidated 25.6.2019.xlsx")

column_name = 'Unnamed: 12'
# plt.ylabel('Frequency')

# cleaned_data = [x for x in df[column_name][1:] if x<=100]
cleaned_data = df[column_name][1:]
plt.xticks(np.arange(0, max(cleaned_data)+10, step=5))
plt.yticks(np.arange(0,39,step=2))
sns.distplot(cleaned_data,kde=True,bins=39)
plt.xlabel('Age (yrs)')
# plt.savefig('./distributions/age_dist.png')
plt.show()