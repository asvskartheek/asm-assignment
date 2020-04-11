import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('expectations_responses.csv')
for field in df.columns:
    sns.distplot(df[field])
    plt.show()