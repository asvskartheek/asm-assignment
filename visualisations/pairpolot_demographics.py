import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('demographics_responses.csv')
sns.pairplot(df)
plt.show()