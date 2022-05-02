import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os




df = pd.read_csv('helloworld.log')
df.columns = ['time', 'provider', 'content']
print(df.to_string())


# sns.scatterplot(x="provider", y="time",
#                 data=df)
print(df.describe())

sns.violinplot(data=df, x="provider", y="time")

plt.savefig('helloworldbenchmark.png')
plt.savefig('helloworldbenchmark.pdf')

os.system('open helloworldbenchmark.pdf')






