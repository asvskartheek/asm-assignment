import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

labels = ['1st year','2nd year','Alumni','Asst. Prof','Assoc. Prof','Prof','Director','H.O.D- Assoc. Prof','Dean']
frequencies = [2,10,18,2,1,2,2,1,1]
plt.pie(frequencies,labels=labels,autopct='%1.1f%%')
plt.savefig('./Pie Charts/roll_pie.png')